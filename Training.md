# Modern Python Testing

<!-- TOC -->

- [Modern Python Testing](#modern-python-testing)
    - [INTRODUCTION TO MODERN TESTING](#introduction-to-modern-testing)
        - [Testing Fundamentals](#testing-fundamentals)
        - [Creating a virtual python environment](#creating-a-virtual-python-environment)
        - [Activate the virtual environment](#activate-the-virtual-environment)
        - [Deactivate a VENV](#deactivate-a-venv)
        - [Delete a VENV](#delete-a-venv)
        - [Install pytest](#install-pytest)
        - [Getting Started with pytest](#getting-started-with-pytest)
            - [Test Discovery](#test-discovery)
            - [Running all test](#running-all-test)
            - [Verbose Output](#verbose-output)
        - [Teseting Exercises](#teseting-exercises)
    - [DEBUGGING](#debugging)
        - [The Python Debugger](#the-python-debugger)
        - [A Broken Program](#a-broken-program)
        - [Breakpoint](#breakpoint)
        - [PDB Commands](#pdb-commands)
            - [Next vs. Step](#next-vs-step)
        - [Debugging with pytest](#debugging-with-pytest)
            - [Debug on failure](#debug-on-failure)
            - [Debug from Start](#debug-from-start)
            - [Useful Flags](#useful-flags)
            - [Debugging a Failed Test](#debugging-a-failed-test)
        - [Inspection Python Objects](#inspection-python-objects)
        - [Debugging Tips](#debugging-tips)
        - [Debugging Exercises](#debugging-exercises)
            - [Guessing Game](#guessing-game)
            - [Calulation Error](#calulation-error)
            - [Transaction Reconciliation](#transaction-reconciliation)
    - [WRITING TESTS WITH LLMs](#writing-tests-with-llms)
        - [Making Code Testable with LLM](#making-code-testable-with-llm)
        - [Generating Tests with LLMs](#generating-tests-with-llms)
        - [Iteration](#iteration)
        - [Verify](#verify)
        - [LLM Testing Workflow](#llm-testing-workflow)
        - [LLM Exercises](#llm-exercises)
            - [Picking The LLM](#picking-the-llm)
            - [percent_to_grade](#percent_to_grade)
            - [phonetic](#phonetic)
            - [rock](#rock)
            - [vote_tally](#vote_tally)
    - [Test Coverage](#test-coverage)
        - [Measuring Coverge with pytest](#measuring-coverge-with-pytest)
        - [Basic Test](#basic-test)
        - [HTML Coverage Report](#html-coverage-report)
        - [Missing Lines Report](#missing-lines-report)
            - [Default Line Coverage](#default-line-coverage)
            - [Branch Coverage](#branch-coverage)
        - [Coverage in the LLM Era](#coverage-in-the-llm-era)
        - [Coverage Exercises](#coverage-exercises)
            - [dollars coverage](#dollars-coverage)
            - [percent_to_grade coverage](#percent_to_grade-coverage)
            - [phonetic coverage](#phonetic-coverage)
            - [rock coverage](#rock-coverage)
            - [vote_tally coverage](#vote_tally-coverage)
    - [OUTPUT AND ASSERTIONS](#output-and-assertions)
        - [TESTING EXCEPTIONS](#testing-exceptions)
            - [Basic Exception Tesing](#basic-exception-tesing)
        - [CAPTURING STANDARD OUTPUT](#capturing-standard-output)
            - [Method 1: Monkey Patch Print Weak](#method-1-monkey-patch-print-weak)
            - [Method 2: contextlib.redirect_stdout better](#method-2-contextlibredirect_stdout-better)
            - [Method 3: pytest’s capsys fixture best](#method-3-pytests-capsys-fixture-best)
        - [Advanced Assertion Patterns](#advanced-assertion-patterns)
            - [Testing Partial Output](#testing-partial-output)
            - [Testing with Regular Expressions](#testing-with-regular-expressions)
            - [Testing Multi-line output](#testing-multi-line-output)
        - [OUTPUT AND EXCEPTION TESTING EXERCISES](#output-and-exception-testing-exercises)
            - [howdy](#howdy)
            - [flip_dict](#flip_dict)
            - [altprint](#altprint)

<!-- /TOC -->

## INTRODUCTION TO MODERN TESTING

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

## DEBUGGING

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

## WRITING TESTS WITH LLMs

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

#### Picking The LLM

Anthropic Claude 4 Sonnet

#### percent_to_grade

prompt: The following python is contained in a file called percent_to_grade.py. The code needs tested. Write and annotate tests using pytest that will identify any errors in the code and assist the developer in remediating those errors. The orginal clode is: 

Result 1 file: percent_to_grade_llm.py

The LLM provides the following additional information:  

Key Issues These Tests Will Reveal:
Redundant A+ Logic : The special case for percent > 99 is redundant since 100 % 10 = 0, and scores like 97, 98, 99 already get A+ through the general rule.
Parameter Naming : The parameter round shadows Python's built-in round() function.
Inconsistent Return Pattern : F grades return early, while other grades go through the suffix logic, making the code structure inconsistent.
No Input Validation : The function doesn't validate input types or ranges.
Edge Case Handling : The function works with negative numbers and numbers > 100, but this behavior might not be intended.
Floating Point Precision : The function doesn't account for potential floating-point precision issues.

**Run the test**

```md
(.venv) PS D:\GitHub\MyPython> pytest --pdb percent_to_grade_llm.py
================================================================================ test session starts =================================================================================== 
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
collected 26 items                                                                                                                                                                                                       

percent_to_grade_llm.py ..........................                                                                                                                                 [100%] 

================================================================================= 26 passed in 0.06s ================================================================================== 
(.venv) PS D:\GitHub\MyPython>
```

#### phonetic

The code is in phonetic.py

The prompt: The following python is contained in a file called phonetic.py. The code needs tested. Write and annotate tests using pytest that will identify any errors in the code and assist the developer in remediating those errors. The orginal clode is: 

The resultant test is contained in file phonetic_llm.py

the LLM provide additionla insights: 

```md
Key Issues These Tests Will Reveal:
Spacing Issues : The most significant bug is that join(' ') adds spaces between ALL characters, including existing spaces, creating double/triple spaces in the output.
Non-alphabetic Character Handling : The function passes through digits, punctuation, and special characters unchanged, which may not be appropriate for phonetic spelling.
Input Validation : No validation for input types - will crash with None, integers, or other non-string types.
Unicode Handling : Accented characters and non-ASCII letters are passed through unchanged rather than being converted to their base letters.
Whitespace Preservation : Tabs, newlines, and other whitespace characters are preserved, which may not be desired.
Real-world Usage Issues : The spacing problem makes the output difficult to read for practical use cases.
Suggested Fixes:
Fix spacing : Filter out spaces before conversion or handle them specially
Add input validation : Check for string input and handle edge cases
Consider digits : Decide whether to spell out numbers or handle them specially
Handle Unicode : Consider normalizing accented characters to base letters
```

**Run the test**

There appaer to be errors:

```md
=================================
(.venv) PS D:\GitHub\MyPython> pytest --pdb phonetic_llm.py        
===================================== test session starts ======================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
collected 34 items                                                                              

phonetic_llm.py ...................F
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

self = <phonetic_llm.TestPhoneticInputValidation object at 0x0000014BCF3A96D0>

    def test_none_input(self):
        """Test function behavior with None input

        This will likely raise an AttributeError since None has no upper() method.
        """
        with pytest.raises(AttributeError):
>           phonetic(None)

phonetic_llm.py:155:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

text = None

    def phonetic(text):
        """Convert text to NATO phonetic alphabet."""
        nato = {
            'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
            'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
            'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
            'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
            'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
            'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
            'Y': 'Yankee', 'Z': 'Zulu'
        }

>       return ' '.join(nato.get(char.upper(), char) for char in text)
                                                                 ^^^^
E       TypeError: 'NoneType' object is not iterable

phonetic.py:13: TypeError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>
> d:\github\mypython\phonetic.py(13)phonetic()
-> return ' '.join(nato.get(char.upper(), char) for char in text)
(Pdb)
```
The test fails when the value of the input variable "text" is set to a value of "None". The indicates the developer should include an error handling technique in the event the user doesn't submit a value for the input variable.

Another failure happens when inputting "123". Integers are not iterable, so the test fails.

Let's follow this with a next prompt: Evaluate the original code using the test code. Is there a value which can be assigned to “text” which causes the test to fail?  

The LLM finds additional potential issues using the test:

The next prompt: Generate a summary table that includes the failing test case, the expected behavior, and the actual result. No explanation is necessary.  

The Result:  

| Test Case | Input | Expected Result | Actual Result | Failure Type |
|-----------|-------|----------------|---------------|--------------|
| `phonetic("A B")` | `"A B"` | `"Alpha Bravo"` | `"Alpha   Bravo"` | Spacing Bug |
| `phonetic("A  B")` | `"A  B"` | `"Alpha  Bravo"` | `"Alpha     Bravo"` | Spacing Bug |
| `phonetic("HI THERE")` | `"HI THERE"` | `"Hotel India Tango Hotel Echo Romeo Echo"` | `"Hotel India   Tango Hotel Echo Romeo Echo"` | Spacing Bug |
| `phonetic("S O S")` | `"S O S"` | `"Sierra Oscar Sierra"` | `"Sierra   Oscar   Sierra"` | Spacing Bug |
| `phonetic("   ")` | `"   "` | `"   "` | `"     "` | Spacing Bug |
| `phonetic(None)` | `None` | Should handle gracefully | `AttributeError: 'NoneType' object has no attribute 'upper'` | Type Error |
| `phonetic(123)` | `123` | Should handle gracefully | `TypeError: 'int' object is not iterable` | Type Error |
| `phonetic(['A', 'B'])` | `['A', 'B']` | Should handle gracefully | `AttributeError: 'list' object has no attribute 'upper'` | Type Error |
| `phonetic(True)` | `True` | Should handle gracefully | `AttributeError: 'bool' object has no attribute 'upper'` | Type Error |
| `phonetic("café")` | `"café"` | `"Charlie Alpha Foxtrot Echo"` | `"Charlie Alpha Foxtrot é"` | Unicode Handling |
| `phonetic("naïve")` | `"naïve"` | `"November Alpha India Victor Echo"` | `"November Alpha ï Victor Echo"` | Unicode Handling |

#### rock

Created an additional file: rock2.py 

The following python is contained in a file called rock2.py. The code needs tested. Write and annotate tests using pytest that will identify any errors in the code and assist the developer in remediating those errors. The orginal clode is: 

The results are located in the rock2_llm.py

The model provided additional results in the table, following the request from the previous exercise, though I did have request the model to reformat the table into an object which can be copied into a markdown document:  


Key Issues These Tests Will Reveal:

| Test Case | Issue Identified | Expected Behavior | Actual Result |
|-----------|------------------|-------------------|---------------|
| `test_main_exception_flow_bug()` | NameError in main() | Handle exception gracefully | `NameError: name 'result' is not defined` |
| `test_case_sensitivity()` | Case sensitivity | Accept "ROCK", "Rock" | `ValueError: Invalid input` |
| `test_whitespace_handling()` | No input trimming | Accept " rock " | `ValueError: Invalid input` |
| `@patch('rock2.rock') with exception` | Exception handling bug | Continue after exception | NameError when accessing undefined `result` |
| Main function output | Inconsistent formatting | Clean output | Extra empty lines from `print()` |

THe LLM identifes the most critical bug as the exception handling bug in main():  
Root Cause:  
The original code structure separates the exception handling from the result processing, but doesn't account for the case where an exception prevents result from being defined.  

```python
try:
    result = rock(args.player1, args.player2)
except ValueError as e:
    print(e)
# BUG: If exception occurs, 'result' is never defined
if result is None:  # NameError if exception was raised
    print("It's a tie")
```

After being prompted to "write and annotate a fix for the exception handling bug in main()" the LLM provides two potential fixes

```python
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("player1", choices=options)
    parser.add_argument("player2", choices=options)
    args = parser.parse_args()
    
    print("Player 1 played", args.player1)
    print("Player 2 played", args.player2)
    print()
    
    # FIX: Initialize result to None and restructure exception handling
    result = None  # Initialize result to prevent NameError
    
    try:
        result = rock(args.player1, args.player2)
    except ValueError as e:
        print(e)
        return  # FIX: Exit early after error instead of continuing
    
    # Now we can safely check result since it's either None (tie) or a tuple (win)
    if result is None:
        print("It's a tie")
    else:
        winner, action, loser = result
        print(winner.capitalize(), action, loser)
        print()
        if winner == args.player1:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
```

And a more "defensive" alternative  

```python
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("player1", choices=options)
    parser.add_argument("player2", choices=options)
    args = parser.parse_args()
    
    print("Player 1 played", args.player1)
    print("Player 2 played", args.player2)
    print()
    
    try:
        result = rock(args.player1, args.player2)
        
        # FIX: Move all result processing inside the try block
        if result is None:
            print("It's a tie")
        else:
            winner, action, loser = result
            print(winner.capitalize(), action, loser)
            print()
            if winner == args.player1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")
                
    except ValueError as e:
        # FIX: Handle error and exit cleanly
        print(f"Error: {e}")
        # Could also use sys.exit(1) for error exit code
```

The use of the word "defensive" by the model raises questions. I asked the model to 'Explain why the second potential fix is considered more “defensive”?`

The model provided six reasons the second option is more "defensive".

1. Single Point of Control: All success-path code is protected by the same exception handler. If ANY part of the result processing fails, it's caught.  

```python
# Option 2 (Defensive) - Everything in one try block
try:
    result = rock(args.player1, args.player2)
    # ALL result processing happens here
    if result is None:
        print("It's a tie")
    else:
        # ... handle win scenario
except ValueError as e:
    print(f"Error: {e}")

# Option 1 - Split control flow
try:
    result = rock(args.player1, args.player2)
except ValueError as e:
    print(e)
    return  # Early exit

# Separate processing outside try block
if result is None:
    # ...
```

2. Protection Against Future Errors : Catches not just the rock() function errors, but any errors in the entire processing chain.  

```python 
# What if this line throws an exception in the future?
winner, action, loser = result  # Could fail if result structure changes
print(winner.capitalize(), action, loser)  # Could fail if winner is None
```
3. Fail-Safe Principle : Defensive programming follows the principle: "If anything can go wrong, contain it" 

```python
# Option 2 protects against:
# - rock() function errors
# - Tuple unpacking errors
# - String method errors (.capitalize())
# - Print formatting errors
# - Logic errors in winner determination

# Option 1 only protects against:
# - rock() function errors 
```

4. Easier Error Handling Evolution

```python 
# Option 2 - Easy to enhance error handling
try:
    result = rock(args.player1, args.player2)
    if result is None:
        print("It's a tie")
    else:
        winner, action, loser = result
        print(winner.capitalize(), action, loser)
        # Future: Add logging, metrics, file output, etc.
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:  # Easy to add catch-all
    print(f"Unexpected error: {e}")
```

5. Atomic Operation Concept : The defensive approach treats the entire "get result and process it" as one atomic operation - either it all succeeds, or it all fails safely.  

```python 
# Option 2: Atomic operation
try:
    # This entire block succeeds or fails as a unit
    result = rock(args.player1, args.player2)
    # Process result...
except:
    # Handle any failure in the entire operation
```
6. Reduces Cognitive Load

```python 
# Option 1: Developer must remember
# - Did the exception happen?
# - Is result defined?
# - What state are we in?

# Option 2: Simple mental model
# - Try to do the whole thing
# - If anything fails, handle it
``` 

The model also provides suggestions for instances when each option might be more effective: 

Trade-offs

| Aspect | Option 1 (Early Return) | Option 2 (Defensive) |
|--------|-------------------------|----------------------|
| **Clarity** | ✅ Clear error vs success paths | ❌ Mixed success/error handling |
| **Debugging** | ✅ Easy to trace execution | ❌ Harder to know where failure occurred |
| **Performance** | ✅ Exits immediately on error | ❌ More code in try block (minimal impact) |
| **Safety** | ❌ Only protects specific errors | ✅ Protects entire operation |
| **Maintainability** | ❌ Need to remember to handle new errors | ✅ Automatic protection for new code |

**When to Use Each**  

Use Option 1 (Early Return) when:

- You have well-defined, specific error conditions
- Performance is critical
- You want explicit control flow
- Errors are expected and recoverable

Use Option 2 (Defensive) when:

- You want maximum safety
- The codebase changes frequently
- Multiple developers work on the code
- Unexpected errors should be contained
- You prefer "fail-safe" over "fail-fast"

The defensive approach prioritizes safety and robustness over explicit control flow, making it more suitable for production code where unexpected failures should be gracefully contained.

#### vote_tally  

## Test Coverage

"Which parts of the code are never execute by tests?"

Reveals: 

- Dead code: Code that’s never executed
- Missing edge cases: Conditional branches that aren’t tested
- Error handling gaps: Exception paths without tests
- Integration blind spots: Code paths only hit in production

### Measuring Coverge with pytest

`:> pip install pytest-cov`

Run the coverage command on the email_validator_test.py

### Basic Test

Format: pytest --cov=[file to be tested] [file containing the tests]
`:> pytest --cov=emailvalidator email_validator_test.py`

this results in the creation of a file called ".coverage", which is a SQLite database that holds coverage-related data.

### HTML Coverage Report

`:> pytest --cov=email_validator --cov-report=html test_email_validator.py`  

Generates and  htmlcov/ directory with an interactive coverage report. 

### Missing Lines Report

Files:calculate_total.py; calculate_total_test.py

#### Default Line Coverage  

`pytest --cov=calcualte_total calculate_total_test.py`  

This indicates 100% of lines are tested

#### Branch Coverage

```md
============================================================================= 1 passed in 0.18s ============================================================================= 
(.venv) PS D:\GitHub\MyPython> pytest --cov=calculate_total --cov-branch calculate_total_test.py
============================================================================ test session starts ============================================================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
plugins: cov-7.0.0
collected 1 item                                                                                                                                                              

calculate_total_test.py .                                                                                                                                              [100%] 

============================================================================== tests coverage =============================================================================== 
______________________________________________________________ coverage: platform win32, python 3.13.8-final-0 ______________________________________________________________ 

Name                 Stmts   Miss Branch BrPart  Cover
------------------------------------------------------
calculate_total.py       5      0      2      1    86%
------------------------------------------------------
TOTAL                    5      0      2      1    86%
============================================================================= 1 passed in 0.11s ============================================================================= 
(.venv) PS D:\GitHub\MyPython>
```
In this case, there is an if-statement. The elements of an if statement are only tested if they are activated. The test, as written, only contains tests for one branch. So, less of the file is actually tested. Whereas, in the default test, only the lines executed are tested.  

the test file requires an additional test:  

```python
def test_no_tax():
    assert calculate_total([3.49], apply_tax=False) == 3.49
    assert calculate_total([3.49, 13.89], apply_tax=False) == 17.38 
```

This will produce 100% branch test
```md
(.venv) PS D:\GitHub\MyPython> pytest --cov=calculate_total --cov-branch calculate_total_test.py
============================================================================ test session starts ============================================================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
plugins: cov-7.0.0
collected 2 items                                                                                                                                                            

calculate_total_test.py ..                                                                                                                                             [100%]

============================================================================== tests coverage =============================================================================== 
______________________________________________________________ coverage: platform win32, python 3.13.8-final-0 ______________________________________________________________ 

Name                 Stmts   Miss Branch BrPart  Cover
------------------------------------------------------
calculate_total.py       5      0      2      0   100%
------------------------------------------------------
TOTAL                    5      0      2      0   100%
============================================================================= 2 passed in 0.08s ============================================================================= 
(.venv) PS D:\GitHub\MyPython> 
```

Observe: No tests have been written for testing custom `tax_rate` values. More tests are still to be written. 

### Coverage in the LLM Era

Traditional reasons limit tests to 80%-90% have disappeared with the apearance of LLMs:  

- Speed: LLMs can generate many tests in seconds
- Creativity: LLMs can often find edge cases humans might miss
- Maintenance: it’s easier to update generated tests than write from scratch

Note: 100% code coverage does not mean 100% feature coverage.  

Code coverage only says “this line of code was executed”  
Code coverage cannot measure whether useful assertions were made or whether all possible scenarios are adequately tested.  

Important Points:  

- Code coverage identifies unevaluated code  
- Code coverage does not determine whether code was tested well, just whether it was run  
- Use pytest-cov to measure and visualize coverage gaps  
- Enable branch coverage with --cov-branch to catch missing conditional paths  
- Line coverage shows which lines ran; branch coverage shows which paths were taken  
- HTML reports make it easy to see exactly which lines need tests  
- High coverage provides higher confidence when refactoring or updating code  
-

### Coverage Exercises

#### dollars coverage
 
Run basic test: `:> pytest --cov=dollars test_dollars.py`  

```md
(.venv) PS D:\GitHub\MyPython> pytest --cov=dollars dollars_test.py
============================================================================ test session starts ============================================================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
plugins: cov-7.0.0
collected 1 item                                                                                                                                                             

dollars_test.py .                                                                                                                                                      [100%] 

============================================================================== tests coverage =============================================================================== 
______________________________________________________________ coverage: platform win32, python 3.13.8-final-0 ______________________________________________________________ 

Name         Stmts   Miss  Cover
--------------------------------
dollars.py      10      5    50%
--------------------------------
TOTAL           10      5    50%
```


Show missing lines: `:> pytest --cov=dollars --cov-report=term-missing dolalrs_test.py` 

```md
(.venv) PS D:\GitHub\MyPython> pytest --cov=dollars --cov-report=term-missing dollars_test.py
============================================================================ test session starts ============================================================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
plugins: cov-7.0.0
collected 1 item                                                                                                                                                             

dollars_test.py .                                                                                                                                                      [100%]

============================================================================== tests coverage =============================================================================== 
______________________________________________________________ coverage: platform win32, python 3.13.8-final-0 ______________________________________________________________ 

Name         Stmts   Miss  Cover   Missing
------------------------------------------
dollars.py      10      5    50%   8-11, 14
------------------------------------------
TOTAL           10      5    50%
```

#### percent_to_grade coverage

run basic coverage: `:> pytest --cov=percent_to_grade --cov-report=term-missing percent_to_grade_test_llm.py`  

```md 
(.venv) PS D:\GitHub\MyPython> pytest --cov=percent_to_grade --cov-report=term-missing percent_to_grade_test_llm.py 
============================================================================ test session starts ============================================================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
plugins: cov-7.0.0
collected 26 items                                                                                                                                                           

percent_to_grade_test_llm.py ..........................                                                                                                                [100%]

============================================================================== tests coverage ===============================================================================
______________________________________________________________ coverage: platform win32, python 3.13.8-final-0 ______________________________________________________________

Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
percent_to_grade.py      26      0   100%
---------------------------------------------------
TOTAL                    26      0   100%
============================================================================ 26 passed in 0.11s =============================================================================
(.venv) PS D:\GitHub\MyPython> 
```

run produce HTML report:  `:> pytest --cov=percent_to_grade --cov-branch --cov-report=html percent_to_grade_test_llm.py`  

``md
(.venv) PS D:\GitHub\MyPython> pytest --cov=percent_to_grade --cov-branch --cov-report=html percent_to_grade_test_llm.py
============================================================================ test session starts ============================================================================
platform win32 -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\GitHub\MyPython
plugins: cov-7.0.0
collected 26 items                                                                                                                                                           

percent_to_grade_test_llm.py ..........................                                                                                                                [100%]

============================================================================== tests coverage ===============================================================================
______________________________________________________________ coverage: platform win32, python 3.13.8-final-0 ______________________________________________________________

Coverage HTML written to dir htmlcov
============================================================================ 26 passed in 0.17s =============================================================================
(.venv) PS D:\GitHub\MyPython> 
``

Questions:

- How many missing lines?
- which lines are missing?
- Which branches, if any, are partial?  

#### phonetic coverage

Run coverage:

Run basic coverage: `:> pytest --cov=phonetic --cov-branch --cov-report=html phonetic_test.py`

Run coverage against your tests: `pytest --cov --cov-branch --cov-report=html phonetic_test.py`

Failure to supply a specific module to --cov runs coverage against all files in the current directory.

Be sure to check the test_phonetic.py file. Do your tests have 100% coverage?

Feature coverage:  

Is your code coverage 100%?  

Is your feature coverage also 100%?  

#### rock coverage

Run coverage.  You can decide how to formulate the coverage command on your own for this one.

Questions:

What coverage is missing?

Are there any uncovered branches?

#### vote_tally coverage

Check your code coverage for the get_vote_tally function.  

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

#### altprint

Write tests for the altprint function.

Hint: Since this function writes to sys.stdout, you’ll need to use pytest’s capsys fixture to capture the output.

