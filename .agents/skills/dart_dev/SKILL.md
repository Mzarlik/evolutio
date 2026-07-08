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
*   Variables and parameter names must be `camelCase`.
*   Classes, enums, extensions, and mixins must be `PascalCase`.
*   Source files, directories, and package names must be `snake_case`.

## Dependency Management
Use the `pub` package manager:
*   Get dependencies: `flutter pub get` or `dart pub get`
*   Upgrade dependencies: `flutter pub upgrade` or `dart pub upgrade`
*   Add dependency: `flutter pub add <package>`
*   Add dev dependency: `flutter pub add --dev <package>`

## Flutter Coding Best Practices
*   **Widget Composition:** Prefer breaking down large widget trees into smaller, reusable stateless widgets.
*   **State Management:** Follow clean architecture; decouple business logic from the UI layer (e.g., using BLoC, Riverpod, Provider, or Cubit).
*   **Constants:** Make constructor parameters `const` whenever possible to optimize rendering performance.
*   **Asset Management:** Ensure all asset pathways are declared correctly in `pubspec.yaml`.

## Testing & Verification
*   Tests should be located under the `test/` directory.
*   Run unit/widget tests: `flutter test`
*   Run specific test: `flutter test test/widget_test.dart`
*   Generate test coverage: `flutter test --coverage`
