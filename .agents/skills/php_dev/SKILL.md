---
name: PHP Development Skill
description: Guidelines and commands for developing, testing, and managing dependencies for PHP and Laravel applications.
---

# PHP Development Skill

This skill provides the execution patterns, commands, and best practices for developing PHP applications in this codebase.

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
*   Dump autoload: `composer dump-autoload`

## Framework Best Practices (Laravel)
*   **Eloquent Models:** Avoid placing complex business logic or raw queries inside controllers. Offload logic to Services or Repositories.
*   **Migrations:** Always use migrations to modify databases: `php artisan make:migration <name>` and `php artisan migrate`.
*   **Artisan Commands:**
    *   Clear cache: `php artisan optimize:clear`
    *   List routes: `php artisan route:list`
    *   Run queues: `php artisan queue:work`

## Testing & Verification
*   Tests are run via PHPUnit or Pest.
*   **PHPUnit:** `vendor/bin/phpunit`
*   **Pest:** `vendor/bin/pest`
*   Ensure mock objects are used for external APIs in testing environments.
