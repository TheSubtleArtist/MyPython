# fix_csv_test.py
import pytest
import csv
from pathlib import Path
from unittest.mock import patch
from io import StringIO

# Import the functions we're testing
from fix_csv import convert_csv, main

class TestConvertCsv:
    """Tests for the convert_csv function."""
    
    def test_simple_pipe_delimited_to_comma(self, tmp_path):
        """Test converting a simple pipe-delimited file to comma-delimited."""
        # Create a simple pipe-delimited input file
        input_file = tmp_path / "input.csv"
        input_content = """Name|Age|City
John|25|New York
Alice|30|Los Angeles
Bob|35|Chicago"""
        input_file.write_text(input_content)
        
        # Define output file
        output_file = tmp_path / "output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify the output
        output_content = output_file.read_text()
        expected_content = """Name,Age,City
John,25,New York
Alice,30,Los Angeles
Bob,35,Chicago
"""
        assert output_content == expected_content
        
        # Also verify by reading with csv.reader
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Age', 'City'],
            ['John', '25', 'New York'],
            ['Alice', '30', 'Los Angeles'],
            ['Bob', '35', 'Chicago']
        ]
        assert rows == expected_rows
    
    def test_data_containing_commas(self, tmp_path):
        """Test handling data that contains commas (should be quoted in output)."""
        # Create pipe-delimited file with comma-containing data
        input_file = tmp_path / "input_with_commas.csv"
        input_content = """Name|Description|Price
Product A|A great product, highly rated|19.99
Product B|Simple, effective solution|29.99
Product C|Complex item, with many, many features|49.99"""
        input_file.write_text(input_content)
        
        output_file = tmp_path / "output_with_commas.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Read and verify the output using csv.reader to handle quoting properly
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Description', 'Price'],
            ['Product A', 'A great product, highly rated', '19.99'],
            ['Product B', 'Simple, effective solution', '29.99'],
            ['Product C', 'Complex item, with many, many features', '49.99']
        ]
        assert rows == expected_rows
        
        # Verify that commas in data are properly quoted in the raw output
        output_content = output_file.read_text()
        assert '"A great product, highly rated"' in output_content
        assert '"Simple, effective solution"' in output_content
        assert '"Complex item, with many, many features"' in output_content
    
    def test_data_containing_quotes(self, tmp_path):
        """Test handling data that contains quotes (should be escaped properly)."""
        # Create pipe-delimited file with quote-containing data
        input_file = tmp_path / "input_with_quotes.csv"
        input_content = '''Name|Quote|Author
Product A|He said "Hello World"|John Doe
Product B|She replied "That's great!"|Jane Smith
Product C|The sign read "Welcome to "Paradise" Resort"|Unknown'''
        input_file.write_text(input_content)
        
        output_file = tmp_path / "output_with_quotes.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Read and verify using csv.reader
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Quote', 'Author'],
            ['Product A', 'He said "Hello World"', 'John Doe'],
            ['Product B', 'She replied "That\'s great!"', 'Jane Smith'],
            ['Product C', 'The sign read "Welcome to "Paradise" Resort"', 'Unknown']
        ]
        assert rows == expected_rows
        
        # Verify that quotes are properly escaped in the raw output
        output_content = output_file.read_text()
        # In CSV, quotes are escaped by doubling them
        assert '""Hello World""' in output_content or '"He said ""Hello World"""' in output_content
    
    def test_empty_file(self, tmp_path):
        """Test with an empty file."""
        # Create empty input file
        input_file = tmp_path / "empty_input.csv"
        input_file.write_text("")
        
        output_file = tmp_path / "empty_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output is also empty
        output_content = output_file.read_text()
        assert output_content == ""
        
        # Verify using csv.reader
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert rows == []
    
    def test_file_with_only_headers(self, tmp_path):
        """Test with a file containing only headers."""
        # Create file with only header row
        input_file = tmp_path / "headers_only.csv"
        input_content = "Name|Age|City|Country"
        input_file.write_text(input_content)
        
        output_file = tmp_path / "headers_only_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output
        output_content = output_file.read_text()
        expected_content = "Name,Age,City,Country\n"
        assert output_content == expected_content
        
        # Verify using csv.reader
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [['Name', 'Age', 'City', 'Country']]
        assert rows == expected_rows
    
    def test_single_row_with_data(self, tmp_path):
        """Test with a file containing a single data row (no headers)."""
        input_file = tmp_path / "single_row.csv"
        input_content = "John Doe|25|Engineer|New York"
        input_file.write_text(input_content)
        
        output_file = tmp_path / "single_row_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [['John Doe', '25', 'Engineer', 'New York']]
        assert rows == expected_rows
    
    def test_mixed_complex_data(self, tmp_path):
        """Test with complex data containing pipes, commas, quotes, and newlines."""
        input_file = tmp_path / "complex_data.csv"
        input_content = '''Name|Description|Notes
Product A|Contains "special" chars|Price: $19.99, very popular
Product B|Multi-line
description here|Simple product
Product C|Has | pipe character|Also has, commas and "quotes"'''
        input_file.write_text(input_content)
        
        output_file = tmp_path / "complex_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify using csv.reader
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Description', 'Notes'],
            ['Product A', 'Contains "special" chars', 'Price: $19.99, very popular'],
            ['Product B', 'Multi-line\ndescription here', 'Simple product'],
            ['Product C', 'Has | pipe character', 'Also has, commas and "quotes"']
        ]
        assert rows == expected_rows

