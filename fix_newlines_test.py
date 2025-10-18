# fix_newlines_test.py
import pytest
import os
from pathlib import Path
from unittest.mock import patch

# Import the function we're testing
from fix_newlines import fix_newlines

class TestFixNewlines:
    """Tests for the fix_newlines function."""
    
    def test_file_already_ends_with_newline(self, tmp_path):
        """Test with a file that already ends with a newline (should remain unchanged)."""
        # Create a test file that already ends with a newline
        test_file = tmp_path / "with_newline.txt"
        original_content = "Line 1\nLine 2\nLine 3\n"
        test_file.write_text(original_content)
        
        # Store original file size
        original_size = test_file.stat().st_size
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify the file content and size remain unchanged
        result_content = test_file.read_text()
        assert result_content == original_content
        assert test_file.stat().st_size == original_size
    
    def test_file_without_newline_adds_one(self, tmp_path):
        """Test with a file that doesn't end with a newline (should add one)."""
        # Create a test file that doesn't end with a newline
        test_file = tmp_path / "without_newline.txt"
        original_content = "Line 1\nLine 2\nLine 3"
        test_file.write_text(original_content)
        
        # Store original file size
        original_size = test_file.stat().st_size
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify a newline was added
        result_content = test_file.read_text()
        expected_content = original_content + "\n"
        assert result_content == expected_content
        assert test_file.stat().st_size == original_size + 1
    
    def test_empty_file_gets_newline(self, tmp_path):
        """Test with an empty file (should add a newline)."""
        # Create an empty test file
        test_file = tmp_path / "empty.txt"
        test_file.write_text("")
        
        # Verify the file is initially empty
        assert test_file.stat().st_size == 0
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify a newline was added
        result_content = test_file.read_text()
        assert result_content == "\n"
        assert test_file.stat().st_size == 1
    
    def test_single_character_file_without_newline(self, tmp_path):
        """Test with a single character file that doesn't end with newline."""
        test_file = tmp_path / "single_char.txt"
        test_file.write_text("A")
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify newline was added
        result_content = test_file.read_text()
        assert result_content == "A\n"
        assert test_file.stat().st_size == 2
    
    def test_single_newline_file(self, tmp_path):
        """Test with a file containing only a newline character."""
        test_file = tmp_path / "only_newline.txt"
        test_file.write_text("\n")
        
        original_size = test_file.stat().st_size
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify file remains unchanged
        result_content = test_file.read_text()
        assert result_content == "\n"
        assert test_file.stat().st_size == original_size
    
    def test_file_with_multiple_trailing_newlines(self, tmp_path):
        """Test with a file that already has multiple trailing newlines."""
        test_file = tmp_path / "multiple_newlines.txt"
        original_content = "Line 1\nLine 2\n\n\n"
        test_file.write_text(original_content)
        
        original_size = test_file.stat().st_size
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify file remains unchanged (already ends with newline)
        result_content = test_file.read_text()
        assert result_content == original_content
        assert test_file.stat().st_size == original_size
    
    def test_binary_content_without_newline(self, tmp_path):
        """Test with binary content that doesn't end with newline."""
        test_file = tmp_path / "binary.txt"
        # Write binary content directly
        original_content = b"Hello\x00World\xff"
        with open(test_file, "wb") as f:
            f.write(original_content)
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify newline was added
        with open(test_file, "rb") as f:
            result_content = f.read()
        
        expected_content = original_content + b"\n"
        assert result_content == expected_content
    
    def test_binary_content_with_newline(self, tmp_path):
        """Test with binary content that already ends with newline."""
        test_file = tmp_path / "binary_with_newline.txt"
        original_content = b"Hello\x00World\xff\n"
        with open(test_file, "wb") as f:
            f.write(original_content)
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify file remains unchanged
        with open(test_file, "rb") as f:
            result_content = f.read()
        
        assert result_content == original_content
    
    def test_large_file_without_newline(self, tmp_path):
        """Test with a larger file that doesn't end with newline."""
        test_file = tmp_path / "large_file.txt"
        # Create content with 1000 lines, last one without newline
        lines = [f"Line {i}" for i in range(1000)]
        original_content = "\n".join(lines)  # No trailing newline
        test_file.write_text(original_content)
        
        original_size = test_file.stat().st_size
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify newline was added
        result_content = test_file.read_text()
        expected_content = original_content + "\n"
        assert result_content == expected_content
        assert test_file.stat().st_size == original_size + 1
    
    def test_file_ending_with_carriage_return(self, tmp_path):
        """Test with a file ending with carriage return but no newline."""
        test_file = tmp_path / "carriage_return.txt"
        # Write content ending with \r (carriage return) but no \n
        with open(test_file, "wb") as f:
            f.write(b"Line 1\r\nLine 2\r")
        
        original_size = test_file.stat().st_size
        
        # Run the function
        fix_newlines(test_file)
        
        # Verify newline was added after the carriage return
        with open(test_file, "rb") as f:
            result_content = f.read()
        
        expected_content = b"Line 1\r\nLine 2\r\n"
        assert result_content == expected_content
        assert test_file.stat().st_size == original_size + 1

