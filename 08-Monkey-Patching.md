# Monkey Patching

## LLM-Generated Mocking

Did you notice the @patch decorators that our LLM-generated tests used for total_air_travel.py?

The LLM used Python’s unittest.mock.patch to mock sys.argv and builtins.print:

```python
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
```

This is “monkey patching” - temporarily modifying objects during tests. The @patch decorator:

- Replaces the specified object with a mock
- Passes the mock as an argument to the test
- Automatically restores the original object when the test ends

While unittest.mock.patch works, pytest provides its own fixture called monkeypatch that’s often simpler to use.

## Remember patch_args?

Remember the patch_args fixture we created in the fixtures section? We used it to modify sys.argv for testing the dmath.py program:

```python
import sys
import pytest

@pytest.fixture(name="args")
def patch_args():
    """Set sys.argv to ["program.py"] and send to test function."""
    old_sys, sys.argv = sys.argv, ["program.py"]
    def set_args(*args):
        sys.argv = ["program.py", *args]
    yield set_args
    sys.argv = old_sys

# We could have used the monkeypatch fixture to accomplish the same thing more simply:

import sys
import pytest

@pytest.fixture(name="args")
def patch_args(monkeypatch):
    """Set sys.argv to ["program.py"] and send to test function."""
    monkeypatch.setattr("sys.argv", ["program.py"])
    def set_args(*args):
        sys.argv = ["program.py", *args]
    return set_args

# Notice that we don’t need to worry about cleanup - monkeypatch handles that automatically!
```

## Patching at the Point of Use 

Monkey patching isn’t magic - it’s just an attribute assignment. Where you patch matters!

Let’s create a simple dice rolling program to demonstrate this. Here’s the complete program (roll.py):

```python
import sys
from random import randint


def roll_dice(*nums):
    """Roll dice with the given number of sides and return the sum."""
    if not nums:
        nums = [6]
    return sum(randint(1, n) for n in nums)


def main():
    """Main function that parses command line arguments and rolls dice."""
    dice_sides = [int(n) for n in sys.argv[1:]]
    result = roll_dice(*dice_sides)
    print(result)


if __name__ == "__main__":
    main()
```

Notice how it imports randint from random. Now let’s see what happens when we try to test this.

Let’s make a test_roll.py file with a test that patches random.randint:

```python
import pytest
from roll import roll_dice

def test_roll_dice(monkeypatch):
    # Return 2 first, then 4
    monkeypatch.setattr("random.randint", lambda a, b: 3)
    result = roll_dice(6, 6)  # Roll 2 6-sided die
    assert result == 6, "roll 3 plus roll 3 is 6"
```

Let’s run that test now:

```md
$ pytest test_roll.py -v
====================== test session starts ===================

test_roll.py::test_roll_dice FAILED         [100%]

========================== FAILURES ==========================
_______________________ test_roll_dice _______________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x72a75ac130e0>

    def test_roll_dice(monkeypatch):
        # Return 2 first, then 4
        monkeypatch.setattr("random.randint", lambda a, b: 3)
        result = roll_dice(6, 6)  # Roll 2 6-sided die
>       assert result == 6, "roll 3 plus roll 3 is 6"
E       AssertionError: roll 3 plus roll 3 is 6
E       assert 8 == 6

test_roll.py:8: AssertionError
=================== short test summary info ===================
FAILED test_roll.py::test_roll_dice - AssertionError: roll 3 plus roll 3 is 6
====================== 1 failed in 0.03s ======================
```

The test failed!

This test failed because roll.py imports randint directly. When it calls randint(1, 6), it’s calling the imported function, not random.randint.

Patching should be performed where an object is used, which is not necessarily the same as where the object is defined.

Now let’s use the correct approach - patching where randint is used:

```python
import pytest
from roll import roll_dice

def test_roll_dice_correct_patch(monkeypatch):
    # Return 2 first, then 4
    monkeypatch.setattr("roll.randint", lambda a, b: 3)
    result = roll_dice(6, 6)  # Roll 2 6-sided die
    assert result == 6, "roll 3 plus roll 3 is 6"

```

Let’s run this test to see it succeed:

```md
$ pytest test_roll.py -v
====================== test session starts ======================
test_roll_right.py::test_roll_dice PASSED

======================= 1 passed in 0.01s =======================
```

