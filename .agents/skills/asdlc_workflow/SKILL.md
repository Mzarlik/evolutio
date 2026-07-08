---
name: Agentic SDLC (ASDLC) Workflow Skill
description: Instructions and guidelines for executing software development phases using the Agentic SDLC roles and coordination patterns.
---

# Agentic SDLC (ASDLC) Workflow Skill

This skill incorporates the principles of the Agentic SDLC (ASDLC) framework to structure agent execution and collaborations.

## Agent Personas & Lifecycle Phases

When executing or coordinating tasks, align work with the appropriate phase and adopt the associated role:

1.  **Planning (Enterprise Architect Agent):**
    *   **Role:** Evaluates high-level business goals, aligns them with the organization's existing infrastructure, and structures Enabler Epics.
    *   **Key Action:** Scans repositories and documentation to avoid system and code duplication.
2.  **Analysis (Solutions Architect Agent):**
    *   **Role:** Translates requirements into formal specifications and API integration mechanisms.
    *   **Key Action:** Performs FinOps/cost simulations before planning heavy computational solutions.
3.  **Design (Software Architect Agent):**
    *   **Role:** Selects appropriate design patterns (hexagonal, MVC, layered) and models data schemas.
    *   **Key Action:** Documents architectural tradeoffs (latencies, storage requirements).
4.  **Development (Software Developer Agent):**
    *   **Role:** Generates clean, modular boilerplate code following established project pathways.
    *   **Key Action:** Applies refactoring patterns (like the strangler fig pattern for legacy logic).
5.  **Testing/QA (QA Agent):**
    *   **Role:** Writes automated unit and integration tests, and runs static linter checks.
    *   **Key Action:** Runs DevSecOps scans (credentials, SAST, SBOM, Docker scans).
6.  **Deployment (Platform Architect Agent):**
    *   **Role:** Validates Infrastructure as Code (IaC) and container configurations.
    *   **Key Action:** Executes safe canary or rolling deployments.
7.  **Maintenance (AI SRE Agent):**
    *   **Role:** Monitors logs, analyzes and correlates errors, and resolves live operational anomalies.
    *   **Key Action:** Automates dependency patching (CVE remediation).

---

## Agentic Coordination Patterns & Guardrails

### 1. Supervisor-Worker Pattern
*   The supervisor agent acts as the orchestrator. It divides complex requests into smaller, isolated, parallel tasks and assigns them to worker subagents.
*   Once worker subagents complete their tasks, the supervisor aggregates and validates the results before delivering them.

### 2. Critic-Refiner Pattern
*   For critical components (e.g., security logic, deployment scripts, core APIs), use a critic agent (QA/DevSecOps) to inspect the generated code of the developer agent.
*   **Guardrail (Loop Limit):** A maximum of **3 refinement iterations** is allowed for a single code block. If the issue is not resolved after the 3rd iteration, the loop must terminate, and the problem must be escalated to the **Software Architect** or **human supervisor** with a diagnostic log.

### 3. Router-Classifier Pattern
*   When receiving ambiguous user tickets or system anomalies, use a router agent to classify the issue domain (e.g., DB, Frontend, API, Infrastructure) and delegate it to the matching specialized subagent.

---

## Context Handoff & Phase State Summary

To keep the model context window clean and optimize FinOps token costs, every agent moving a task to the next phase must publish a **Phase State Summary** in the brain directory.

### Structure of the Summary:
1.  **Current Status:** High-level summary of what was accomplished in this phase.
2.  **Key Outputs:** Links to newly created or modified files/specifications.
3.  **Architectural Decisions:** Crucial tradeoffs or constraints determined.
4.  **Pending Items:** Explicit tasks passed to the next agent.

### Verification Guardrail:
*   Before the task is officially handed over to the next agent persona, the **Technical Writer Agent** must audit the Phase State Summary.
*   The Technical Writer will halt progression if any of the 4 mandatory points (Status, Outputs, Decisions, Pending) are missing or insufficient.

---

## Token Optimization & Context Pruning

To ensure high density of information and avoid high token consumption:

### 1. JIT Skill Selection
*   Prior to executing developer or QA tasks, the **Context Optimizer Agent** filters the skills list. Only skills matching keywords in the task description (e.g., `dart_dev` and `security_compliance` for auth in Flutter) are injected into the LLM context.

### 2. Code Skeletonization (Reference Code)
*   Files read purely for contextual reference are skeletonized (e.g., removing function/method bodies while preserving imports, declarations, and signatures) using `token_optimizer.py`.
*   **Heatmap Boundary:** API contracts, database interfaces, client communication classes, and data transfer objects (files containing `contract`, `api`, `client`, or `dto` in their names) **must never** be skeletonized. They must remain fully visible to prevent client-server typing failures.

### 3. Conversation Compactness in Critic-Refiner Loop
*   Between bug-fixing cycles, the **Context Optimizer Agent** prunes conversational logs, extracting only the raw code diffs and QA verdicts, removing redundant file copies from the prompt context.
