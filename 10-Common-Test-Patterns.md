# Common Test Patterns

Best Practices

## Use Descriptive Test Names

```python
def test_calculator_prints_division_by_zero_error_to_stderr(capsys):
    """Test that calculator prints specific error message to stderr."""
    # Clear test intention from the name
```

## Separate Concerns

```python
def test_calculation_logic():
    """Test the calculation logic separately from output."""
    assert calculate(5, 3) == 8

def test_output_formatting(capsys):
    """Test output formatting separately from logic."""
    print_result(8)
    captured = capsys.readouterr()
    assert captured.out == "Result: 8\n"
```

## Essential pytest Commands

### Run all tests

`:> pytest`

### Run tests in a specific file

`:> pytest test_calculator.py`

### Run tests matching a pattern

`:>  pytest -k "test_add"`

### Run tests with verbose output

`:>  pytest -v`

### Run tests and show local variables on failure

`:> $ pytest -l`

### Run tests and drop into debugger on failure

`:> $ pytest --pdb`

### Run tests and stop on first failure

`:> $ pytest -x`

### Run tests with coverage report

`:> pytest --cov=.`
