# Modern Python Testing

## Modern Testing with pytest and LLMs

https://modern-testing.pym.dev/  

Original material taught by Trey Hunner of Truthful Technology LLC.  


### Testing Fundamentals

Test Case: A single test scenario  
Test Suite: Collection of related tests  
Assertion: A statement that must be true for the test to pass  

### Creating a virtual python environment  

Useful for keeping the installed Python packages for your Python project separate from other Python projects on your machine.  

Navigate to the directory where necessary files are stored

Create the virtual environment: `:> python3 -m venv .myvenv --prompt='testing'`

- ".myvenv" designates the name of the folder where the new virtual environment is stored. Files stored here will be deleted when the virtual environment is deleted    
- "--prompt='testing'" designates the prompt display text  

### Activate the virtual environment

Linux:  `:> source .myvenv/bin/activate`  
Windows: `:> .venv\Scripts\activate`

The virtual environment is activated when '(testing)' is displayed as the prompt.  

Verify the location from where the new enviornment is running:  

```md
:> (testing) PS D:\GitHub\MyPython> pip -V
pip 25.2 from D:\GitHub\MyPython\.myvenv\Lib\site-packages\pip (python 3.13)
```  

The environment is running from within the '.myvenv' directory.  

### Deactivate a VENV

`:> deactivate`

### Delete a VENV  

Deactivate first
Delete with unix command: `:> rm -r .venv`
Delete with Pipenv when Pipenv was used to create the venv. must be inside the project directory, so that Pipenv and Pipenv.lock files are visible: `:>pipenv --rm`

### Install pytest  

```bash
:> (testing) PS D:\GitHub\MyPython> pip install pytest
Collecting pytest
  Downloading pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB)
Collecting colorama>=0.4 (from pytest)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting iniconfig>=1 (from pytest)
  Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging>=20 (from pytest)
  Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting pygments>=2.7.2 (from pytest)
  Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Downloading pytest-8.4.2-py3-none-any.whl (365 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Downloading packaging-25.0-py3-none-any.whl (66 kB)
Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 17.6 MB/s  0:00:00
Installing collected packages: pygments, pluggy, packaging, iniconfig, colorama, pytest
```

### Getting Started with pytest 

create ``test_calculator.py`` 

#### Test Discovery

pytest automatically finds tests using these rules:  

- Test files: test_*.py or *_test.py  
- Test classes: Test* (must start with Test)  
- Test functions: test_* (must start with test_)  

#### Running all test  

`:> pytest` # runs all tests in the current and subdirectories  

#### Verbose Output  

`:> pytest -v` # shows indivdiual test names and results  

### Teseting Exercises  

- dollars
- to_percent
- rock
- vote_tally

## Debugging

### The Python Debugger

- Step through code line by line
- Inpsect variables at any point
- Set breakpoints to pause execution
- Run code

### A Broken Program

```python
from random import randint

answer = randint(0, 1)
n = input("Guess: 0 or 1? ")

if n == answer:
    print("Correct!")
else:
    print(f"Incorrect. The answer was {answer}.")
```

Running `guess.py` always results in an "incorrect" answer

### Breakpoint

add `breakpoint()` call to top of code, or where the step through shoud begin

When program runs, `(pdb)` becomes the prompt

`l` command shows the current location in the program  

```python
> d:\github\mypython\guess.py(3)<module>()
-> breakpoint()
(Pdb) l
  1     from random import randint
  2
  3  -> breakpoint()
  4
  5     answer = randint(0, 1)
  6     n = input("Guess: 0 or 1? ")
  7
  8     if n == answer:
  9         print("Correct!")
 10     else:
 11         print(f"Incorrect. The answer was {answer}.")
(Pdb)
```

`n` command runs the line of code on which the program currently sits  

```python
(Pdb) n
> /home/trey/guess.py(6)<module>()
-> n = input("Guess: 0 or 1? ")
```

Run statements and see their results
`:> (Pdb) answer` to show the value for the answer variable:

`n` execute the line of code that asks the user to guess 0 or 1

```python
(Pdb) l
  1     from random import randint
  2
  3     breakpoint()
  4
  5     answer = randint(0, 1)
  6  -> n = input("Guess: 0 or 1? ")
  7
  8     if n == answer:
  9         print("Correct!")
 10     else:
 11         print(f"Incorrect. The answer was {answer}.")
(Pdb) n
Guess: 0 or 1? 
```

