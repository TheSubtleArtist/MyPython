## CREATING FIXTURES

### What are Fixtures

Functions that provide a fixed baseline for tests to run consistently. they can set up test data, configure tests, or even rely on other fixtures.  

Main Benefits:  

- Reusability: share setup code across multiple tests
- Isolation: Each test gets fresh, clean data  
- Teardown: Automatically clean up after tests
- Dependency isolation: Test receive exactly what they need  
- 

Fixtures are created by decorating a function with the `@pytest.fixture` decorator turning that function into a pytest fixture.  

Use a fixture in a test by adding an arguement which has the same name as the fixture, to the test. 

### Fixtures are Magical  

Before pytest calls a test function, it will introspect the function object to see which arguments it accepts.  
If any of those arguments don’t have some other meaning, pytest assumes that they’re fixture names.  
Those fixture functions will be automatically called and their return value will be passed into the test function as its called..  

It’s also a bit implicit.  
Where was this fixture defined? Is it a pytest built-in fixture, a fixture we created, a fixture provided by a third-party library? Where does it live.  

Hunting down fixtures can be tricky sometimes and occasionally in moments of fixture-hunting frustration.  

### Naming Fixtures  

Set the name of the fixture using the name keyword argument:  

```python
@pytest.fixture(name='sample_csv_content')
def sample_csv_content_fixture():
    """Provide sample CSV content for testing."""
    return """Category,Cost,Description
Air Travel,$450.00,Flight to NYC
Hotels,$200.00,Hotel stay
Air Travel,$325.50,Return flight
Food,$85.25,Dinner
Air Travel,$150.00,Domestic flight"""
```  

### Fixture Depedencies  

Fixtures can depend on other fixtures. For example, our LLM-generated tests for total_air_travel.py generated a sample_csv_file fixture that relied on pytest’s tmp_path fixture:

```python
import pytest

# ...

class TestMain:
    """Test the main command-line interface function."""

    @pytest.fixture
    def sample_csv_file(self, tmp_path):
        """Create a sample CSV file for main() testing."""
        csv_content = """Category,Cost,Description
Air Travel,$500.00,Business trip
Hotels,$150.00,Hotel stay
Air Travel,$300.25,Personal travel"""

        csv_file = tmp_path / "test_expenses.csv"
        csv_file.write_text(csv_content)
        return str(csv_file)

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

    # ...
```
  
The test_main_with_valid_file test function doesn’t need to care that sample_csv_file relies on the tmp_path fixture to create a temporary file.  

The temporary file will be automatically deleted after the test wraps up, just as if we used the tmp_path had been used in our test directly.  

### Fixtures That Do Stuff  

Another common use case of fixtures is to do something before and/or after each test.

Let’s write a fixture that monkey-patches sys.argv to make it easier to test functions that rely on command-line arguments.

Let’s say we want to test the parse_args function in this dmath.py program. This program performs date math: it can add/subtract days from a date, or calculate the difference between two dates

dmath.py

Let’s make a fixture that changes sys.argv to a new list and returns that new list. This is placed in the `dmath_test.py` by adding an `args` arguement to each test:  

```python
import pytest
import sys


@pytest.fixture(name="args")
def patch_args():
    """Set sys.argv to ["program.py"] and send to test function."""
    argv = ["program.py"]
    sys.argv = argv
    return argv
```  

### Teardown Fixtures  

Fixtures can also have a tear down step.

In our args fixture we should probably set sys.argv back to its previous value after each of our tests end.

We can do that by making our fixture into a generator function, by using the yield statement: 

```python
import sys

import pytest


@pytest.fixture(name="args")
def patch_args():
    """Set sys.argv to ["program.py"] and send to test function."""
    old_sys, sys.argv = sys.argv, ["program.py"]
    yield sys.argv
    sys.argv = old_sys
```

The code after the `yield` statement will be executed after each test the same way the code before yield will be executed before each test.  

### Factory Fixtures  

If a fixture needs some sort of input in order to do their work, that fixture could return a function that does the actual work of the fixture.  
This allows us to delay the fixture work until the function is called.  
This is called a factory as fixture pattern.  
Here we’re returning a function which will set sys.argv (rather than returning the sys.argv list):  

