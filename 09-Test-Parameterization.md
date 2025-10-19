# Test Parametrization

## What is Parametrization?

Parametrization allows you to run the same test with different inputs and expected outputs.  
Instead of writing multiple similar tests, you can write one test and provide multiple sets of data to test against.  
This is especially useful when:

- Testing the same function with various inputs
- Testing edge cases and boundary conditions
- Reducing code duplication in tests
- Making tests more maintainable

## Basic Parametrization

When testing, it’s very common to want to call a function with particular inputs and check for a known output.  
This can make for a lot of very repetitive code though.  

For example, let’s say we have a pairwise function in a pairwise.py file that takes an iterable and returns pairs of adjacent elements:

```python
def pairwise(iterable):
    """Return successive overlapping pairs from iterable."""
    result = []
    items = list(iterable)
    for i in range(len(items)):
        if i + 1 < len(items):
            result.append((items[i], items[i + 1]))
        else:
            result.append((items[i], None))
    return result
```

Without parametrization, we might write many similar tests test_pairwise.py:

```python
from pairwise import pairwise

class TestPairwise:
    """Tests for pairwise."""

    def test_list(self):
        assert pairwise([1, 2, 3]) == [(1, 2), (2, 3), (3, None)]

    def test_empty_list(self):
        assert pairwise([]) == []

    def test_string(self):
        assert pairwise("hey") == [("h", "e"), ("e", "y"), ("y", None)]
```

The pytest library comes with a parametrize decorator which allows us to execute the same test multiple times with different parameters.

We can parametrize our tests by using pytest.mark.parametrize like this:

```python
import pytest
from pairwise import pairwise

@pytest.mark.parametrize("iterable, expected", [
    ([1, 2, 3], [(1, 2), (2, 3), (3, None)]),
    ([], []),
    ("hey", [("h", "e"), ("e", "y"), ("y", None)]),
])
def test_pairwise(iterable, expected):
    assert pairwise(iterable) == expected
```

The first argument to parametrize is a string with parameter names (comma-separated), and the second is a list of tuples with the test data.

When we run the tests in verbose mode (with -v or --verbose) we’ll see the 3 tests:

```md
$ pytest test_pairwise.py -v
 ======================== test session starts =========================
 platform linux -- Python 3.12.7, pytest-8.4.2, pluggy-1.6.0
 rootdir: /home/trey
 plugins: mock-3.15.1
 collected 3 items

 test_pairwise2.py::test_pairwise[iterable0-expected0] PASSED    [ 33%]
 test_pairwise2.py::test_pairwise[iterable1-expected1] PASSED    [ 66%]
 test_pairwise2.py::test_pairwise[hey-expected2] PASSED          [100%]

 ========================== 3 passed in 0.01s ==========================
```

## Parametrizing with IDs

You can provide custom test IDs to make test output more readable.

Using pytest.param for more control:

```python
import pytest

from pairwise import pairwise

@pytest.mark.parametrize("iterable, expected", [
    pytest.param([1, 2, 3], [(1, 2), (2, 3), (3, None)], id="list"),
    pytest.param([], [], id="empty"),
    pytest.param("hey", [("h", "e"), ("e", "y"), ("y", None)], id="string"),
])
def test_pairwise_with_ids(iterable, expected):
    assert pairwise(iterable) == expected
```

You can also use a callable for ids that returns the ID for given items:

```python
def repr_ids(value):
    return repr(value)

test_cases = [
    ([1, 2, 3], [(1, 2), (2, 3), (3, None)]),
    ([], []),
    ("hey", [("h", "e"), ("e", "y"), ("y", None)]),
]

@pytest.mark.parametrize("iterable, expected", test_cases, ids=repr_ids)
def test_pairwise_with_callable_ids(iterable, expected):
    assert pairwise(iterable) == expected
```

This will show each of the inputs in the test output, making it easier to identify which test case failed.

So when we run the tests again, we’ll see the names list, empty, and string:

```md
$ pytest test_pairwise.py -v
 ======================== test session starts =========================
 platform linux -- Python 3.12.7, pytest-8.4.2, pluggy-1.6.0
 rootdir: /home/trey
 plugins: mock-3.15.1
 collected 3 items

 test_pairwise3.py::test_pairwise_with_ids[list] PASSED          [ 33%]
 test_pairwise3.py::test_pairwise_with_ids[empty] PASSED         [ 66%]
 test_pairwise3.py::test_pairwise_with_ids[string] PASSED        [100%]

 ========================== 3 passed in 0.01s ==========================
```

## Multiple Parametrization

You can apply multiple parametrize decorators to create a cross-product of test cases.

See this version of test_calculate_total2.py:

