# line_numbers_test.py
import pytest
import tempfile
from pathlib import Path
from argparse import ArgumentParser, FileType

# Import the functions we're testing
from line_numbers import print_with_line_numbers, main

class TestPrintWithLineNumbers:
    """Tests for the print_with_line_numbers function."""
    
    def test_simple_text_file_multiple_lines(self, capsys, tmp_path):
        """Test with a simple text file containing multiple lines."""
        # Create a test file with multiple lines
        test_file = tmp_path / "test_file.txt"
        test_content = "First line\nSecond line\nThird line\nFourth line"
        test_file.write_text(test_content)
        
        # Open the file and test the function
        with open(test_file, 'r') as f:
            print_with_line_numbers(f)
        
        # Capture and verify the output
        captured = capsys.readouterr()
        expected_output = "1 First line\n2 Second line\n3 Third line\n4 Fourth line\n"
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_empty_file(self, capsys, tmp_path):
        """Test with an empty file."""
        # Create an empty test file
        test_file = tmp_path / "empty_file.txt"
        test_file.write_text("")
        
        # Open the file and test the function
        with open(test_file, 'r') as f:
            print_with_line_numbers(f)
        
        # Capture and verify the output (should be empty)
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    def test_file_with_blank_lines(self, capsys, tmp_path):
        """Test with a file containing blank lines."""
        # Create a test file with blank lines
        test_file = tmp_path / "blank_lines_file.txt"
        test_content = "Line 1\n\nLine 3\n\n\nLine 6"
        test_file.write_text(test_content)
        
        # Open the file and test the function
        with open(test_file, 'r') as f:
            print_with_line_numbers(f)
        
        # Capture and verify the output
        captured = capsys.readouterr()
        expected_output = "1 Line 1\n2 \n3 Line 3\n4 \n5 \n6 Line 6\n"
        assert captured.out == expected_output
        assert captured.err == ""