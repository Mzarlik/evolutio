# Global Workspace Rules & Guidelines

Welcome to the **evolutio** workspace. This document outlines the general code quality standards, conventions, and practices that all agents and developers must adhere to when working on this codebase.

## 1. General Principles
*   **Documentation:** Always maintain inline comments, docstrings, and README files. Explain the *why*, not just the *what*.
*   **Git Best Practices:** 
    *   Commit messages must be clear, concise, and follow Conventional Commits (e.g., `feat:`, `fix:`, `docs:`, `refactor:`).
    *   **Automated Backup Rule:** Before starting an autonomous code editing or bug-fixing loop, the agent must run `git stash` to capture a clean snapshot or create a temporary branch (e.g., `git checkout -b feature/bug-refinement-failed`). If refinement fails and escalates, the codebase can be restored instantly using a single git revert/restore command.
*   **Security:** Never commit credentials, tokens, or sensitive configuration details. Use environment variables (via `.env` templates).

---

## 2. API Contract Synchronization & Decoupling
To prevent project coupling and isolation failures in cross-language stacks (e.g., Python/PHP backend and Dart/Flutter mobile client):
*   **Decoupled Schema Registry:** All client-side code generation must rely exclusively on schemas exported to the shared directory `.agents/contracts/`.
*   **Backend Duty:** Backend developer/deployment agents (Python or PHP) must auto-generate and export a standard schema (e.g., `openapi.json`) into `.agents/contracts/` whenever endpoint signatures change.
*   **Frontend Duty:** The `api_contract_sync` agent reads exclusively from `.agents/contracts/` to update Dart client models, never accessing the backend directories directly.

---

## 3. Critic-Refiner Loop Limit Guardrail
To prevent infinite correction loops (deadlock cognitivo) between developers and QA agents on minor issues:
*   **Iteration Limit:** A maximum of **3 refinement iterations** is allowed for a single block of code or feature.
*   **Escalation:** If the issue is not resolved within 3 iterations, execution must pause, and the developer/QA agents must escalate the problem to the **Software Architect** (for architectural review) or to the **human supervisor** with a brief diagnostic log.

---

## 4. Context Handoff & Phase State Summary
To prevent context window saturation and control FinOps cost:
*   **Handoff Document:** Every agent transitioning to a new phase must construct a **Phase State Summary** (Resumen de Estado de Fase) inside the brain folder. This serves as the single source of truth for the next agent, enabling them to work with clean context.
*   **Required Format:**
    1. **Current Status:** High-level summary of what was accomplished.
    2. **Key Outputs:** Links to newly created or modified files/specifications.
    3. **Architectural Decisions:** Crucial tradeoffs or constraints determined.
    4. **Pending Items:** Explicit tasks passed to the next agent.

---

## 5. Token Optimization and Context Pruning
To optimize prompt tokens and prevent LLM context bloat:
*   **Prompt Caching Predictability:** To leverage the LLM's prompt caching mechanics, load larger static files (such as `AGENTS.md` and default framework instructions) at the absolute front of the prompt context in a fixed, stable order. Append dynamic parameters (JIT skills, task-specific skeletons, logs) at the end of the context to prevent cache invalidation.
*   **JIT Skills Selection:** Feed only matching language/framework skills into the context based on task keywords.
*   **Code Skeletonization:** Trim method bodies of reference files to simple signatures using AST or regex parsers, always bypassing client/server contract schemas (files with `contract`, `api`, `client`, or `dto` in their names) to prevent type drift.
*   **Critic-Refiner Compression:** Trim redundant logs in loop cycles to extract only the raw code diffs and QA verdicts.

---

## 6. Core Agents Registry
*   **Enterprise Architect:** `.agents/core/agents/enterprise_architect.json` - Phase 1 Planning orchestrator.
*   **Solutions Architect:** `.agents/core/agents/solutions_architect.json` - Phase 2 Analysis lead.
*   **Software Architect:** `.agents/core/agents/software_architect.json` - Phase 3 Design lead.
*   **Context Optimizer:** `.agents/core/agents/context_optimizer.json` - Token & Context Density Specialist.
*   **Technical Writer:** `.agents/core/agents/technical_writer.json` - Doc writer & validation checker.
*   **HITL Gatekeeper:** `.agents/core/agents/hitl_gatekeeper.json` - Human-in-the-loop coordinator.
