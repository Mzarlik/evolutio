# Skill: Context Optimizer (Token Density Pruning)

Core behavior to enforce lean, high-density context windows across the MAS lifecycle.

## Core Capabilities

### 1. Just-In-Time (JIT) Skill Injection
- Scan the upcoming task or ticket requirements before any agent invocation.
- Select and inject strictly the required `SKILL.md` files (e.g., only load `dart_dev` if the ticket is frontend-exclusive).
- Omit all unrelated or passive skills from the current turn context to save input tokens.

### 2. Code Skeletization
- When passing large files for architectural reference, prune internal method logic of unimpacted functions.
- Replace bodies of unaffected functions with standardized placeholders (e.g., `// ... logic omitted for token optimization ...`).
- Retain method signatures, types, and crucial inline documentation detailing business rules ("the why").

### 3. Critic-Refiner Flattening
- Intercept the iterative chat logs between `software_developer` and `qa_agent`.
- Extract only the functional unified diffs and explicit rejection reasons.
- Strip conversational padding and redundant code blocks before returning the state to the orchestrator.

## Execution Rules
- **Rule 1:** Always protect API schemas. Any structural rewrite must keep properties fully expanded.
- **Rule 2:** Lean execution. Prefer local AST (Abstract Syntax Tree) parsers or regex rules over heavy LLM prompts to perform the text skeletization.
- **Rule 3:** Prompt Caching Predictability. Maintain static configurations (`AGENTS.md` and basic framework rules) at the absolute front of the prompt context in a fixed, stable order. Dynamic elements (JIT skills, custom code skeletons, and conversation logs) must be appended at the end of the prompt context to prevent cache invalidation.