Conflict: want to see the value of "n" but it is both a variable and a command  

Solutions:

1. Put a ! character at the beginning of our line to tell PDB that our statement is a Python statement and not a PDB command

2. Run the `interact` command which would drop us into a regular Python REPL where we can run any commands we’d like as usual

Run the `interact` command to enter the standard python REPL and use any avaialble python command: 

```python
(Pdb) interact
*pdb interact start*
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__pdb_convenience_variables', '__spec__', 'answer', 'n', 'randint']
>>> answer
1
>>> n
'1'
>>>
```
use `dir()` to list all variables
list the values of `answer` and `n` to show their values

Reveals that `answer` is an integer, while `n` is a string and this causes the program to always return a "incorrect" answer. There is no data type control.

use `exit()` to close the `interact` command environment



### PDB Commands

Useful PDB commands:  

- n(ext): Run the next line of code
- s(tep): Step into the current line of code (step into a function call usually)
- r(eturn): Return from the current function
- c(ontinue): Exit PDB, continuing until the next breakpoint or the end of the program
- l(ist): List the surrounding code lines
- interact: Enter interactive mode, which starts a Python REPL session
- !: Prefix a line with ! to force PDB to run it as Python code
- q(uit): Exit debugger
- pp <variable>: Pretty-print a variable  

#### N(ext) vs. S(tep)  

“next” will execute the next line of code
“step” will step one level down into the next line of code.  

If your code calls a function:  

- “next” : you will find yourself on the line after the function fully runs  
- “step” :  you’ll find yourself inside the function as it runs

### Debugging with pytest

#### Debug on failure

`:> pytest --pdb <file-to-test.py>`

#### Debug from Start

`:> pytest --pdb-trace <file-to-test.py>`

#### Useful Flags

- --lf - Run only last failed tests
- --ff - Run failed tests first
- -x - Stop on first failure
- --tb=short - Shorter traceback format
- --tb=line - One line per failure

#### Debugging a Failed Test

`Inspire.py` has a common CSV parsing bug

`Inspire_test.py` test and reveals the failed  test

Run the test `:> pytest --pdb Inspire_test.py` automatically enters the debugging envrionment upon failure of a test.  

```python
filename = 'C:\\Users\\danie\\AppData\\Local\\Temp\\pytest-of-danie\\pytest-0\\test_quote_with_comma0\\quotes.csv'

    def get_all_quotes(filename):
        """Read quotes from a CSV file and return as named tuples."""
        Quote = namedtuple('Quote', 'author text')
        quotes = []
        with open(filename) as quotes_file:
            for line in quotes_file:
>               author, quote = line.split(',')
                ^^^^^^^^^^^^^
E               ValueError: too many values to unpack (expected 2)

inspire.py:12: ValueError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
> d:\github\mypython\inspire.py(12)get_all_quotes()
-> author, quote = line.split(',')
(Pdb)
```
Use `l` to show where this first error occurred. The first run of the test indicated line twelve. The the `l` command shows the program has stopped at line 12.  
The error is within a loop. use `p line` to print the current value of "line" at the current iteration of the loop.  
Use `line.split(',')` to show what happened with teh command from the code is executed. Notice the result of the command is four elements in the list instead of the expected two. Commas within the quotes are being interpreted as delimters, not part of the list element. CSV parsing is not correct. Fixing this is not the point in this training.

```python
(Pdb) l
  7         """Read quotes from a CSV file and return as named tuples."""
  8         Quote = namedtuple('Quote', 'author text')
  9         quotes = []
 10         with open(filename) as quotes_file:
 11             for line in quotes_file:
 12  ->             author, quote = line.split(',')
 13                 quotes.append(Quote(author, quote))
 14         return quotes
 15
 16
 17     def main(filename):
(Pdb) p line
'Dr. Seuss,"One fish, two fish, red fish, blue fish"\n'
(Pdb) line.split(',')
['Dr. Seuss', '"One fish', ' two fish', ' red fish', ' blue fish"\n']
(Pdb)
```


### Inspection Python Objects

objects.py


### Debugging Tips

use `breakpoint()` to start python debugger   

- n(ext): Run the next line of code
- s(tep): Step into the current line of code (step into a function call usually)
- r(eturn): Return from the current function
- c(ontinue): Exit PDB, continuing until the next breakpoint or the end of the program
- l(ist): List the surrounding code lines
- interact: Enter interactive mode, which starts a Python REPL session
- !: Prefix a line with ! to force PDB to run it as Python code
- q(uit): Exit debugger
- pp <variable>: Pretty-print a variable  

