#!/usr/bin/env python3
import sys
import os
import re
import ast

# ---------------------------------------------------------
# 1. JIT Skill Selection Rules
# ---------------------------------------------------------
SKILLS_MAP = {
    "python": ["python_dev"],
    "fastapi": ["python_dev", "security_compliance"],
    "django": ["python_dev", "database_dev"],
    "flask": ["python_dev"],
    "php": ["php_dev"],
    "laravel": ["php_dev", "database_dev"],
    "composer": ["php_dev"],
    "dart": ["dart_dev"],
    "flutter": ["dart_dev"],
    "db": ["database_dev"],
    "database": ["database_dev"],
    "sql": ["database_dev"],
    "migration": ["database_dev"],
    "security": ["security_compliance"],
    "auth": ["security_compliance"],
    "cors": ["security_compliance"],
    "token": ["security_compliance"],
    "jwt": ["security_compliance"],
}

def get_jit_skills(task_description: str) -> list:
    """Analyze the task description and return necessary skills."""
    desc_lower = task_description.lower()
    selected_skills = set()
    for keyword, skills in SKILLS_MAP.items():
        if keyword in desc_lower:
            selected_skills.update(skills)
    
    # Always include workflow skill
    selected_skills.add("asdlc_workflow")
    return sorted(list(selected_skills))

# ---------------------------------------------------------
# 2. Dependency Heatmap Guardrail
# ---------------------------------------------------------
BYPASS_KEYWORDS = ["contract", "api", "client", "dto", "interface"]

def should_bypass_skeletonization(filepath: str) -> bool:
    """Check if the file matches dependency heatmap bypass keywords."""
    filename = os.path.basename(filepath).lower()
    return any(kw in filename for kw in BYPASS_KEYWORDS)

# ---------------------------------------------------------
# 3. Code Skeletonizers
# ---------------------------------------------------------
def skeletonize_python(code: str) -> str:
    """Uses Python's AST to replace method and function bodies with pass."""
    try:
        root = ast.parse(code)
    except SyntaxError:
        # Fallback to regex if syntax is invalid
        return code

    class BodyPruner(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            # Keep docstring if exists
            docstring = ast.get_docstring(node)
            new_body = []
            if docstring:
                new_body.append(ast.Expr(value=ast.Constant(value=docstring)))
            new_body.append(ast.Pass())
            node.body = new_body
            return node

        def visit_AsyncFunctionDef(self, node):
            docstring = ast.get_docstring(node)
            new_body = []
            if docstring:
                new_body.append(ast.Expr(value=ast.Constant(value=docstring)))
            new_body.append(ast.Pass())
            node.body = new_body
            return node

    pruned_ast = BodyPruner().visit(root)
    ast.fix_missing_locations(pruned_ast)
    return ast.unparse(pruned_ast)

def skeletonize_regex(code: str) -> str:
    """Simple regex fallback to strip function bodies between curly brackets."""
    # Matches function declarations and their bodies in braces
    # This is a basic implementation. Real environments might use full lexers.
    pattern = re.compile(
        r'(function\s+\w+\s*\(.*?\)\s*(?::\s*\w+)?\s*)\{(?:[^{}]|(?R))*\}',
        re.DOTALL
    )
    
    def replacer(match):
        return match.group(1) + "{\n    /* ... code omitted to optimize context ... */\n}"
    
    return pattern.sub(replacer, code)

def skeletonize_file(filepath: str) -> str:
    """Read, verify bypass status, and skeletonize a file."""
    if not os.path.exists(filepath):
        return f"Error: File {filepath} not found."
        
    if should_bypass_skeletonization(filepath):
        # Return full file content because it contains critical contract types
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
            
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
        
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".py":
        return skeletonize_python(code)
    elif ext in [".php", ".dart"]:
        return skeletonize_regex(code)
    else:
        return code

# ---------------------------------------------------------
# 4. Critic-Refiner History Compacter
# ---------------------------------------------------------
def compact_critic_history(raw_conversation: str) -> str:
    """Extracts only diffs and QA verdicts from conversation block."""
    compacted = []
    lines = raw_conversation.split('\n')
    
    in_diff = False
    diff_block = []
    
    for line in lines:
        if line.strip().startswith("```diff") or line.strip().startswith("```"):
            in_diff = not in_diff
            if not in_diff:
                compacted.append("\n".join(diff_block))
                diff_block = []
            continue
        
        if in_diff:
            diff_block.append(line)
        else:
            # Check for QA verdicts or critical error messages
            if any(verdict in line.lower() for verdict in ["verdict", "error", "fail", "approved", "rejection"]):
                compacted.append(line)
                
    return "\n".join(compacted)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python token_optimizer.py skills '<task description>'")
        print("  python token_optimizer.py skeletonize <file_path>")
        sys.exit(1)
        
    action = sys.argv[1]
    
    if action == "skills":
        task = sys.argv[2]
        print("JIT Skills recommended:", get_jit_skills(task))
    elif action == "skeletonize":
        path = sys.argv[2]
        print(skeletonize_file(path))