```python
import pytest

from calculate_total import calculate_total

@pytest.mark.parametrize("apply_tax", [True, False])
@pytest.mark.parametrize("tax_rate", [0.05, 0.10, 0.15])
def test_calculate_total_cross_product(apply_tax, tax_rate):
    result = calculate_total([10.00, 5.50], apply_tax=apply_tax, tax_rate=tax_rate)
    expected = 15.50 * (1 + tax_rate if apply_tax else 1)
    assert result == round(expected, 2)
```

This creates 6 test cases (2 × 3) testing all combinations of tax application and tax rate values.

Although, multi-dimensional parametrization is rarely used and rarely useful.

In fact, the above test is a bad example of this because it would be better written as two separate tests (test_calculate_total3.py):

```python
import pytest

from calculate_total import calculate_total

@pytest.mark.parametrize("tax_rate, expected", [
    (0.05, 16.28),
    (0.10, 17.05),
    (0.15, 17.82),
])
def test_calculate_total_cross_product(tax_rate, expected):
    result = calculate_total([10.00, 5.50], tax_rate=tax_rate)
    assert result == expected

@pytest.mark.parametrize("tax_rate", [0.05, 0.10, 0.15])
def test_calculate_total_cross_product_without_tax(tax_rate):
    result = calculate_total([10.00, 5.50], tax_rate=tax_rate, apply_tax=False)
    assert result == 15.50
```

## Parametrize Exercises

These exercises will help you practice refactoring existing tests to use parametrization.

### dollars 

You previously wrote tests for the format_dollars function (dollars.py):

```python
def format_dollars(amount):
    """Format a number as US currency."""
    return f"${amount:.2f}"
You likely wrote separate test functions like:

def test_format_dollars_basic():
    assert format_dollars(80) == "$80.00"

def test_format_dollars_rounding():
    assert format_dollars(3.048) == "$3.05"

def test_format_dollars_small():
    assert format_dollars(0.05) == "$0.05"
```

Your task: Refactor these into a single parametrized test using @pytest.mark.parametrize in your test_dollars.py file.

### to_percent

You previously wrote tests for the to_percent function (to_percent.py):

```python

def to_percent(ratio):
    """Return a percentage string representing the given numeric ratio."""
    return f"{ratio:.1%}"
```

Refactor your existing tests into a parametrized test in your test_to_percent.py file.

### four

You previously wrote tests for the four.py program’s main() function (four.py):

```python
def main():
    number = int(sys.argv[1])

    while number != 4:
        word = number_to_word(number)
        letter_count = len(word)
        print(f"The word {word} has {letter_count} letters in it.")
        number = letter_count

    print("The word four has 4 letters in it.")
    print("Done.")
```

You likely tested different starting numbers separately, each with their own expected output.

Refactor your tests to use parametrization for different starting numbers in your test_four.py file.

### phonetic

You previously wrote tests for the phonetic function (phonetic.py):

```python
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

    return ' '.join(nato.get(char.upper(), char) for char in text)
```

Refactor your tests to use parametrization for different text inputs and their expected NATO phonetic outputs in your test_phonetic.py file.

Consider testing:

Single letters

Multiple letters

Mixed case

Non-letters

### percent_to_grade

You previously wrote tests for the percent_to_grade function (percent_to_grade.py):

```python
def percent_to_grade(percent, *, suffix=False, round=False):
    if round:
        percent = round_half_up(percent)
    if percent >= 90:
        letter = 'A'
    elif percent >= 80:
        letter = 'B'
    elif percent >= 70:
        letter = 'C'
    elif percent >= 60:
        letter = 'D'
    else:
        return 'F'
    if suffix:
        if letter == 'A' and percent > 99:
            letter += '+'
        elif letter != 'F':
            if percent % 10 >= 7:
                letter += '+'
            elif percent % 10 < 3:
                letter += '-'
    return letter
```

This function has multiple parameters and complex branching logic.

Refactor your tests to use parametrization in your test_percent_to_grade.py file.

Consider these approaches:

Simple parametrization for basic grade boundaries without suffix

Multiple parametrization with both suffix=True and suffix=False scenarios

pytest.param with custom IDs to make test names clear

Bonus: Use pytest.param to mark certain edge cases with descriptive IDs like "perfect_score" or "failing_grade".

### altprint

You previously wrote tests for the altprint function (altprint.py):

def altprint(text):
    """Print text in aLtErNaTiNg CaPiTaLiZaTiOn."""
    result = ""
    capitalize_next = False
    for char in text:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
            else:
                result += char.lower()
            capitalize_next = not capitalize_next
        else:
            result += char
    sys.stdout.write(result + "\n")
Your task: Refactor your tests to use parametrization for different text inputs and their expected alternating case outputs in your test_altprint.py file.

Remember: This function prints to stdout, so you’ll need capsys to capture the output.

Consider testing:

Simple text

Text with spaces

Text with numbers

Empty string