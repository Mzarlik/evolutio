---
name: Dart & Flutter Development Skill
description: Instructions for writing Dart code, Flutter widgets, package management via pub, and running Flutter unit/widget tests.
---

# Dart & Flutter Development Skill

This skill provides the execution patterns, commands, and best practices for developing Dart and Flutter applications.

## Code Style & Formatting
*   Follow the **Effective Dart** rules.
*   Format code using: `dart format .`
*   Analyze code: `dart analyze` or `flutter analyze`

## Dependency Management
Use the `pub` package manager:
*   Get dependencies: `flutter pub get` or `dart pub get`
*   Upgrade dependencies: `flutter pub upgrade` or `dart pub upgrade`
*   Add dependency: `flutter pub add <package>`

## Flutter Coding Best Practices
*   **Widget Composition:** Prefer breaking down large widget trees into smaller, reusable stateless widgets.
*   **State Management:** Follow clean architecture; decouple business logic from the UI layer (e.g., using BLoC, Riverpod, Provider, or Cubit).

## API Contract Synchronization
*   **Decoupled Sync:** The Dart client/mobile frontend must never query backend python/php source directories directly.
*   **Schema Source:** Read the OpenAPI specification from the shared folder `.agents/contracts/openapi.json`.
*   **Generation:** Run standard Dart code generation tools (e.g., `build_runner` or `openapi-generator`) to auto-generate models, types, and services using the shared schema.
*   Run command: `flutter pub run build_runner build --delete-conflicting-outputs`

## Testing & Verification
*   Tests should be located under the `test/` directory.
*   Run unit/widget tests: `flutter test`