class TestConvertCsvErrorHandling:
    """Tests for error handling in convert_csv function."""
    
    def test_input_file_not_found(self, tmp_path):
        """Test behavior when input file doesn't exist."""
        output_file = tmp_path / "output.csv"
        
        with pytest.raises(FileNotFoundError):
            convert_csv("nonexistent_input.csv", str(output_file))
    
    def test_invalid_output_directory(self, tmp_path):
        """Test behavior when output directory doesn't exist."""
        input_file = tmp_path / "input.csv"
        input_file.write_text("Name|Age\nJohn|25")
        
        # Try to write to non-existent directory
        invalid_output = tmp_path / "nonexistent_dir" / "output.csv"
        
        with pytest.raises(FileNotFoundError):
            convert_csv(str(input_file), str(invalid_output))

class TestMainFunction:
    """Tests for the main function."""
    
    def test_main_with_correct_arguments(self, tmp_path, capsys):
        """Test main function with correct command line arguments."""
        # Create input file
        input_file = tmp_path / "test_input.csv"
        input_content = "Name|Age\nJohn|25\nAlice|30"
        input_file.write_text(input_content)
        
        output_file = tmp_path / "test_output.csv"
        
        # Mock sys.argv
        test_args = ["fix_csv.py", str(input_file), str(output_file)]
        with patch('sys.argv', test_args):
            main()
        
        # Verify output file was created correctly
        assert output_file.exists()
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [['Name', 'Age'], ['John', '25'], ['Alice', '30']]
        assert rows == expected_rows
        
        # Check that no error messages were printed
        captured = capsys.readouterr()
        assert captured.err == ""
    
    def test_main_with_insufficient_arguments(self, capsys):
        """Test main function with insufficient command line arguments."""
        # Test with no arguments
        test_args = ["fix_csv.py"]
        with patch('sys.argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Usage: python fix_csv.py <input_file> <output_file>" in captured.out
    
    def test_main_with_too_many_arguments(self, capsys):
        """Test main function with too many command line arguments."""
        test_args = ["fix_csv.py", "input.csv", "output.csv", "extra_arg"]
        with patch('sys.argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Usage: python fix_csv.py <input_file> <output_file>" in captured.out
    
    def test_main_with_one_argument(self, capsys):
        """Test main function with only one argument."""
        test_args = ["fix_csv.py", "input.csv"]
        with patch('sys.argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Usage: python fix_csv.py <input_file> <output_file>" in captured.out

class TestParametrizedScenarios:
    """Parametrized tests for various conversion scenarios."""
    
    @pytest.mark.parametrize("input_content,expected_rows", [
        # Simple cases
        ("a|b\n1|2", [['a', 'b'], ['1', '2']]),
        ("x", [['x']]),
        ("a|b|c", [['a', 'b', 'c']]),
        
        # Empty fields
        ("|b|\n1||3", [['', 'b', ''], ['1', '', '3']]),
        
        # Single column
        ("Name\nJohn\nAlice", [['Name'], ['John'], ['Alice']]),
        
        # Numbers and mixed data
        ("ID|Value\n1|100.50\n2|200.75", [['ID', 'Value'], ['1', '100.50'], ['2', '200.75']]),
        
        # Special characters (not commas or quotes)
        ("Name|Symbol\nTest|@#$%\nAnother|&*!", [['Name', 'Symbol'], ['Test', '@#$%'], ['Another', '&*!']]),
    ])
    def test_various_conversion_scenarios(self, input_content, expected_rows, tmp_path):
        """Test convert_csv with various input scenarios."""
        input_file = tmp_path / "param_input.csv"
        input_file.write_text(input_content)
        
        output_file = tmp_path / "param_output.csv"
        
        # Run conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        assert rows == expected_rows

class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""
    
    def test_trailing_pipes(self, tmp_path):
        """Test handling of trailing pipe characters."""
        input_file = tmp_path / "trailing_pipes.csv"
        input_content = """Name|Age|
John|25|
Alice|30|"""
        input_file.write_text(input_content)
        
        output_file = tmp_path / "trailing_pipes_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Age', ''],
            ['John', '25', ''],
            ['Alice', '30', '']
        ]
        assert rows == expected_rows
    
    def test_inconsistent_column_counts(self, tmp_path):
        """Test handling of rows with different numbers of columns."""
        input_file = tmp_path / "inconsistent_columns.csv"
        input_content = """Name|Age|City
John|25
Alice|30|Los Angeles|Extra
Bob|35|Chicago"""
        input_file.write_text(input_content)
        
        output_file = tmp_path / "inconsistent_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Age', 'City'],
            ['John', '25'],
            ['Alice', '30', 'Los Angeles', 'Extra'],
            ['Bob', '35', 'Chicago']
        ]
        assert rows == expected_rows
    
    def test_whitespace_handling(self, tmp_path):
        """Test handling of whitespace in fields."""
        input_file = tmp_path / "whitespace.csv"
        input_content = """Name|Age|City
 John |25| New York 
Alice| 30|Los Angeles
 Bob | 35 | Chicago """
        input_file.write_text(input_content)
        
        output_file = tmp_path / "whitespace_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output (whitespace should be preserved)
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Age', 'City'],
            [' John ', '25', ' New York '],
            ['Alice', ' 30', 'Los Angeles'],
            [' Bob ', ' 35 ', ' Chicago ']
        ]
        assert rows == expected_rows
    
    def test_unicode_characters(self, tmp_path):
        """Test handling of Unicode characters."""
        input_file = tmp_path / "unicode.csv"
        input_content = """Name|City|Country
José|São Paulo|Brasil
François|Montréal|Canada
山田|東京|日本"""
        input_file.write_text(input_content, encoding='utf-8')
        
        output_file = tmp_path / "unicode_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output
        with open(output_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'City', 'Country'],
            ['José', 'São Paulo', 'Brasil'],
            ['François', 'Montréal', 'Canada'],
            ['山田', '東京', '日本']
        ]
        assert rows == expected_rows
    
    def test_very_long_fields(self, tmp_path):
        """Test handling of very long field content."""
        long_text = "A" * 1000  # 1000 character string
        input_file = tmp_path / "long_fields.csv"
        input_content = f"Name|Description\nProduct|{long_text}"
        input_file.write_text(input_content)
        
        output_file = tmp_path / "long_fields_output.csv"
        
        # Run the conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify output
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [
            ['Name', 'Description'],
            ['Product', long_text]
        ]
        assert rows == expected_rows