### Debugging Exercises

#### Guessing Game

guessingGame.py  

Askss user to guess either `0` or `1` and returns whether they have guessed correctly.  
Current problem: Always answers as incorrect, even if the user's guess is correct  

1. Add `breakpoint()` before  the `if` statement since everthing before that executes.
2. Run the program and guess `0`. The program fails and enters python debugger automatically
3. use `p n` to print the user's guess
4. use `p answer` to reveal the random integer selected by the program.
5. Notice the user's input is stored as a string while `answer` is stored as an integer. This is a type mismatch
6. Verify with `p type(n)` and `p type(answer)` to shows the types of objects.
7. Verify the failure with `p n == answer`
8. Fix the code by changing the input statement to `n = int(input("Guess:0 or 1? "))`

#### Calulation Error

average.py

The first calculation works, but the second fails.

1. Place `breakpoint()` as the first line of `def calculate_average()`
2. Run the program and arrive at the breakpoint, before entering the function.
3. Use `c` to continue. `avg` executes correctly and the breakpoint is reached again, before the calculation of `avg2`.
4. Use `p numbers` to see what the function is using for the values passed from avg2. The result is an empty list, because `empty_scores` is empty.
5. Verify with `p len(numbers)`.  

Fix the problems by adding the appropriate methods to handle empty lists gracefully.

#### Transaction Reconciliation

reconcile.py should reconcile to csv files containing financial transactions. It should identify when a transaction amount changed, but it does not.
reconcile_test.py contains the failing test.

1. Run `pytest --pdb reconcile_test.py`. `reconcile_test.py` fails at line 31 due to an error in `reconcile.py` at line 22.

```python
(.venv) PS D:\GitHub\MyPython> pytest --pdb reconcile_test.py
=================================================================================================== test session starts ====================================================================================================
platform win32 -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
collected 1 item                                                                                                                                                                                                            

reconcile_test.py F
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

    def test_reconcile_amount_change():
        """Test case where transaction amounts changed: 50.00 → 49.99"""
        # Create temporary CSV files
        file1_data = [
            ["Date", "Dept", "Amount", "Payee"],
            ["2000-12-05", "Engineering", "50.00", "Zapier"]
        ]
        file2_data = [
            ["Date", "Dept", "Amount", "Payee"],
            ["2000-12-05", "Engineering", "49.99", "Zapier"]
        ]

        # Write to temporary files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f1:
            writer = csv.writer(f1)
            writer.writerows(file1_data)
            file1_path = f1.name

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f2:
            writer = csv.writer(f2)
            writer.writerows(file2_data)
            file2_path = f2.name

        try:
>           removed, added, differences = reconcile_transactions(file1_path, file2_path)
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

reconcile_test.py:31:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

file1 = 'C:\\Users\\danie\\AppData\\Local\\Temp\\tmpg3f7usc2.csv', file2 = 'C:\\Users\\danie\\AppData\\Local\\Temp\\tmp5y2g3vu1.csv'

    def reconcile_transactions(file1, file2):
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            reader1 = csv.reader(f1)
            reader2 = csv.reader(f2)
            header1 = next(reader1)
            header2 = next(reader2)

            if header1 != header2:
                raise ValueError("Headers do not match.")

            transactions1 = set(tuple(row) for row in reader1)
            transactions2 = set(tuple(row) for row in reader2)

            removed = transactions1 - transactions2
            added = transactions2 - transactions1

            differences = []
            for t1 in transactions1:
                for t2 in transactions2:
>                   if t1[:3] == t2[:3] and t1[3] != t2[3]:
                                            ^^^^^
E                   IndexError: tuple index out of range # <<-- THE ERR

reconcile.py:22: IndexError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
> d:\github\mypython\reconcile.py(22)reconcile_transactions()
-> if t1[:3] == t2[:3] and t1[3] != t2[3]:
(Pdb)
```

2. Add `breakpoint()` just above the point where ptest identifies the problem. In this case, just below the "if" statement.  
3. run `pytest --pdb reconcile_test.py` again. The test stops at the point where comparisons are made.
4. Pay attention to the evaluation expression. What are the values located at t1[3] and t2[3]. Are they values the function actually intends to compare?

## Writing Tests with LLMs

### Making Code Testable with LLM

