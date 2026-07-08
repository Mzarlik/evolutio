---
name: Agentic SDLC (ASDLC) Workflow Skill
description: Instructions and guidelines for executing software development phases using the Agentic SDLC roles and coordination patterns.
---

# Agentic SDLC (ASDLC) Workflow Skill

This skill incorporates the principles of the Agentic SDLC (ASDLC) framework to structure agent execution and collaborations.

## Agent Personas & Lifecycle Phases

When executing or coordinating tasks, align work with the appropriate phase and adopt the associated role:

1.  **Planning (Enterprise Architect Agent):**
    *   Align tasks with high-level business and infrastructure constraints.
    *   Scan repositories and documentation to avoid system and code duplication.
2.  **Analysis (Solutions Architect Agent):**
    *   Translate requirements into formal specifications and API integration mechanisms.
    *   Perform FinOps/cost simulations before planning heavy computational solutions.
3.  **Design (Software Architect Agent):**
    *   Select appropriate design patterns (hexagonal, microservices, layered) and model data schemas.
    *   Document architectural tradeoffs (latencies, storage requirements).
4.  **Development (Software Developer Agent):**
    *   Generate clean, modular boilerplate code following established project pathways.
    *   Apply refactoring patterns (like the strangler fig pattern for legacy logic).
5.  **Testing/QA (QA Agent):**
    *   Write extensive automated unit tests, edge-case simulations, and integration suites.
    *   Run DevSecOps scans (credentials, SAST, SBOM, Docker scans).
6.  **Deployment (Platform Architect Agent):**
    *   Validate Infrastructure as Code (IaC) files (Terraform/CloudFormation) and container configurations.
    *   Execute safe canary or rolling deployments.
7.  **Maintenance (AI SRE Agent):**
    *   Monitor logs, analyze and correlate errors, and resolve live operational anomalies.
    *   Automate dependency patching (CVE remediation).

---

## Agentic Coordination Patterns

When designing multi-agent processes or self-refining work, apply the following patterns:

### 1. Supervisor-Worker Pattern
*   The supervisor agent acts as the orchestrator. It divides complex requests into smaller, isolated, parallel tasks and assigns them to worker subagents.
*   Once worker subagents complete their tasks, the supervisor aggregates and validates the results before delivering them.

### 2. Critic-Refiner Pattern
*   For critical components (e.g., security logic, deployment scripts, core APIs), use a critic agent (QA/DevSecOps) to inspect the generated code of the developer agent.
*   The developer agent refines the code iteratively based on the critic's feedback until it satisfies the quality/security standards.

### 3. Router-Classifier Pattern
*   When receiving ambiguous user tickets or system anomalies, use a router agent to classify the issue domain (e.g., DB, Frontend, API, Infrastructure) and delegate it to the matching specialized subagent.
