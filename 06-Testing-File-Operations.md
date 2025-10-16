# Testing File Operations

## Example Input Files

How do the tests work when they need input files?  

The total_air_travel program  reads from CSV files.  

The LLM-generated tests used pytest’s tmp_path fixture to create temporary files for testing:


```python
class TestIntegration:
    """Integration tests that test the entire workflow."""

    def test_end_to_end_workflow(self, tmp_path):
        """Test the complete workflow from CSV file to final output."""
        # Create a comprehensive test CSV file
        csv_content = """Category,Cost,Description,Date
Air Travel,$1200.00,International flight,2024-01-15
Hotels,$350.00,Business hotel,2024-01-15
Air Travel,$89.99,Domestic connection,2024-01-16
Food,$125.50,Client dinner,2024-01-16
Air Travel,$0.00,Cancelled flight refund,2024-01-17
Transport,$45.00,Airport taxi,2024-01-17
Air Travel,$299.75,Rescheduled flight,2024-01-18"""

        csv_file = tmp_path / "integration_test.csv"
        csv_file.write_text(csv_content)

        # Test the complete workflow
        total = get_air_travel_costs(str(csv_file))
        expected_total = 1200.00 + 89.99 + 0.00 + 299.75

        assert abs(total - expected_total) < 0.01
        assert total == 1589.74

    def test_large_dataset_performance(self, tmp_path):
        """Test performance with a larger dataset."""
        # Generate a larger CSV file programmatically
        csv_file = tmp_path / "large_dataset.csv"

        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Category', 'Cost', 'Description'])

            total_expected = 0
            for i in range(1000):
                if i % 3 == 0:  # Every third entry is air travel
                    cost = 100.00 + (i % 100)
                    writer.writerow(['Air Travel', f'${cost:.2f}', f'Flight {i}'])
                    total_expected += cost
                else:
                    cost = 50.00 + (i % 50)
                    writer.writerow(['Hotels', f'${cost:.2f}', f'Hotel {i}'])

        # Test that it can handle the larger dataset efficiently
        result = get_air_travel_costs(str(csv_file))

        # Verify the calculation is correct for the large dataset
        assert abs(result - total_expected) < 0.01
```

This is a common pattern for testing file operations: create temporary files with known content, run your function, then verify the results.

## The tmp_path Fixture

The tmp_path fixture creates a temporary directory that’s automatically cleaned up after each test. It returns a pathlib.Path object pointing to the temporary directory.

### File Writing Example

Let’s test a function that creates README files. Here’s the program (make_readme.py):

Now here’s how we test the make_readme function using contextlib.chdir to change to our temporary directory (test_make_readme.py):


### File Reading Example

Now let’s test a function that reads CSV data. Here’s the program (quotes.py):

Now here’s how we test the get_all_quotes function (test_quotes.py):

### Alternative: Python’s tempfile Module

Python’s standard library provides tempfile.NamedTemporaryFile and tempfile.TemporaryDirectory for creating temporary files and directories:

```python
import tempfile
from pathlib import Path

from quotes import get_all_quotes

def test_get_all_quotes_with_named_temporary_file():
    """Example using NamedTemporaryFile."""
    with tempfile.NamedTemporaryFile(mode="wt", suffix=".csv", delete_on_close=False) as f:
        csv_content = """Einstein,Imagination is more important than knowledge
Twain,The secret of getting ahead is getting started
Jobs,Innovation distinguishes between a leader and a follower"""
        f.write(csv_content)
        f.close()
        temp_file = f.name

        quotes = get_all_quotes(temp_file)
        assert len(quotes) == 3
        assert quotes[0].author == "Einstein"
        assert quotes[2].text == "Innovation distinguishes between a leader and a follower"

def test_get_all_quotes_with_temporary_directory():
    """Example using TemporaryDirectory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        quotes_file = Path(temp_dir, "quotes.csv")
        csv_content = """Einstein,Imagination is more important than knowledge
Twain,The secret of getting ahead is getting started
Jobs,Innovation distinguishes between a leader and a follower"""
        quotes_file.write_text(csv_content)

        quotes = get_all_quotes(quotes_file)
        assert len(quotes) == 3
        assert quotes[1].author == "Twain"
```

While Python’s tempfile module works fine, pytest’s tmp_path fixture has some advantages:

- Simpler: Just add tmp_path parameter to your test function
- Pathlib integration: Returns pathlib.Path objects (more modern)
- Automatic cleanup: No need for context managers or manual cleanup
- Debugging friendly: Temporary files are kept when tests fail (helpful for debugging)

For most testing scenarios, tmp_path is the recommended approach.

## File Testing Exercises


Exercises on testing functions that work with files.

### line_numbers

Here’s a program that prints file contents with line numbers (line_numbers.py):

Write tests for the print_with_line_numbers function in a file called test_line_numbers.py:

- Test with a simple text file containing multiple lines
- Test with an empty file
- Test with a file containing blank lines
Remember: You can use capsys to capture the printed output.

Hint: The function expects an open file object, so you’ll need to open the temporary file you create.

### Summing Timestamps
We have a Python script that sums up the total time in a CSV file. Given this CSV file (tracks.csv):

The program would output:

`$ python sum_timestamps.py tracks.csv`
`39:18`

Write automated tests for this code in a file called sum_timestamps_test.py.

### fix_newlines

Here’s a program that ensures files end with a newline character (fix_newlines.py):

This program modifies files in-place to ensure they end with a newline character. Many text editors and tools expect files to end with newlines, and this utility fixes files that don’t.

Write tests for the fix_newlines function in a file called fix_newlines_test.py. The function accepts either a pathlib.Path object or a filename (string) pointing to a file. Write tests for at least these 2 cases:

- Test with a file that already ends with a newline (should remain unchanged)
- Test with a file that doesn’t end with a newline (should add one)

Hint: The function works with binary files. You can create test files with tmp_path and check their content with read_bytes().

### fix_csv

Here’s a program that converts pipe-delimited CSV files to comma-delimited CSV files (fix_csv.py):

- Test converting a simple pipe-delimited file to comma-delimited
- Test handling data that contains commas (should be quoted in output)
- Test handling data that contains quotes (should be escaped properly)
- Test with an empty file
- Test with a file containing only headers

Example: If the input file contains Name|Age|City with a row John Smith|30|New York, NY, the output should properly quote the city field as "New York, NY".