```python
import datetime
import sys

import pytest

from dmath import parse_args


@pytest.fixture(name="args")
def patch_args():
    """Set sys.argv to ["program.py"] and send to test function."""
    old_sys, sys.argv = sys.argv, ["program.py"]
    def set_args(*args):
        sys.argv = ["program.py", *args]
    yield set_args
    sys.argv = old_sys


def test_no_args(args):
    with pytest.raises(SystemExit) as e:
        parse_args()


def test_single_integer_parsed(args):
    args("5")
    result = parse_args()
    assert result.days_or_date == 5
    assert result.date == datetime.date.today()


def test_invalid_input(args):
    args("invalid")
    with pytest.raises(SystemExit) as e:
        parse_args()


def test_date_only_no_second_arg(args):
    args.extend(["1999-12-31"])
    result = parse_args()
    assert result.date == datetime.date.today()
    assert result.days_or_date == datetime.date(1999, 12, 31)


def test_date_and_days(args):
    args("1999-12-31", "5")
    result = parse_args()
    assert result.date == datetime.date(1999, 12, 31)
    assert result.days_or_date == 5


def test_two_dates(args):
    args("2000-01-01", "2000-01-10")
    result = parse_args()
    assert result.date == datetime.date(2000, 1, 1)
    assert result.days_or_date == datetime.date(2000, 1, 10)


def test_default_date_with_days(args):
    args("30")
    result = parse_args()
    assert result.date == datetime.date.today()
    assert result.days_or_date == 30
```

### conftest  

Where do you store fixtures when you want to use them within multiple test modules?  
You can use a `conftest.py` file for this!  
We could move our args fixture into a conftest.py file for example to use it within multiple test modules:  

### Fixture Exercises

#### Dollars Main Function

Use the `args` fixture in `conftest.py` to update tests for dollars.py 

Write tests for the main function in your test_dollars.py file:

- Test various dollar amounts using `capsys` to verify printed output
- Test invalid inputs (like non-numeric strings) that should cause SystemExit
- Use your `args` fixture to control command-line arguments

#### Exploriing LLM Fixtures

Look for custom fixtures that were defined in LLM-generated tests. You can search for pytest.fixture in these files to find them:

- test_percent_to_grade.py
- test_phonetic.py
- test_rock.py
- test_vote_tally.py

Ask yourself questions about the fixtures you find:

- Do you understand how they work?
- What do they provide to the tests?
- How do they use fixture dependencies? (if they do)
- Are they using any pytest built-in fixtures like tmp_path or capsys?

#### File Path Arguements

Write an `path_arg` fixture that:

- Uses the args fixture and the tmp_path fixture
- Puts a specific file path in the first argument of sys.argv
- Returns that pathlib.Path object so you can call write_text on it

Then use this fixture to write tests for the main function of `line_numbers.py`.

Your fixture should allow you to write tests like:

```python
def test_main_with_multiple_lines(path_arg, capsys):
    path_arg.write_text("line 1\nline 2\nline 3\n")
    main()
    captured = capsys.readouterr()
    assert "1 line 1" in captured.out
    assert "2 line 2" in captured.out
    assert "3 line 3" in captured.out
```

#### Data Fixutrue Refactoring

Pick one of these test files to refactor:

- test_fix_newlines.py
- test_line_numbers.py
- test_sum_timestamps.py
- test_fix_csv.py

Create data fixtures to eliminate repetitive test data setup. For example:

- CSV content fixtures for multiple test scenarios
- File content fixtures for different file types
- Edge case data fixtures for boundary testing  

#### Track Time Processing

Write tests for the main function of sum_timestamps.py.  
You could use a version of our args fixture or you could write a custom fixture.  
Hint: you’ll want to use tmp_path and capsys as well.  

#### Multi-File Factory Fixtures

Create a with_path_args factory fixture that:

- Accepts any number of multi-line strings
- Dedents them an
- Puts the paths to those files in sys.argv in the order given (using the args fixture)
- Returns a iterable of the new paths, in order

Then use this to write tests for the main function of fix_csv.py.

Your fixture should allow you to write tests like:  

```python
def test_main_pipe_to_comma_conversion(with_path_args):
    input_file, output_file = with_path_args(
        """Name|Age|City
        John|30|New York
        Jane|25|Boston""",
        ""
    )

    main()

    result = output_file.read_text()
    assert "John,30,New York" in result
    assert "Jane,25,Boston" in result
```

## More on Fixtures

### Passing Data to Fixtures

We could also use markers to send data into a fixture.

Here we’ve “marked” our tests with an argv marker and we’re reading that argv marker by using the request fixture (our fixture is relying on a pytest built-in fixture):

