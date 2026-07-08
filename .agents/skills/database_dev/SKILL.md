---
name: Database Development Skill
description: Guidelines and rules for database migrations, query optimization, N+1 query prevention, and safe rollbacks.
---

# Database Development Skill

This skill provides guidelines and constraints for database schema design, migrations, query performance optimization, and rollback strategies.

## Safe Database Migrations
*   **Irreversible Operations:** Avoid migrations that destroy or drop tables/columns without a backup plan. Always write a matching `down` migration (for PHP/Laravel) or ensure rollbacks work (for Python/Django).
*   **Zero Downtime:** When renaming columns or tables, use a multi-step deployment strategy (e.g., add new column -> sync data -> point code to new column -> drop old column).
*   **Locks:** Avoid running heavy schema modifications on live databases that hold exclusive locks on large tables.

## Query Performance & N+1 Prevention
*   **Eager Loading:** Always use eager loading to fetch related records instead of lazy loading to prevent N+1 query issues:
    *   *Laravel (Eloquent):* Use `Model::with('relation')` instead of looping and calling `$model->relation`.
    *   *Django:* Use `select_related()` (for ForeignKey/OneToOne) or `prefetch_related()` (for ManyToMany).
*   **Query Logs:** Enable query logging in development or staging to monitor SQL volume.

## Indexing Policies
*   **Foreign Keys:** Always add database indexes on foreign keys (`*_id` columns).
*   **Search Columns:** Index columns that are frequently used in `WHERE`, `ORDER BY`, or `JOIN` operations.
*   **High Cardinality:** Prefer indexing high cardinality columns. Avoid indexing columns with very low uniqueness (e.g., boolean flags).

## Rollback & Canary Deployments
*   If a canary deployment fails or generates anomalous latencies/errors, automatically trigger rollback scripts:
    *   Run backward migration steps.
    *   Revert connection configurations to the stable database replica if split.