Consider using an LLM to refactor code to make it more testable.  

In this example, 
  ```python
  import csv
  from pathlib import Path
  import sys
  
  [csv_filename] = sys.argv[1:]
  
  
  total = 0
  with open(csv_filename) as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
          if row["Category"] == "Air Travel":
              cost = float(row["Cost"].removeprefix("$"))
              total += cost
  print(f"Total air travel expenses: ${total:.02f}")
  ```


For this, I used Antropic Claude Sonnet 4.

The prompt:  "I want to write automated tests for the following code. Evaluate the code. Is the code testable? If the code is not testable, refactor the code making automated tests more achievable. The code:"
"
The response:  

```md
Code Evaluation
The current code has several testability issues:

Hard dependency on sys.argv - Makes it impossible to test without manipulating command-line arguments
Direct file I/O operations - Requires creating actual files for testing
Mixed responsibilities - Argument parsing, file processing, and output are all in one block
No separation of concerns - Everything happens in the global scope
Direct print statements - Output can't be captured or verified easily
```  

The refactored code:

```python
import csv
from pathlib import Path
import sys
from typing import TextIO, Dict, Any

def parse_cost(cost_str: str) -> float:
    """Parse a cost string (e.g., '$123.45') into a float."""
    return float(cost_str.removeprefix("$"))

def calculate_air_travel_expenses(csv_reader) -> float:
    """Calculate total air travel expenses from a CSV reader."""
    total = 0.0
    for row in csv_reader:
        if row.get("Category") == "Air Travel":
            cost = parse_cost(row["Cost"])
            total += cost
    return total

def process_expense_file(file_handle: TextIO) -> float:
    """Process an expense CSV file and return total air travel expenses."""
    reader = csv.DictReader(file_handle)
    return calculate_air_travel_expenses(reader)

def format_expense_result(total: float) -> str:
    """Format the expense total as a currency string."""
    return f"Total air travel expenses: ${total:.2f}"

def main(csv_filename: str) -> str:
    """Main function that processes a CSV file and returns formatted result."""
    with open(csv_filename) as csv_file:
        total = process_expense_file(csv_file)
        return format_expense_result(total)

def cli_main():
    """Command-line interface entry point."""
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_filename>", file=sys.stderr)
        sys.exit(1)
    
    csv_filename = sys.argv[1]
    try:
        result = main(csv_filename)
        print(result)
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":  

    cli_main()  
```  

Beauty is in the eye of the beholder.  This output seeks testablity, as requested, but results in a good deal of ineffencies.


### Generating Tests with LLMs

The prompt 

```md
Please write tests for this code, using pytest.
Put docstrings and comments in the tests to make them clear.
Make sure the tests are thorough.
The name of this file is `total_air_travel.py`.
```

The results...

