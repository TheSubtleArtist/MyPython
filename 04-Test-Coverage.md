## TEST COVERAGE

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

