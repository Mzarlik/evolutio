---
name: PHP Development Skill
description: Guidelines and commands for developing, testing, and managing dependencies for PHP and Laravel applications.
---

# PHP Development Skill

This skill provides the execution patterns, commands, and best practices for developing PHP applications.

## Code Standards & Strict Typing
*   Every PHP file must declare strict typing at the very top:
    ```php
    <?php
    declare(strict_types=1);
    ```
*   Follow the **PSR-12** / **PER Coding Style 2.0** guidelines.
*   Format check:
    *   **PHP-CS-Fixer:** `vendor/bin/php-cs-fixer fix --dry-run`
    *   **PHPCS:** `vendor/bin/phpcs --standard=PSR12 src/`

## Dependency Management
Always use `composer`:
*   Install dependencies: `composer install`
*   Add a dependency: `composer require <package>`
*   Add a dev dependency: `composer require --dev <package>`

## Framework Best Practices (Laravel)
*   **Eloquent Models:** Avoid placing complex business logic or raw queries inside controllers. Offload logic to Services or Repositories.
*   **Migrations:** Always use migrations to modify databases.
*   **Contract Export:** Whenever Laravel route footprints or database response types change, export/update the API schemas in `.agents/contracts/openapi.json`.

## Testing & Verification
*   Tests are run via PHPUnit or Pest.
*   **PHPUnit:** `vendor/bin/phpunit`
*   **Pest:** `vendor/bin/pest`
