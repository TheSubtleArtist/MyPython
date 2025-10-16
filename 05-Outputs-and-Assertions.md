## OUTPUT AND ASSERTIONS

### TESTING EXCEPTIONS

Testing error cases when code SHOULD raise and exception  

pytest provide ``pytest.raises`` context manager for testing exceptions  

#### Basic Exception Tesing

files: quadratic.py, quadratic_test.py  

Run the basic test: ``pytest quadratic.py quadratic_test.py``

```md
(.venv) PS D:\GitHub\MyPython> pytest quadratic.py quadratic_test.py
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
plugins: cov-7.0.0
collected 5 items                                                                                                                                           

quadratic_test.py .....                                                                                                                               [100%] 

==================================================================== 5 passed in 0.09s ===================================================================== 
(.venv) PS D:\GitHub\MyPython> 
```

### CAPTURING STANDARD OUTPUT

#### Method 1: Monkey Patch Print (Weak)

Based on a test method for total_air_travel example earlier The LLM used unittest.mock.pathc ot monkey patch the built-in print function  

```python
from unittest.mock import patch

# ...

class TestMain:
    """Test the main command-line interface function."""

    # ...

    @patch('sys.argv')
    @patch('builtins.print')
    def test_main_with_valid_file(self, mock_print, mock_argv, sample_csv_file):
        """Test main function with a valid CSV file."""
        # Mock command line arguments
        mock_argv.__getitem__.return_value = [sample_csv_file]
        mock_argv.__len__.return_value = 2  # script name + 1 argument

        # Call main function
        main()

        # Verify print was called with expected output
        mock_print.assert_called_once_with("Total air travel expenses: $800.25")

    @patch('sys.argv')
    @patch('builtins.print')
    def test_main_with_no_air_travel(self, mock_print, mock_argv, tmp_path):
        """Test main function with a CSV file containing no air travel expenses."""
        # Create CSV with no air travel
        csv_content = """Category,Cost,Description
Hotels,$150.00,Hotel stay
Food,$75.50,Meals"""

        csv_file = tmp_path / "no_air_travel.csv"
        csv_file.write_text(csv_content)

        mock_argv.__getitem__.return_value = [str(csv_file)]
        mock_argv.__len__.return_value = 2

        main()

        mock_print.assert_called_once_with("Total air travel expenses: $0.00")
```

This approach has several problems:

- Brittle - Assumes code uses built-in print instead of other ways to write to sys.stdout
- Complex - Requires understanding mocking concepts and decorators
- Unnecessary - pytest provides better built-in solutions

#### Method 2: contextlib.redirect_stdout (better)

Instead of monkey patching the built-in print function, we could monkey patch the standard output stream to capture all output.

We could do that with `contextlib.redirect_stdout`:

```python
import io
from contextlib import redirect_stdout
from unittest.mock import patch

# ...

class TestMain:
    """Test the main command-line interface function."""

    # ...

    @patch('sys.argv')
    def test_main_with_valid_file(self, mock_argv, sample_csv_file):
        """Test main function with a valid CSV file."""
        # Mock command line arguments
        mock_argv.__getitem__.return_value = [sample_csv_file]
        mock_argv.__len__.return_value = 2  # script name + 1 argument

        with redirect_stdout(io.StringIO()) as stdout:
            main()

        assert stdout.getvalue() == "Total air travel expenses: $800.25\n"
```

#### Method 3: pytest’s capsys fixture (best)

Instead of manually monkey patching print or `sys.stdout`, we could rely on pytest to capture output for us.

pytest’s `capsys` fixture captures anything written to `sys.stdout` and `sys.stderr`

Adding functionality to our test function by simply adding a parameter may seem a bit magical (and it is!). This capsys argument is a pytest fixture. We’ll cover fixtures in more detail later.  :  

