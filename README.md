# evolutio

[![Antigravity](https://img.shields.io/badge/Orchestrator-Google%20Antigravity-blue.svg)](#)
[![Python](https://img.shields.io/badge/Backend-Python%20%7C%20FastAPI%20%7C%20Django-green.svg)](#)
[![PHP](https://img.shields.io/badge/Backend-PHP%20%7C%20Laravel-purple.svg)](#)
[![Dart](https://img.shields.io/badge/Frontend-Dart%20%7C%20Flutter-blue.svg)](#)

Welcome to **evolutio**, a repository structured for hybrid software development combining Python, PHP, and Dart/Flutter, fully automated under the **Agentic SDLC (ASDLC)** framework. 

This workspace is designed to be co-piloted by a Multi-Agent System (MAS) powered by **Google Antigravity**, utilizing custom-tailored workspace rules, specialized skills, and specialized subagents.

---

## 🚀 Tech Stack

*   **Python:** Frameworks like FastAPI and Django, linted with Ruff/Pylint, tested with `pytest`.
*   **PHP:** PSR-12 standard, strict typing declared (`declare(strict_types=1);`), frameworks like Laravel, tested with `phpunit` or `pest`.
*   **Dart & Flutter:** Effective Dart style guidelines, state management, and widget testing.

---

## 🤖 Agentic SDLC (ASDLC) Framework

The development lifecycle in this repository is divided into phases, each led by specialized agent personas coordinating via structured communication patterns.

### Workspace Customizations Structure (`.agents/`)
We configure our agents through the workspace-scoped customizations root folder:
*   [AGENTS.md](file:///.agents/AGENTS.md): Defines global rules, style guides, and agent guardrails.
*   [skills/](file:///.agents/skills/): Contains specialized instructions for Python, PHP, Dart/Flutter, database development, security compliance, and ASDLC workflows.
*   [agents/](file:///.agents/agents/): Host templates for spawning specialized subagents in the session.

### Core Guardrails
1.  **Critic-Refiner Loop Limit:** To prevent "deadlocks" and infinite loops during automated bug-fixing, code reviews between the developer and QA agents are capped at a **maximum of 3 iterations**. If unresolved, the issue is escalated to a human or the Software Architect.
2.  **Phase State Summary:** To keep context window token usage low and prevent memory leakage, every phase transition writes a structured **Phase State Summary** as the single source of truth for the next agent.

---

## 👥 Agentic Personas (Subagents)

| Agent Name | SDLC Phase | Focus Area |
| :--- | :--- | :--- |
| `enterprise_architect` | Phase 1: Planning | Scope, infrastructure alignment, and duplication checks. |
| `solutions_architect` | Phase 2: Analysis | Requirements specification (SRS) and API contract design. |
| `software_architect` | Phase 3: Design | Design patterns selection and schema modeling. |
| `software_developer` | Phase 4: Development | Modular code generation and legacy code refactoring. |
| `qa_agent` | Phase 5: Testing | Automated test writing, linter checks, and security audits. |
| `platform_architect` | Phase 6: Deployment | Infrastructure as Code (IaC) and canary releases. |
| `ai_sre` | Phase 7: Maintenance | Logging analysis, anomaly correlation, and CVE patching. |
| `technical_writer` | Transversal | Inline documentation checks and `SKILL.md` updates. |
| `api_contract_sync` | Transversal | Real-time Dart/Flutter code generation from backend endpoints. |
| `hitl_gatekeeper` | Transversal | Human approval coordinator (budgets, QA gates, Slack logs). |

---

## 🛠️ Getting Started

When working with Antigravity inside this repository, the agent will automatically load all rules and skills from the `.agents/` directory.

### Spawning a Subagent
Spawning a subagent uses the templates defined under `.agents/agents/`. For example, to invoke the QA Agent:
```json
{
  "Subagents": [
    {
      "TypeName": "qa_agent",
      "Role": "Security Auditor",
      "Prompt": "Audit the credentials in the src/ directory."
    }
  ]
}
```
