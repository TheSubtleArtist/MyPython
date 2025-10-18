# line_numbers_test2.py
import pytest
import sys
from pathlib import Path
from unittest.mock import patch

# Import the functions we're testing
from line_numbers import print_with_line_numbers, main

# Base args fixture for controlling command-line arguments
@pytest.fixture
def args(monkeypatch):
    """
    PYTEST FEATURE: Base fixture for controlling command-line arguments
    BENEFIT: Reusable way to set sys.argv for testing main() function
    STUDENT NOTE: This fixture uses monkeypatch to safely modify sys.argv
    """
    def _set_args(arg_list):
        """Set sys.argv to the provided argument list."""
        full_args = ["line_numbers.py"] + arg_list
        monkeypatch.setattr(sys, 'argv', full_args)
    return _set_args

@pytest.fixture
def path_arg(args, tmp_path):
    """
    PYTEST FEATURE: Composite fixture using multiple other fixtures
    BENEFIT: Combines args and tmp_path to create a file path argument setup
    STUDENT NOTE: This fixture depends on both args and tmp_path fixtures
    
    Uses the args fixture and tmp_path fixture:
    - Puts a specific file path in the first argument of sys.argv
    - Returns that pathlib.Path object so you can call write_text on it
    """
    # Create a test file path
    test_file = tmp_path / "test_file.txt"
    
    # Set up command line arguments with this file path
    args([str(test_file)])
    
    # Return the Path object so tests can write content to it
    return test_file

class TestMainFunctionWithPathArg:
    """Tests for the main function using the path_arg fixture."""
    
    def test_main_with_simple_text_file(self, path_arg, capsys):
        """
        PYTEST FEATURE: Using composite fixture with capsys
        BENEFIT: Test main function with real file creation and output capture
        STUDENT NOTE: path_arg sets up both the file path and command line args
        """
        # Write content to the file using the returned Path object
        path_arg.write_text("First line\nSecond line\nThird line")
        
        # Run main function
        main()
        
        # Verify output
        captured = capsys.readouterr()
        expected_output = "1 First line\n2 Second line\n3 Third line\n"
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_main_with_empty_file(self, path_arg, capsys):
        """Test main function with an empty file."""
        # Create empty file
        path_arg.write_text("")
        
        # Run main function
        main()
        
        # Verify no output for empty file
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    def test_main_with_single_line(self, path_arg, capsys):
        """Test main function with a file containing a single line."""
        path_arg.write_text("Only one line")
        
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "1 Only one line\n"
        assert captured.err == ""
    
    def test_main_with_blank_lines(self, path_arg, capsys):
        """Test main function with a file containing blank lines."""
        content = "Line 1\n\nLine 3\n\n\nLine 6"
        path_arg.write_text(content)
        
        main()
        
        captured = capsys.readouterr()
        expected_output = "1 Line 1\n2 \n3 Line 3\n4 \n5 \n6 Line 6\n"
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_main_with_lines_ending_in_newlines(self, path_arg, capsys):
        """Test main function with file where all lines properly end with newlines."""
        content = "First line\nSecond line\nThird line\n"
        path_arg.write_text(content)
        
        main()
        
        captured = capsys.readouterr()
        expected_output = "1 First line\n2 Second line\n3 Third line\n"
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_main_with_very_long_lines(self, path_arg, capsys):
        """Test main function with very long lines."""
        long_line = "A" * 1000
        content = f"Short line\n{long_line}\nAnother short line"
        path_arg.write_text(content)
        
        main()
        
        captured = capsys.readouterr()
        expected_output = f"1 Short line\n2 {long_line}\n3 Another short line\n"
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_main_with_special_characters(self, path_arg, capsys):
        """Test main function with special characters in file content."""
        content = "Line with tabs\there\nLine with unicode: café, naïve\nLine with symbols: @#$%^&*()"
        path_arg.write_text(content)
        
        main()
        
        captured = capsys.readouterr()
        expected_lines = [
            "1 Line with tabs\there",
            "2 Line with unicode: café, naïve", 
            "3 Line with symbols: @#$%^&*()"
        ]
        expected_output = "\n".join(expected_lines) + "\n"
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_main_with_mixed_line_endings(self, path_arg, capsys):
        """Test main function with different line ending styles."""
        # Create content with different line endings
        content = "Line 1\nLine 2\rLine 3\r\nLine 4"
        path_arg.write_text(content)
        
        main()
        
        captured = capsys.readouterr()
        # The exact output depends on how Python handles different line endings
        # when reading in text mode, but we should get 4 numbered lines
        lines = captured.out.strip().split('\n')
        assert len(lines) >= 3  # At least 3 lines should be present
        assert lines[0].startswith("1 ")
        assert lines[1].startswith("2 ")