```python
from unittest.mock import patch

# ...

class TestMain:
    """Test the main command-line interface function."""

    # ...

    @patch('sys.argv')
    @patch('builtins.print')
    def test_main_with_valid_file(self, mock_print, mock_argv, sample_csv_file, capsys):
        """Test main function with a valid CSV file."""
        # Mock command line arguments
        mock_argv.__getitem__.return_value = [sample_csv_file]
        mock_argv.__len__.return_value = 2  # script name + 1 argument

        # Call main function
        main()

        # Capture and verify output
        captured = capsys.readouterr()
        assert captured.out == "Total air travel expenses: $800.25\n"
        assert captured.err == ""
```

### Advanced Assertion Patterns

#### Testing Partial Output

```python
from unittest.mock import patch
from quadratic import main

@patch('sys.argv', ['quadratic.py', '1', '-5', '6'])
def test_main_partial_output(capsys):
    """Test that main prints solution values, not exact format."""
    main(['1', '-5', '6'])

    captured = capsys.readouterr()
    # Test that both solutions appear in output, regardless of exact format
    assert "3.0" in captured.out
    assert "2.0" in captured.out
    assert "x =" in captured.out
```

#### Testing with Regular Expressions

```python
import re
from unittest.mock import patch
from quadratic import main

@patch('sys.argv', ['quadratic.py', '1', '-3', '2'])
def test_main_regex_output(capsys):
    """Test output format using regex patterns."""
    main(['1', '-3', '2'])

    captured = capsys.readouterr()
    # Match pattern: "x = <number> or <number>"
    pattern = r"x = \d+\.\d+ or \d+\.\d+"
    assert re.search(pattern, captured.out)
```

#### Testing Multi-line output

uses `textwrap.dedent`

```python
import textwrap
from unittest.mock import patch
from quadratic import main, QuadraticError

def test_main_help_output(capsys, monkeypatch):
    """Test help output when no arguments provided."""
    # Simulate a version that prints usage when no args given
    def mock_main(args):
        if not args:
            print(textwrap.dedent("""
                Usage: quadratic.py <a> <b> <c>

                Solves quadratic equations of the form ax² + bx + c = 0

                Arguments:
                  a, b, c    Coefficients (a cannot be 0)
            """).strip())
            return
        # ... rest of original logic

    monkeypatch.setattr('quadratic.main', mock_main)
    main([])

    captured = capsys.readouterr()
    expected = textwrap.dedent("""
        Usage: quadratic.py <a> <b> <c>

        Solves quadratic equations of the form ax² + bx + c = 0

        Arguments:
          a, b, c    Coefficients (a cannot be 0)
    """).strip()

    assert captured.out == expected
```

### OUTPUT AND EXCEPTION TESTING EXERCISES

#### howdy

Write tests for the howdy function using pytest’s capsys fixture  

```md
Key Improvements with pytest and capsys:
1. Simplified Output Capture:
- capsys.readouterr() cleanly captures both stdout and stderr
- Automatic cleanup between tests
2. Parametrized Testing:
- @pytest.mark.parametrize for clean, readable test cases
- Easy to add new test cases without duplicating code
- Better test failure reporting with parameter values
3. Fixtures:
- Custom fixtures for reusable test data
- sample_names and special_characters fixtures for organized test data
- Automatic dependency injection
4. Better Error Handling:
- pytest.raises() for exception testing
- More intuitive assertion syntax with assert
5. Test Organization:
- Multiple test classes for logical grouping
- Custom markers (@pytest.mark.slow, @pytest.mark.integration)
- Easy selective test running
6. Enhanced Mocking:
- monkeypatch fixture for cleaner mocking
- No need to import separate mock libraries
7. Cleaner Assertions:
- Simple assert statements instead of self.assertEqual
- Better failure messages automatically generated
- Verification of both stdout and stderr
```

**Running the Tests**

Run all tests  
`pytest test_howdy.py -v`  

Run specific test class  
`pytest test_howdy.py::TestHowdyParameterized -v`  

