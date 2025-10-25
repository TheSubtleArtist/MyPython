## Key Testing Principles

Some principles to keep in mind:

### Write Tests Early (Test-Inspired Development if not Test-Driven Development)

Consider writing tests alongside your code. This helps ensure your code is testable and meets requirements.

### Test Behavior, Not Implementation

Focus on what your code should do, not how it does it. This makes tests more resilient to refactoring.

### Keep Tests Simple and Focused

Each test should verify one specific behavior. If a test fails, it should be immediately clear what went wrong.

### Use Descriptive Test Names

Test names should clearly describe what is being tested and what the expected outcome is.

### Maintain Test Independence

Tests should not depend on each other. They should be able to run in any order.

### Use Tests as Documentation

Well-written tests serve as living documentation of how code should behave.

## pytest Best Practices

### Organize Tests with conftest.py

Use conftest.py files to share fixtures and configuration across test modules.

### Use Appropriate Fixture Scopes

Choose the right fixture scope (function, class, module, session) based on your needs.

### Parametrize Instead of Duplicating

Use @pytest.mark.parametrize to test multiple scenarios with the same logic.

### Mock External Dependencies

Use monkeypatch or unittest.mock to isolate your code from external services.

### Test Edge Cases and Error Conditions

Don’t just test the happy path. Test boundary conditions, invalid inputs, and error scenarios.

### Use Clear Assertions

Prefer specific assertions (assert x == 5) over generic ones (assert x).

## Working with AI-Generated Code

When working with AI-generated code, testing becomes even more critical:

### Always Verify AI Code

AI can generate syntactically correct but logically flawed code. Tests help catch these issues.

### Ask AI to Generate Tests Too

Use AI tools to help write comprehensive test suites for AI-generated code.

### Test Edge Cases Thoroughly

AI may not consider all edge cases. Supplement AI-generated tests with additional scenarios