The key insight: When roll.py imports randint, it creates a local reference. We must patch roll.randint (where it’s used), not random.randint (where it’s defined).

The rule is: patch where the object is used, not where it’s defined.

## Changing Directories

Remember in the Testing File Operations section, we used contextlib.chdir to test the make_readme function:

```python
import contextlib
from make_readme import make_readme

def test_make_readme(tmp_path):
    """Test creating a README file in current working directory."""
    project_name = "My Awesome Project"

    # Change to temporary directory and run function
    with contextlib.chdir(tmp_path):
        make_readme(project_name)

    readme_file = tmp_path / "readme.md"
    assert readme_file.exists()
```

We could use monkeypatch.chdir instead:

```python
from make_readme import make_readme

def test_make_readme(tmp_path, monkeypatch):
    """Test creating a README file in current working directory."""
    project_name = "My Awesome Project"
    monkeypatch.chdir(tmp_path)

    make_readme(project_name)

    readme_file = tmp_path / "readme.md"
    assert readme_file.exists()
```

The monkeypatch.chdir method changes the current directory and automatically changes it back when the test ends.

## pytest-mock

While monkeypatch is great for simple attribute setting, it doesn’t help us verify how mocked objects were called.

The unittest.mock.patch approach that the LLM used earlier does allow this, but pytest-mock provides a cleaner alternative.

First install it:

`$ pip install pytest-mock`

The pytest-mock plugin provides a mocker fixture that wraps Python’s unittest.mock.

We could refactor the LLM’s test to use mocker instead of @patch:

```python
def test_main_with_valid_file(mocker, sample_csv_file):
    """Test main function with a valid CSV file using mocker."""
    # Mock sys.argv
    mocker.patch('sys.argv', ['total_air_travel.py', sample_csv_file])

    # Mock print
    mock_print = mocker.patch('builtins.print')

    # Call main function
    main()

    # Verify print was called with expected output
    mock_print.assert_called_once_with("Total air travel expenses: $800.25")
```

This is cleaner than the @patch approach - no decorators and no extra parameters!

Here’s another example with a names.py file:

```python
from urllib.request import urlopen

api_url = "https://www.pseudorandom.name"

def get_name():
    """Get a random name from the API."""
    return urlopen(api_url).read().decode("utf-8").rstrip()

```

And here is a test_names.py file which uses the mocker fixture:

```python
from io import BytesIO

def test_get_name(mocker):
    # Mock urlopen
    mock_urlopen = mocker.patch(
        "names.urlopen",
        return_value=BytesIO(b"Trey Hunner\n"),
    )

    result = get_name()

    # Verify the function returned the right value
    assert result == "Trey Hunner"

    # Verify urlopen was called with the correct URL
    mock_urlopen.assert_called_once_with("https://www.pseudorandom.name")
```

The mocker fixture provides all the power of unittest.mock but with automatic cleanup like monkeypatch.

Key methods on mocked objects:

- assert_called_once() - Verify called exactly once
- assert_called_once_with(*args, **kwargs) - Verify called once with specific arguments
- assert_called_with(*args, **kwargs) - Verify last call had specific arguments
- call_count - Number of times called
- call_args - Arguments from last call
- call_args_list - List of all call arguments

## Patch Exercises

These exercises will help you practice monkey patching with monkeypatch and/or pytest-mock.

### Testing User Input

Here’s a fancy_input function that repeatedly prompts the user until they provide valid input (fancy_input.py):

```python
def fancy_input(question, validator):
    """Ask a question repeatedly until a valid response is given."""
    while True:
        reply = input(f"{question} ")
        try:
            return validator(reply)
        except Exception:
            print("\nPlease enter a valid response.\n")
```

The function works like this:

```md
response = fancy_input("What is your favorite number?", int)
What is your favorite number? 4.5

Please enter a valid response.

What is your favorite number? 5,000

Please enter a valid response.

What is your favorite number? 5000
response
5000
```

Your task is to write tests for this function in a file called test_fancy_input.py. You’ll need to mock builtins.input to simulate user input.

Hints:

- Use either monkeypatch.setattr or mocker.patch to replace builtins.input

