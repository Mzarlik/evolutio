---
name: Security & Compliance Skill
description: Security standards for input sanitization, password hashing, CORS, and token authentication.
---

# Security & Compliance Skill

This skill outlines the minimum security requirements and compliance regulations that must be audited and enforced across the codebase.

## Input Sanitization & Injection Prevention
*   **SQL Injection:** Always use parameterized queries or ORM interfaces. Never concatenate user input directly into raw SQL query strings.
*   **XSS Prevention:** Escape all output before rendering it in templates or HTML nodes. Use framework-provided escaping utilities (e.g., Blade `{{ }}` syntax in Laravel or Django's default escaping).
*   **Validation:** Apply strict request parameter validation on all endpoints (e.g., Pydantic models in FastAPI or Request validation classes in Laravel).

## Password Security
*   **Hashing:** Passwords must be hashed using a strong, slow-hashing algorithm before database insertion:
    *   Use **Argon2id** or **bcrypt** with an appropriate work factor (rounds).
    *   *Never* store plain text passwords, MD5, or SHA-1 hashes of passwords.
*   **Secrets:** Keep salting and hashing configuration variables out of code; use project secrets.

## Cross-Origin Resource Sharing (CORS)
*   **Production Constraints:** In production, never configure CORS headers with a wildcard (`Access-Control-Allow-Origin: *`). Specify exact origin domains.
*   **Credentials:** Avoid enabling `Access-Control-Allow-Credentials` when wildcards are active.

## Token Configuration & Lifetime Policies
*   **JWT Lifetimes:** Keep access token lifetimes short (e.g., 15 minutes). Use secure refresh tokens stored in `HttpOnly` cookies to renew sessions.
*   **Token Verification:** Always verify signatures, expiration (`exp` claim), and issuer (`iss` claim) on every inbound authenticated request.
