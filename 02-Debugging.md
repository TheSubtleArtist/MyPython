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