class TestFileIntegrity:
    """Tests to ensure file integrity and proper handling."""
    
    def test_file_overwrite_behavior(self, tmp_path):
        """Test that output file is properly overwritten if it exists."""
        input_file = tmp_path / "input.csv"
        input_file.write_text("Name|Age\nJohn|25")
        
        output_file = tmp_path / "output.csv"
        # Create existing output file with different content
        output_file.write_text("Old,Content,Here\n1,2,3")
        
        # Run conversion
        convert_csv(str(input_file), str(output_file))
        
        # Verify old content is completely replaced
        with open(output_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [['Name', 'Age'], ['John', '25']]
        assert rows == expected_rows
        
        # Verify no traces of old content
        content = output_file.read_text()
        assert "Old" not in content
        assert "Content" not in content
    
    def test_same_input_output_file(self, tmp_path):
        """Test behavior when input and output filenames are the same."""
        # Note: This is a potentially destructive operation in real usage
        test_file = tmp_path / "same_file.csv"
        original_content = "Name|Age\nJohn|25\nAlice|30"
        test_file.write_text(original_content)
        
        # This should work but will overwrite the original file
        convert_csv(str(test_file), str(test_file))
        
        # Verify the file now contains comma-separated data
        with open(test_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        expected_rows = [['Name', 'Age'], ['John', '25'], ['Alice', '30']]
        assert rows == expected_rows
        
        # Verify original pipe format is gone
        content = test_file.read_text()
        assert '|' not in content

if __name__ == "__main__":
    pytest.main([__file__, "-v"])