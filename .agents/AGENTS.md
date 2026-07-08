# Workspace Rules & Guidelines

Welcome to the **evolutio** workspace. This document outlines the general code quality standards, conventions, and practices that all agents and developers must adhere to when working on this codebase.

## 1. General Principles
*   **Documentation:** Always maintain inline comments, docstrings, and README files. Explain the *why*, not just the *what*.
*   **Git Best Practices:** 
    *   Commit messages must be clear, concise, and follow Conventional Commits (e.g., `feat:`, `fix:`, `docs:`, `refactor:`).
    *   **Automated Backup Rule:** Before starting an autonomous code editing or bug-fixing loop, the agent must run `git stash` to capture a clean snapshot or create a temporary branch (e.g., `git checkout -b feature/bug-refinement-failed`). If refinement fails and escalates, the codebase can be restored instantly using a single git revert/restore command.
*   **Security:** Never commit credentials, tokens, or sensitive configuration details. Use environment variables (via `.env` templates).

---

## 2. Python Coding Style & Standards
*   **Style Guide:** Adhere to **PEP 8**. Use type hints for all function signatures.
*   **Tooling:** Use `ruff` or `black` for formatting and `pylint` for linting.
*   **Dependency Management:** Prefer `poetry` if a `pyproject.toml` is present; otherwise, use `pip` with `requirements.txt`.
*   **Testing:** Write unit tests using `pytest`. Place test files in the `tests/` directory.

---

## 3. PHP Coding Style & Standards
*   **Style Guide:** Follow **PSR-12** / **PER Coding Style 2.0**.
*   **Safety:** Always start PHP files with `declare(strict_types=1);`.
*   **Tooling:** Use `php-cs-fixer` or `phpcs` for syntax checks and formatting.
*   **Frameworks:** For Laravel applications, adhere to standard MVC/Service-Repository patterns and Eloquent best practices.
*   **Testing:** Write tests using `phpunit` or `pest`.

---

## 4. Dart & Flutter Style & Standards
*   **Style Guide:** Follow **Effective Dart** recommendations (casing, library structuring).
*   **Formatting:** Format code using `dart format`.
*   **Tooling:** Run `flutter analyze` or `dart analyze` to ensure there are no static analysis warnings or errors.
*   **Testing:** Use `flutter test` for unit and widget testing. Structure test files under the `test/` directory mimicking the `lib/` directory structure.

---

## 5. Agentic SDLC (ASDLC) Workflow Rules
*   **Role-Based Execution:** When assigned complex tasks, organize execution by mimicking the specialized roles (Solutions Architect, Software Developer, QA Agent, etc.).
*   **Bugs & Refactoring:** Use the **Critic-Refiner** pattern. Write the code, and then run a self-review or QA check to audit for potential edge cases, security issues, or performance drops.
*   **Integration:** Before creating new integrations, consult the API contracts or structural documentation of the system.

---

## 6. Critic-Refiner Loop Limit Guardrail
To prevent infinite correction loops (deadlock cognitivo) between developers and QA agents on minor issues:
*   **Iteration Limit:** A maximum of **3 refinement iterations** is allowed for a single block of code or feature.
*   **Escalation:** If the issue is not resolved within 3 iterations, execution must pause, and the developer/QA agents must escalate the problem to the **Software Architect** (for architectural review) or to the **human supervisor** with a brief diagnostic log.

---

## 7. Context Handoff & Phase State Summary
To prevent context window saturation and control FinOps cost:
*   **Handoff Document:** Every agent transitioning to a new phase must construct a **Phase State Summary** (Resumen de Estado de Fase) inside the brain folder. This serves as the single source of truth for the next agent, enabling them to work with clean context.
*   **Required Format:**
    1. **Current Status:** High-level summary of what was accomplished.
    2. **Key Outputs:** Links to newly created or modified files/specifications.
    3. **Architectural Decisions:** Crucial tradeoffs or constraints determined.
    4. **Pending Items:** Explicit tasks passed to the next agent.

---

## 8. Token Optimization and Context Pruning
To optimize prompt tokens and prevent LLM context bloat:
*   **Prompt Caching Predictability:** To maximize the hit rate of model caches, static files of larger size (like `AGENTS.md` and basic rules of `asdlc_workflow/SKILL.md`) must be loaded at the absolute prefix of the prompt context in a fixed, stable order. Dynamic elements (JIT skills, task-specific skeletons, diffs) must be appended at the end of the prompt context.
*   **JIT Skills Selection:** Feed only matching language/framework skills into the context based on task keywords.
*   **Code Skeletonization:** Trim method bodies of reference files to simple signatures using AST or regex parsers, always bypassing client/server contract schemas (files with `contract`, `api`, `client`, or `dto` in their names) to prevent type drift.
*   **Critic-Refiner Compression:** Trim redundant logs in loop cycles to extract only the raw code diffs and QA verdicts.

### Context Optimizer Agent
- **Ubicación:** `.agents/agents/context_optimizer.json`
- **Misión:** Intercepta las solicitudes y los estados de fase para reducir los tokens de entrada mediante la carga dinámica de habilidades y esqueletos de código, asegurando la máxima densidad semántica sin degradar las directrices del espacio de trabajo.
