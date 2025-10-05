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


#### Transaction Reconciliation