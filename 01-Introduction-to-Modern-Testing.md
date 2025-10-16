# Modern Python Testing

https://modern-testing.pym.dev/  

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
    - [TEST COVERAGE](#test-coverage)
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
    - [CREATING FIXTURES](#creating-fixtures)
        - [What are Fixtures](#what-are-fixtures)
        - [Fixtures are Magical](#fixtures-are-magical)
        - [Naming Fixtures](#naming-fixtures)
        - [Fixture Depedencies](#fixture-depedencies)
        - [Fixtures That Do Stuff](#fixtures-that-do-stuff)
        - [Teardown Fixtures](#teardown-fixtures)
        - [Factory Fixtures](#factory-fixtures)
        - [conftest](#conftest)
        - [Fixture Exercises](#fixture-exercises)
            - [Dollars Main Function](#dollars-main-function)
            - [Exploriing LLM Fixtures](#exploriing-llm-fixtures)
            - [File Path Arguements](#file-path-arguements)
            - [Data Fixutrue Refactoring](#data-fixutrue-refactoring)
            - [Track Time Processing](#track-time-processing)
            - [Multi-File Factory Fixtures](#multi-file-factory-fixtures)

<!-- /TOC -->

## INTRODUCTION TO MODERN TESTING



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