```python

import datetime
import sys

import pytest

from dmath import parse_args


@pytest.fixture(name='args')
def patch_args(request):
    """Set sys.argv to ['program.py'] and send to test function."""
    old_sys, sys.argv = sys.argv, ['program.py']
    argv_marker = request.node.get_closest_marker("argv")
    if argv_marker is not None:
        sys.argv += argv_marker.args
    yield sys.argv
    sys.argv = old_sys

def test_no_args(args):
    with pytest.raises(SystemExit) as e:
        parse_args()

@pytest.mark.argv('5')
def test_single_integer_parsed(args):
    result = parse_args()
    assert result.days_or_date == 5
    assert result.date == datetime.date.today()

@pytest.mark.argv('invalid')
def test_invalid_input(args):
    with pytest.raises(SystemExit) as e:
        parse_args()

@pytest.mark.argv('1999-12-31')
def test_date_only_no_second_arg(args):
    with pytest.raises(SystemExit) as e:
        parse_args()

@pytest.mark.argv('1999-12-31', '5')
def test_date_and_days(args):
    result = parse_args()
    assert result.date == datetime.date(1999, 12, 31)
    assert result.days_or_date == 5

@pytest.mark.argv('2000-01-01', '2000-01-10')
def test_two_dates(args):
    result = parse_args()
    assert result.date == datetime.date(2000, 1, 1)
    assert result.days_or_date == datetime.date(2000, 1, 10)

@pytest.mark.argv('30')
def test_default_date_with_days(args):
    result = parse_args()
    assert result.date == datetime.date.today()
    assert result.days_or_date == 30
```

You can see what else you can do with that request fixture in the documentation.

You’ll want to modify your pytest.ini file (or make a new one) to inform it of this new argv marker:


[pytest]
markers =
    argv: Mark command line arguments to use with args fixture
Alternatively you could add this to conftest.py to modify your pytest configuration for you (plugins often do this to register their markers automatically):

```python


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", "argv: Mark command line arguments to use with args fixture"
    )
```

### Automatic Fixtures

You can automatically use a fixture for every test in a module by setting a global pytestmark variable equal to pytest.mark.usefixtures(FIXTURE_NAME):

```python
import datetime
import sys

import pytest

from dmath import parse_args


pytestmark = pytest.mark.usefixtures("args")


def test_no_args():
    with pytest.raises(SystemExit) as e:
        parse_args()

@pytest.mark.argv('5')
def test_single_integer_parsed():
    result = parse_args()
    assert result.days_or_date == 5
    assert result.date == datetime.date.today()

@pytest.mark.argv('invalid')
def test_invalid_input():
    with pytest.raises(SystemExit) as e:
        parse_args()

@pytest.mark.argv('1999-12-31')
def test_date_only_no_second_arg():
    with pytest.raises(SystemExit) as e:
        parse_args()

@pytest.mark.argv('1999-12-31', '5')
def test_date_and_days():
    result = parse_args()
    assert result.date == datetime.date(1999, 12, 31)
    assert result.days_or_date == 5

@pytest.mark.argv('2000-01-01', '2000-01-10')
def test_two_dates():
    result = parse_args()
    assert result.date == datetime.date(2000, 1, 1)
    assert result.days_or_date == datetime.date(2000, 1, 10)
```

Or you can make every test method in a class use a fixture automatically by using pytest.mark.usefixtures as a class decorator:

```python
import datetime
import sys

import pytest

from dmath import parse_args


@pytest.mark.usefixtures("args")
class Test_parse_args:
    def test_no_args(self):
        with pytest.raises(SystemExit) as e:
            parse_args()

    @pytest.mark.argv('5')
    def test_single_integer_parsed(self):
        result = parse_args()
        assert result.days_or_date == 5
        assert result.date == datetime.date.today()

    @pytest.mark.argv('invalid')
    def test_invalid_input(self):
        with pytest.raises(SystemExit) as e:
            parse_args()

    @pytest.mark.argv('1999-12-31')
    def test_date_only_no_second_arg(self):
        with pytest.raises(SystemExit) as e:
            parse_args()

    @pytest.mark.argv('1999-12-31', '5')
    def test_date_and_days(self):
        result = parse_args()
        assert result.date == datetime.date(1999, 12, 31)
        assert result.days_or_date == 5

    @pytest.mark.argv('2000-01-01', '2000-01-10')
    def test_two_dates(self):
        result = parse_args()
        assert result.date == datetime.date(2000, 1, 1)
        assert result.days_or_date == datetime.date(2000, 1, 10)

```

We can even make a fixture that’s automatically used in every test by passing an autouse=True argument when defining our fixture:

```python


import sys

import pytest


@pytest.fixture(name='args', autouse=True)
def patch_args(request):
    """Set sys.argv to ['program.py'] and send to test function."""
    old_sys, sys.argv = sys.argv, ['program.py']
    argv_marker = request.node.get_closest_marker("argv")
    if argv_marker is not None:
        sys.argv += argv_marker.args
    yield sys.argv
    sys.argv = old_sys
```

Though it’s probably best not to automatically use most fixtures.

Note that in all the above cases (using pytest.mark.usefixtures or autouse=True) that we don’t get access to the actual return value of the fixture.

### Fixture Scope

If you don’t want a fixture to be re-run for every test that uses it, you can change the fixture scope from “function” (the default) to “class”, “module”, “package”, or “session”. The “session” scope means the fixture will be run just once for the whole testing session (the entire Python process execution).