- Test both successful validation and retry scenarios

- Use capsys to verify the printed output

Remember that input is called multiple times in the retry scenario

Write tests that verify:

- Valid input is returned correctly after validation

- Invalid input causes the question to be asked again

- The exact text printed to the screen matches the expected format

### Testing Date-Dependent Code

Here’s a friday.py program that prints “FRIDAY” only when today is Friday (friday.py):

```python
from datetime import date

# 0 means Monday, 1 means Tuesday, etc.
if date.today().weekday() == 4:
    print("FRIDAY")
```

Testing this program is tricky because it depends on the current date. You need to patch datetime.date.today() to return specific dates for testing.

Here’s a flawed patch_date function that doesn’t properly clean up after itself:

```python
def patch_date(year, month, day):
    """Monkey patch the current time to be the given time."""
    import datetime

    date_args = year, month, day

    class FakeDate(datetime.date):
        """A datetime.date class with mocked today method."""
        @classmethod
        def today(cls):
            return cls(*date_args)

    def set_date(year, month, day, *rest):
        nonlocal date_args
        date_args = year, month, day

    datetime.date = FakeDate

    return set_date
```

This function modifies datetime.date globally and never restores the original class!

Your task:

Create a proper pytest fixture called set_date that safely mocks datetime.date.today()

Use either monkeypatch or pytest-mock to ensure proper cleanup

Write tests for the friday.py program in a file called test_friday.py that verify:

It prints “FRIDAY” when today is Friday (weekday 4)

It prints nothing on other days of the week

Hints:

You may need to mock friday.date.today (where it’s used) instead of datetime.date.today (where it’s defined)

A Friday in 2030 is September 13th (2030-09-13)

A Thursday in 2030 is September 12th (2030-09-12)

Remember to import the main function or friday module in your tests

### Testing Command-Line Programs

Here’s a four.py program that plays a number-to-word game (four.py):

```python
import sys

def number_to_word(n):
    """Convert single digit number to word."""
    words = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    return words[n]

def main():
    number = int(sys.argv[1])

    while number != 4:
        word = number_to_word(number)
        letter_count = len(word)
        print(f"The word {word} has {letter_count} letters in it.")
        number = letter_count

    print("The word four has 4 letters in it.")
    print("Done.")

if __name__ == "__main__":
    main()
```

The program works like this:

```md
$ python3 four.py 1
The word one has 3 letters in it.
The word three has 5 letters in it.
The word five has 4 letters in it.
The word four has 4 letters in it.
Done.
```

Your task:

Write tests for this program’s main function in a file called test_four.py. You’ll need to:

Mock sys.argv to simulate command-line arguments

Use capsys to capture and verify the printed output

Test different starting numbers (like 1, 2, 7) to ensure the logic works

Hints:

Create an args fixture or use monkeypatch.setattr to control sys.argv

Remember that sys.argv[0] is the script name, so sys.argv[1] is the first argument

All numbers eventually lead to 4, but they take different paths

### Jot

Here’s a jot.py program that saves quick thoughts to a file with timestamps (jot.py):

```python

from datetime import date
from pathlib import Path

def main():
    text = input("jot: ")
    jot_path = Path.home() / "jot.txt"

    with open(jot_path, mode="at") as jot_file:
        print(date.today(), text, file=jot_file)

if __name__ == "__main__":
    main()
```

The program works like this:

```md
$ python3 jot.py
jot: raisin M&M
This appends 2023-01-01 raisin M&M to ~/jot.txt (assuming today is 2023-01-01).
```

Your task:

Write tests for this program’s main() function in a file called test_jot.py. This is challenging because you need to mock multiple things:

Mock user input - builtins.input to simulate what the user types

Mock the current date - datetime.date.today to control the timestamp

Mock the file path - pathlib.Path.home to avoid writing to the real home directory

Use tmp_path to create a temporary directory for testing file operations.

Hints:

Use the set_date fixture approach from the “Testing Date-Dependent Code” exercise to safely mock dates

Mock builtins.input to simulate user input

Mock jot.Path.home to redirect file operations to your tmp_path

Remember to verify that the file content matches the expected format

This exercise combines concepts from all previous exercises: input mocking, date mocking (using fixtures), and file operations!