```python
"""
Comprehensive test suite for the CSV expense calculator.

This module tests the expense calculation functionality including:
- Core calculation logic with various data scenarios
- File handling and error cases
- Edge cases and boundary conditions
- Integration testing with actual file operations

Tests use pytest fixtures and parameterized tests for thorough coverage.
"""

import pytest
import csv
import sys
from io import StringIO
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path
import tempfile
import os

# Assuming the code is in expense_calculator.py
from expense_calculator import calculate_expenses, main


class TestCalculateExpenses:
    """Test suite for the calculate_expenses function."""
    
    def test_calculate_expenses_with_air_travel_only(self):
        """
        Test calculation when CSV contains only air travel expenses.
        
        This verifies that the function correctly identifies and sums
        all air travel expenses when no other categories are present.
        """
        csv_content = """Category,Cost
Air Travel,$250.00
Air Travel,$300.50
Air Travel,$100.25"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Expected: 250.00 + 300.50 + 100.25 = 650.75
        assert total == 650.75

    def test_calculate_expenses_mixed_categories(self):
        """
        Test calculation with mixed expense categories.
        
        Ensures that only air travel expenses are included in the total
        while other categories are properly ignored.
        """
        csv_content = """Category,Cost
Air Travel,$250.00
Hotel,$150.00
Air Travel,$300.50
Food,$75.25
Car Rental,$200.00
Air Travel,$50.00"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Expected: 250.00 + 300.50 + 50.00 = 600.50
        # Hotel, Food, and Car Rental should be ignored
        assert total == 600.50

    def test_calculate_expenses_no_air_travel(self):
        """
        Test calculation when no air travel expenses exist.
        
        Verifies that the function returns 0 when the CSV contains
        only non-air-travel expenses.
        """
        csv_content = """Category,Cost
Hotel,$150.00
Food,$75.25
Car Rental,$200.00
Taxi,$25.50"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Expected: 0.00 (no air travel expenses)
        assert total == 0.0

    def test_calculate_expenses_empty_file(self):
        """
        Test calculation with empty CSV file (headers only).
        
        Ensures graceful handling when CSV has headers but no data rows.
        """
        csv_content = """Category,Cost"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        assert total == 0.0

    def test_calculate_expenses_costs_without_dollar_sign(self):
        """
        Test calculation with costs that don't have dollar sign prefix.
        
        Verifies that the function handles both "$250.00" and "250.00" formats.
        """
        csv_content = """Category,Cost
Air Travel,250.00
Air Travel,$300.50
Air Travel,100.25"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Expected: 250.00 + 300.50 + 100.25 = 650.75
        assert total == 650.75

    def test_calculate_expenses_integer_costs(self):
        """
        Test calculation with integer cost values.
        
        Ensures that costs without decimal places are handled correctly.
        """
        csv_content = """Category,Cost
Air Travel,$250
Air Travel,$300
Air Travel,$100"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Expected: 250 + 300 + 100 = 650
        assert total == 650.0

    def test_calculate_expenses_decimal_precision(self):
        """
        Test calculation with various decimal precision values.
        
        Verifies accurate floating-point arithmetic with different
        decimal place counts.
        """
        csv_content = """Category,Cost
Air Travel,$250.1
Air Travel,$300.99
Air Travel,$100.001"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Expected: 250.1 + 300.99 + 100.001 = 651.091
        assert abs(total - 651.091) < 0.001  # Account for floating-point precision

    def test_calculate_expenses_case_sensitive_category(self):
        """
        Test that category matching is case-sensitive.
        
        Ensures that "air travel", "AIR TRAVEL", etc. are not matched
        when the expected category is "Air Travel".
        """
        csv_content = """Category,Cost
air travel,$250.00
AIR TRAVEL,$300.50
Air travel,$100.25
Air Travel,$50.00"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Only "Air Travel" (exact case) should be counted
        assert total == 50.0

    @pytest.mark.parametrize("cost_value,expected", [
        ("$0.00", 0.0),
        ("$0.01", 0.01),
        ("$999999.99", 999999.99),
        ("0.00", 0.0),
        ("1.23", 1.23),
    ])
    def test_calculate_expenses_edge_cost_values(self, cost_value, expected):
        """
        Test calculation with edge case cost values.
        
        Parameterized test for various cost formats and edge values
        including zero costs and very large amounts.
        """
        csv_content = f"""Category,Cost
Air Travel,{cost_value}"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        assert abs(total - expected) < 0.001

    def test_calculate_expenses_missing_category_column(self):
        """
        Test behavior when Category column is missing.
        
        Should raise a KeyError when trying to access the Category column.
        """
        csv_content = """Type,Cost
Air Travel,$250.00"""
        
        file_handle = StringIO(csv_content)
        
        with pytest.raises(KeyError):
            calculate_expenses(file_handle)

    def test_calculate_expenses_missing_cost_column(self):
        """
        Test behavior when Cost column is missing.
        
        Should raise a KeyError when trying to access the Cost column.
        """
        csv_content = """Category,Amount
Air Travel,$250.00"""
        
        file_handle = StringIO(csv_content)
        
        with pytest.raises(KeyError):
            calculate_expenses(file_handle)

    def test_calculate_expenses_invalid_cost_format(self):
        """
        Test behavior with invalid cost values.
        
        Should raise ValueError when cost cannot be converted to float.
        """
        csv_content = """Category,Cost
Air Travel,invalid_cost"""
        
        file_handle = StringIO(csv_content)
        
        with pytest.raises(ValueError):
            calculate_expenses(file_handle)

    def test_calculate_expenses_empty_cost_field(self):
        """
        Test behavior with empty cost field.
        
        Should raise ValueError when trying to convert empty string to float.
        """
        csv_content = """Category,Cost
Air Travel,"""
        
        file_handle = StringIO(csv_content)
        
        with pytest.raises(ValueError):
            calculate_expenses(file_handle)

    def test_calculate_expenses_extra_columns(self):
        """
        Test that extra CSV columns are ignored.
        
        Ensures the function works correctly even when additional
        columns are present in the CSV.
        """
        csv_content = """Category,Cost,Date,Description,Department
Air Travel,$250.00,2023-01-01,Flight to NYC,Sales
Hotel,$150.00,2023-01-01,Hotel stay,Sales
Air Travel,$300.50,2023-01-02,Return flight,Sales"""
        
        file_handle = StringIO(csv_content)
        total = calculate_expenses(file_handle)
        
        # Should still calculate correctly despite extra columns
        assert total == 550.50


class TestMainFunction:
    """Test suite for the main function and CLI behavior."""

    def test_main_insufficient_arguments(self, capsys):
        """
        Test main function behavior with no command line arguments.
        
        Should print usage message to stderr and exit with code 1.
        """
        with patch('sys.argv', ['script.py']):
            with pytest.raises(SystemExit) as exc_info:
                main()
            
            # Check exit code
            assert exc_info.value.code == 1
            
            # Check error message
            captured = capsys.readouterr()
            assert "Usage: python script.py <csv_filename>" in captured.err

    def test_main_too_many_arguments(self, capsys):
        """
        Test main function behavior with too many command line arguments.
        
        Should print usage message to stderr and exit with code 1.
        """
        with patch('sys.argv', ['script.py', 'file1.csv', 'file2.csv']):
            with pytest.raises(SystemExit) as exc_info:
                main()
            
            assert exc_info.value.code == 1
            captured = capsys.readouterr()
            assert "Usage: python script.py <csv_filename>" in captured.err

    def test_main_file_not_found(self, capsys):
        """
        Test main function behavior when specified file doesn't exist.
        
        Should print file not found error and exit with code 1.
        """
        with patch('sys.argv', ['script.py', 'nonexistent.csv']):
            with pytest.raises(SystemExit) as exc_info:
                main()
            
            assert exc_info.value.code == 1
            captured = capsys.readouterr()
            assert "Error: File 'nonexistent.csv' not found." in captured.err

    @patch('builtins.open', new_callable=mock_open, read_data="""Category,Cost
Air Travel,$250.00
Hotel,$150.00
Air Travel,$300.50""")
    def test_main_successful_execution(self, mock_file, capsys):
        """
        Test main function with successful file processing.
        
        Should process file correctly and print formatted result to stdout.
        """
        with patch('sys.argv', ['script.py', 'test.csv']):
            main()
        
        # Verify file was opened correctly
        mock_file.assert_called_once_with('test.csv', 'r', encoding='utf-8', newline='')
        
        # Check output
        captured = capsys.readouterr()
        assert "Total air travel expenses: $550.50" in captured.out

    @patch('builtins.open')
    def test_main_csv_processing_error(self, mock_open_func, capsys):
        """
        Test main function behavior when CSV processing fails.
        
        Should catch ValueError/KeyError and print appropriate error message.
        """
        # Mock file that raises ValueError when processed
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_open_func.return_value = mock_file
        
        # Mock csv.DictReader to raise ValueError
        with patch('csv.DictReader') as mock_reader:
            mock_reader.side_effect = ValueError("Invalid CSV format")
            
            with patch('sys.argv', ['script.py', 'invalid.csv']):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                
                assert exc_info.value.code == 1
                captured = capsys.readouterr()
                assert "Error processing CSV data:" in captured.err


class TestIntegrationWithRealFiles:
    """Integration tests using actual temporary files."""

    def test_integration_with_temporary_file(self, tmp_path):
        """
        Integration test using a real
```


### Iteration

When tests fail, show the error to the LLM  


### Verify

LLM outputs are non-determinitic, meaning the same inputs will not result in the same outputs. There are as many wrong answers as there are right ones.  

Always review generated tests:

Do they actually test the intended behavior?
Are edge cases covered?
Are error conditions handled?
Do the tests make sense?

### LLM Testing Workflow

One possible workflow:  

Analyze code for testability  
Generate initial tests using an LLM  
Iterative refinement, optionally with LLM help  
Verify and understand: LLM output should not be blindly trusted  

Another possible workflow:  

Generate initial tests based on documentation / examples  
Iterative refinement, optionally with LLM help  
Verify and understand: LLM output should not be blindly trusted  

General Advice:  

Start with simple examples  
Build complexity gradually  
Always verify generated code  
Use the LLM’s explanations to learn  
Restart LLM conversations if they get too long  

### LLM Exercises