class TestMainFunctionParametrized:
    """Parametrized tests using the path_arg fixture."""
    
    @pytest.mark.parametrize("file_content,expected_line_count", [
        ("", 0),
        ("Single line", 1),
        ("Line 1\nLine 2", 2),
        ("Line 1\nLine 2\nLine 3", 3),
        ("\n\n\n", 3),  # Three blank lines
        ("A\nB\nC\nD\nE", 5),
        ("First\n\nThird\n\nFifth", 5),  # Mixed content and blank lines
    ])
    def test_main_various_line_counts(self, path_arg, capsys, file_content, expected_line_count):
        """
        PYTEST FEATURE: Parametrized test with fixture
        BENEFIT: Test multiple scenarios with consistent setup
        STUDENT NOTE: path_arg fixture works seamlessly with parametrized tests
        """
        path_arg.write_text(file_content)
        
        main()
        
        captured = capsys.readouterr()
        if expected_line_count == 0:
            assert captured.out == ""
        else:
            lines = captured.out.strip().split('\n')
            assert len(lines) == expected_line_count
            
            # Verify line numbers are correct
            for i, line in enumerate(lines, 1):
                assert line.startswith(f"{i} ")

class TestMainFunctionErrorHandling:
    """Test error handling scenarios with the path_arg fixture."""
    
    def test_main_with_nonexistent_file(self, args):
        """
        PYTEST FEATURE: Testing with non-existent files
        BENEFIT: Verify proper error handling for file operations
        STUDENT NOTE: Uses args fixture directly since we don't want to create the file
        """
        # Use args fixture directly with a non-existent file path
        args(["/nonexistent/path/file.txt"])
        
        with pytest.raises(SystemExit):
            main()
    
    def test_main_with_directory_instead_of_file(self, args, tmp_path):
        """Test main function when argument points to a directory."""
        # Create a directory
        test_dir = tmp_path / "test_directory"
        test_dir.mkdir()
        
        args([str(test_dir)])
        
        with pytest.raises(SystemExit):
            main()
    
    def test_main_with_binary_file(self, path_arg, capsys):
        """Test main function with binary content (should still work in text mode)."""
        # Write some binary-like content
        path_arg.write_bytes(b"Binary content\x00\x01\x02\nSecond line")
        
        # This might work or fail depending on the binary content
        # Let's test that it doesn't crash catastrophically
        try:
            main()
            captured = capsys.readouterr()
            # If it works, verify we get some output
            assert len(captured.out) > 0
        except (UnicodeDecodeError, SystemExit):
            # If it fails due to binary content, that's also acceptable behavior
            pass

class TestMainFunctionEdgeCases:
    """Edge case tests using the path_arg fixture."""
    
    def test_main_with_very_large_file(self, path_arg, capsys):
        """Test main function with a file containing many lines."""
        # Create a file with 100 lines
        lines = [f"Line number {i}" for i in range(1, 101)]
        content = "\n".join(lines)
        path_arg.write_text(content)
        
        main()
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        assert len(output_lines) == 100
        
        # Verify first and last lines are numbered correctly
        assert output_lines[0] == "1 Line number 1"
        assert output_lines[99] == "100 Line number 100"
    
    def test_main_with_unicode_content(self, path_arg, capsys):
        """Test main function with Unicode content."""
        content = "English line\nLigne française\nLinea española\n日本語の行\n한국어 줄"
        path_arg.write_text(content, encoding='utf-8')
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        assert len(lines) == 5
        assert lines[0] == "1 English line"
        assert lines[1] == "2 Ligne française"
        assert lines[2] == "3 Linea española"
        assert lines[3] == "4 日本語の行"
        assert lines[4] == "5 한국어 줄"
    
    def test_main_with_only_newlines(self, path_arg, capsys):
        """Test main function with file containing only newline characters."""
        content = "\n\n\n\n\n"
        path_arg.write_text(content)
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        assert len(lines) == 5
        
        # All lines should be just the line number followed by a space
        for i in range(5):
            assert lines[i] == f"{i + 1} "
    
    def test_main_with_trailing_newline_vs_no_trailing_newline(self, path_arg, capsys):
        """Test difference between files with and without trailing newlines."""
        # Test with trailing newline
        path_arg.write_text("Line 1\nLine 2\n")
        main()
        captured1 = capsys.readouterr()
        
        # Reset and test without trailing newline
        path_arg.write_text("Line 1\nLine 2")
        main()
        captured2 = capsys.readouterr()
        
        # Both should produce the same output (2 numbered lines)
        assert captured1.out == captured2.out
        assert captured1.out == "1 Line 1\n2 Line 2\n"

class TestPathArgFixtureItself:
    """Tests to verify the path_arg fixture works correctly."""
    
    def test_path_arg_returns_path_object(self, path_arg):
        """
        PYTEST FEATURE: Testing fixtures themselves
        BENEFIT: Verify that custom fixtures work as expected
        STUDENT NOTE: Good practice to test complex fixtures
        """
        # Verify path_arg returns a Path object
        assert isinstance(path_arg, Path)
        
        # Verify we can write to it
        path_arg.write_text("test content")
        assert path_arg.read_text() == "test content"
    
    def test_path_arg_sets_command_line_args(self, path_arg):
        """Test that path_arg fixture properly sets command line arguments."""
        # The fixture should have set sys.argv
        assert len(sys.argv) == 2
        assert sys.argv[0] == "line_numbers.py"
        assert sys.argv[1] == str(path_arg)
    
    def test_path_arg_creates_unique_files(self, path_arg, tmp_path):
        """Test that path_arg creates files in the temporary directory."""
        # Verify the file is in the tmp_path directory
        assert path_arg.parent == tmp_path
        
        # Verify the file doesn't exist yet (until we write to it)
        assert not path_arg.exists()
        
        # After writing, it should exist
        path_arg.write_text("content")
        assert path_arg.exists()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])