class TestFixNewlinesErrorHandling:
    """Tests for error handling in fix_newlines function."""
    
    def test_nonexistent_file(self):
        """Test behavior when file doesn't exist."""
        with pytest.raises(FileNotFoundError):
            fix_newlines("nonexistent_file.txt")
    
    def test_directory_instead_of_file(self, tmp_path):
        """Test behavior when path points to a directory."""
        test_dir = tmp_path / "test_directory"
        test_dir.mkdir()
        
        with pytest.raises(IsADirectoryError):
            fix_newlines(test_dir)
    
    def test_permission_denied_simulation(self, tmp_path, monkeypatch):
        """Test behavior when file permissions prevent writing."""
        test_file = tmp_path / "readonly.txt"
        test_file.write_text("content")
        
        # Mock open to raise PermissionError
        original_open = open
        def mock_open(*args, **kwargs):
            if "rb+" in args:
                raise PermissionError("Permission denied")
            return original_open(*args, **kwargs)
        
        monkeypatch.setattr("builtins.open", mock_open)
        
        with pytest.raises(PermissionError):
            fix_newlines(test_file)

class TestFixNewlinesWithPaths:
    """Tests using different path representations."""
    
    def test_with_string_path(self, tmp_path):
        """Test function works with string paths."""
        test_file = tmp_path / "string_path.txt"
        test_file.write_text("content without newline")
        
        # Pass string path instead of Path object
        fix_newlines(str(test_file))
        
        result_content = test_file.read_text()
        assert result_content == "content without newline\n"
    
    def test_with_pathlib_path(self, tmp_path):
        """Test function works with pathlib.Path objects."""
        test_file = tmp_path / "pathlib_path.txt"
        test_file.write_text("content without newline")
        
        # Pass Path object
        fix_newlines(test_file)
        
        result_content = test_file.read_text()
        assert result_content == "content without newline\n"

class TestMainFunctionIntegration:
    """Integration tests for the main function."""
    
    def test_main_function_with_args(self, tmp_path):
        """Test the main function with command line arguments."""
        test_file = tmp_path / "main_test.txt"
        test_file.write_text("content without newline")
        
        # Mock sys.argv to simulate command line execution
        test_args = ["fix_newlines.py", str(test_file)]
        with patch('sys.argv', test_args):
            # Import and run main (avoiding the if __name__ == "__main__" block)
            from fix_newlines import ArgumentParser, Path
            parser = ArgumentParser()
            parser.add_argument("file", type=Path)
            args = parser.parse_args(test_args[1:])
            fix_newlines(args.file)
        
        # Verify the file was modified
        result_content = test_file.read_text()
        assert result_content == "content without newline\n"

class TestParametrizedScenarios:
    """Parametrized tests for various file content scenarios."""
    
    @pytest.mark.parametrize("original_content,should_add_newline", [
        ("", True),  # Empty file
        ("a", True),  # Single character
        ("hello", True),  # Simple text
        ("line1\nline2", True),  # Multiple lines, no trailing newline
        ("hello\n", False),  # Already has newline
        ("line1\nline2\n", False),  # Multiple lines with trailing newline
        ("\n", False),  # Only newline
        ("text\n\n", False),  # Multiple trailing newlines
    ])
    def test_various_content_scenarios(self, original_content, should_add_newline, tmp_path):
        """Test fix_newlines with various content scenarios."""
        test_file = tmp_path / "param_test.txt"
        test_file.write_text(original_content)
        
        original_size = test_file.stat().st_size
        
        # Run the function
        fix_newlines(test_file)
        
        # Check results
        result_content = test_file.read_text()
        new_size = test_file.stat().st_size
        
        if should_add_newline:
            assert result_content == original_content + "\n"
            assert new_size == original_size + 1
        else:
            assert result_content == original_content
            assert new_size == original_size

class TestFileHandleOperations:
    """Tests focusing on file handle operations and edge cases."""
    
    def test_file_seek_operations(self, tmp_path):
        """Test that file seeking operations work correctly."""
        test_file = tmp_path / "seek_test.txt"
        test_content = "Hello World"
        test_file.write_text(test_content)
        
        # Manually verify the file operations that fix_newlines performs
        with open(test_file, "rb+") as f:
            # Test SEEK_END operation
            file_size = f.seek(0, os.SEEK_END)
            assert file_size == len(test_content.encode())
            
            # Test seeking to last character
            f.seek(-1, os.SEEK_END)
            last_char = f.read(1)
            assert last_char == b"d"  # Last character of "World"
        
        # Now run our function
        fix_newlines(test_file)
        
        # Verify newline was added
        result_content = test_file.read_text()
        assert result_content == test_content + "\n"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])