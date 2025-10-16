# Modern Python Testing

https://modern-testing.pym.dev/  

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