Run tests with specific markers  
`pytest test_howdy.py -m "not slow" -v`  

Run with coverage  
`pytest test_howdy.py --cov=howdy -v`  

#### flip_dict

Write tests for the flip_dict function  
Example useage of flip_dict. The function raises ValueError when multiple keys have the same value because you can’t have duplicate keys in the flipped dictionary. :  

```python
>>> flip_dict({"a": 1, "b": 2})
{1: "a", 2: "b"}
>>> flip_dict({"x": "hello", "y": "world"})
{"hello": "x", "world": "y"}
>>> flip_dict({"a": 1, "b": 1})  # Duplicate values!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in flip_dict
ValueError: Duplicate dictionary values found
```

In this case, we can ask an LLM to identify and annotate errors in the code. the annotated code looks like: 

```python
def flip_dict_annotated(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    
    # ERROR 1: No type checking - function will fail with non-dict types
    # This will raise AttributeError if dictionary is None, list, string, etc.
    
    # ERROR 2: Doesn't handle unhashable values
    # If dictionary values contain lists, dicts, sets, etc., this will fail
    # when trying to use them as keys in the returned dictionary
    
    if len(set(dictionary.values())) != len(dictionary):
        # ERROR 3: set() call will fail if values are unhashable
        # Example: {1: [1, 2], 2: [3, 4]} will raise TypeError here
        
        raise ValueError("Duplicate dictionary values found")
        
    return {
        value: key  # ERROR 4: This line will fail if 'value' is unhashable
        for key, value in dictionary.items()
        # ERROR 5: No validation that 'value' can be used as a dictionary key
    }

# ADDITIONAL ISSUES:
# - No handling of empty dictionary (though this actually works fine)
# - No docstring examples showing expected behavior
# - ValueError message could be more descriptive
# - No handling of None values (though None is hashable, so this works)
```
**Basic Test Execution, With Verbosity**  

Run all tests in the file  
`pytest test_flip_dict.py`  

Run with verbose output (shows each test name)  
`pytest test_flip_dict.py -v`  

Run with extra verbose output (shows more details)  
`pytest test_flip_dict.py -vv`  

Run with quiet mode (minimal output)  
`pytest test_flip_dict.py -q`  

**Test Specific Classes**  

Run only basic functionality tests  
`pytest test_flip_dict.py::TestFlipDictBasicFunctionality -v`  

Run only error-related tests  
`pytest test_flip_dict.py::TestFlipDictTypeErrors -v`  

Run only unhashable value tests  
`pytest test_flip_dict.py::TestFlipDictUnhashableValues -v`  

Run multiple specific classes  
`pytest test_flip_dict.py::TestFlipDictBasicFunctionality test_flip_dict.py::TestFlipDictDuplicateValues -v`  

**Test Specific Methods**  

Run a single specific test  
`pytest test_flip_dict.py::TestFlipDictBasicFunctionality::test_flip_dict_simple -v`  

Run specific parameterized test  
`pytest test_flip_dict.py::TestFlipDictParameterized::test_flip_dict_valid_cases -v`  

Run multiple specific methods  
`pytest test_flip_dict.py::TestFlipDictBasicFunctionality::test_flip_dict_simple test_flip_dict.py::TestFlipDictTypeErrors::test_flip_dict_with_none_input -v`  

#### altprint

Write tests for the altprint function.

Hint: Since this function writes to sys.stdout, you’ll need to use pytest’s capsys fixture to capture the output.

**Running the Tests**

Run all tests  
`pytest test_altprint.py -v`  

Run only basic tests  
`pytest test_altprint.py::TestAltprintBasic -v`  

Run parameterized tests  
`pytest test_altprint.py::TestAltprintParameterized -v`  

Skip slow tests  
`pytest test_altprint.py -m "not slow" -v`  

Run with coverage  
`pytest test_altprint.py --cov -v`  

