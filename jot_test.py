# jot_test.py
import pytest
from datetime import date
from pathlib import Path
from unittest.mock import patch, mock_open
from io import StringIO

# Import the function we're testing
from jot import main

class TestJotMainFunction:
    """
    Tests for the jot.py main function using student-friendly mocking approaches.
    
    STUDENT NOTE: This class demonstrates the most readable and understandable
    methods for mocking multiple components in a single function.
    """
    
    def test_basic_jot_functionality(self, monkeypatch, tmp_path):
        """
        Test basic jot functionality with all necessary mocks.
        
        STUDENT-FRIENDLY APPROACH: Using monkeypatch for all mocking
        BENEFIT: Consistent, understandable mocking approach with automatic cleanup
        EDUCATIONAL NOTE: This shows how to mock multiple things in one test
        """
        # 1. MOCK USER INPUT - simulate typing "Hello World"
        # STUDENT NOTE: This replaces input() with a function that returns our test text
        monkeypatch.setattr('builtins.input', lambda prompt: 'Hello World')
        
        # 2. MOCK THE CURRENT DATE - set to a specific known date
        # STUDENT NOTE: This ensures consistent test results regardless of when tests run
        mock_date = date(2023, 12, 25)  # Christmas 2023
        monkeypatch.setattr('jot.date.today', lambda: mock_date)
        
        # 3. MOCK THE FILE PATH - redirect to our temporary directory
        # STUDENT NOTE: This prevents writing to the real home directory
        test_jot_file = tmp_path / "jot.txt"
        mock_home_path = tmp_path
        monkeypatch.setattr('jot.Path.home', lambda: mock_home_path)
        
        # 4. RUN THE FUNCTION
        main()
        
        # 5. VERIFY FILE CONTENT MATCHES EXPECTED FORMAT
        # STUDENT NOTE: Read the file and check it contains exactly what we expect
        assert test_jot_file.exists(), "jot.txt file should be created"
        
        file_content = test_jot_file.read_text()
        expected_content = "2023-12-25 Hello World\n"
        assert file_content == expected_content
    
    def test_multiple_jot_entries(self, monkeypatch, tmp_path):
        """
        Test that multiple jot entries append to the same file.
        
        EDUCATIONAL FOCUS: Shows how file append mode works
        STUDENT NOTE: Each call to main() should add a new line to the file
        """
        # Set up mocks for first entry
        test_jot_file = tmp_path / "jot.txt"
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        # First entry
        monkeypatch.setattr('builtins.input', lambda prompt: 'First entry')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        main()
        
        # Second entry
        monkeypatch.setattr('builtins.input', lambda prompt: 'Second entry')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 2))
        main()
        
        # Verify both entries are in the file
        file_content = test_jot_file.read_text()
        expected_content = "2023-01-01 First entry\n2023-01-02 Second entry\n"
        assert file_content == expected_content
    
    def test_empty_input_handling(self, monkeypatch, tmp_path):
        """
        Test how jot handles empty user input.
        
        STUDENT NOTE: This tests edge cases - what happens with no text?
        """
        # Mock empty input
        monkeypatch.setattr('builtins.input', lambda prompt: '')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 6, 15))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        # Verify file contains date and empty text
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        expected_content = "2023-06-15 \n"  # Date + space + empty text + newline
        assert file_content == expected_content
    
    def test_special_characters_in_input(self, monkeypatch, tmp_path):
        """
        Test jot with special characters, symbols, and Unicode.
        
        STUDENT NOTE: Real-world text often contains special characters
        """
        special_text = "Special chars: !@#$%^&*()_+ émojis 🎉 and línés"
        
        monkeypatch.setattr('builtins.input', lambda prompt: special_text)
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 3, 14))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text(encoding='utf-8')
        expected_content = f"2023-03-14 {special_text}\n"
        assert file_content == expected_content

class TestJotParametrizedScenarios:
    """
    Parametrized tests for systematic testing of various inputs.
    
    STUDENT NOTE: Parametrized tests let us test many scenarios efficiently
    """
    
    @pytest.mark.parametrize("user_input,test_date,expected_line", [
        ("Morning thoughts", date(2023, 1, 1), "2023-01-01 Morning thoughts\n"),
        ("", date(2023, 12, 31), "2023-12-31 \n"),
        ("Short", date(2023, 7, 4), "2023-07-04 Short\n"),
        ("A very long entry with many words and thoughts", date(2023, 2, 14), 
         "2023-02-14 A very long entry with many words and thoughts\n"),
        ("Numbers 123 and symbols !@#", date(2023, 5, 5), "2023-05-05 Numbers 123 and symbols !@#\n"),
    ])
    def test_various_input_scenarios(self, monkeypatch, tmp_path, user_input, test_date, expected_line):
        """
        PYTEST FEATURE: Parametrized testing with multiple mocks
        BENEFIT: Test many scenarios with clean, readable test cases
        STUDENT NOTE: Each parameter set becomes a separate test
        """
        # Apply all necessary mocks
        monkeypatch.setattr('builtins.input', lambda prompt: user_input)
        monkeypatch.setattr('jot.date.today', lambda: test_date)
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        # Run the function
        main()
        
        # Verify the result
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        assert file_content == expected_line

class TestJotFileOperations:
    """
    Tests focused on file operations and path handling.
    
    STUDENT NOTE: These tests verify that files are created and written correctly
    """
    
    def test_file_created_in_correct_location(self, monkeypatch, tmp_path):
        """
        Test that jot.txt is created in the home directory.
        
        EDUCATIONAL FOCUS: Path construction and file creation
        """
        monkeypatch.setattr('builtins.input', lambda prompt: 'test')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        # Verify file exists in the expected location
        expected_file_path = tmp_path / "jot.txt"
        assert expected_file_path.exists()
        assert expected_file_path.is_file()
    
    def test_file_append_mode_behavior(self, monkeypatch, tmp_path):
        """
        Test that the file is opened in append mode.
        
        STUDENT NOTE: This verifies that existing content isn't overwritten
        """
        test_jot_file = tmp_path / "jot.txt"
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        # Create initial content in the file
        test_jot_file.write_text("Existing content\n")
        
        # Add new content via jot
        monkeypatch.setattr('builtins.input', lambda prompt: 'New entry')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        main()
        
        # Verify both old and new content exist
        file_content = test_jot_file.read_text()
        assert "Existing content\n" in file_content
        assert "2023-01-01 New entry\n" in file_content
    
    def test_file_permissions_and_encoding(self, monkeypatch, tmp_path):
        """
        Test that the file can be read after writing.
        
        STUDENT NOTE: Ensures proper file permissions and encoding
        """
        monkeypatch.setattr('builtins.input', lambda prompt: 'Test content')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        test_jot_file = tmp_path / "jot.txt"
        
        # Verify file is readable
        assert test_jot_file.is_file()
        content = test_jot_file.read_text()
        assert content == "2023-01-01 Test content\n"
        
        # Verify file size is reasonable
        assert test_jot_file.stat().st_size > 0

class TestJotDateFormatting:
    """
    Tests focused on date formatting and behavior.
    
    STUDENT NOTE: These tests verify the date appears correctly in the output
    """
    
    @pytest.mark.parametrize("test_date,expected_date_str", [
        (date(2023, 1, 1), "2023-01-01"),
        (date(2023, 12, 31), "2023-12-31"),
        (date(2000, 2, 29), "2000-02-29"),  # Leap year
        (date(1999, 5, 15), "1999-05-15"),
        (date(2024, 7, 4), "2024-07-04"),
    ])
    def test_date_formatting(self, monkeypatch, tmp_path, test_date, expected_date_str):
        """
        Test that dates are formatted correctly in ISO format (YYYY-MM-DD).
        
        PYTEST FEATURE: Testing date formatting specifically
        STUDENT NOTE: Verifies consistent date format regardless of locale
        """
        monkeypatch.setattr('builtins.input', lambda prompt: 'test entry')
        monkeypatch.setattr('jot.date.today', lambda: test_date)
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        
        # Verify the date appears correctly formatted
        assert file_content.startswith(expected_date_str)
        assert file_content == f"{expected_date_str} test entry\n"

class TestJotInputPrompt:
    """
    Tests to verify the input prompt behavior.
    
    STUDENT NOTE: These tests check the user interface aspect
    """
    
    def test_input_prompt_text(self, monkeypatch, tmp_path):
        """
        Test that the correct prompt is displayed to the user.
        
        EDUCATIONAL FOCUS: User interface testing
        """
        captured_prompts = []
        
        def mock_input(prompt):
            captured_prompts.append(prompt)
            return "test response"
        
        monkeypatch.setattr('builtins.input', mock_input)
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        # Verify the prompt text
        assert len(captured_prompts) == 1
        assert captured_prompts[0] == "jot: "

class TestJotCompleteWorkflow:
    """
    Integration tests that verify the complete workflow.
    
    STUDENT NOTE: These tests verify all components working together
    """
    
    def test_complete_user_session_simulation(self, monkeypatch, tmp_path):
        """
        Simulate a complete user session with multiple entries.
        
        EDUCATIONAL FOCUS: End-to-end workflow testing
        """
        # Simulate user session over multiple days
        entries = [
            ("2023-01-01", "Started learning Python"),
            ("2023-01-02", "Learned about functions"),
            ("2023-01-03", "Working on file I/O"),
            ("2023-01-04", "Testing with pytest!"),
        ]
        
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        # Add each entry
        for date_str, text in entries:
            year, month, day = map(int, date_str.split('-'))
            test_date = date(year, month, day)
            
            monkeypatch.setattr('builtins.input', lambda prompt, t=text: t)
            monkeypatch.setattr('jot.date.today', lambda d=test_date: d)
            
            main()
        
        # Verify all entries are in the file
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        
        for date_str, text in entries:
            expected_line = f"{date_str} {text}\n"
            assert expected_line in file_content
        
        # Verify correct number of lines
        lines = file_content.strip().split('\n')
        assert len(lines) == 4
    
    def test_realistic_daily_usage(self, monkeypatch, tmp_path):
        """
        Test realistic daily usage patterns.
        
        STUDENT NOTE: This simulates how someone might actually use the jot program
        """
        # Mock setup
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        # Day 1: Morning entry
        monkeypatch.setattr('builtins.input', lambda prompt: 'Morning coffee and planning')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 6, 1))
        main()
        
        # Day 1: Evening entry  
        monkeypatch.setattr('builtins.input', lambda prompt: 'Completed project milestone')
        main()  # Same date
        
        # Day 2: Quick note
        monkeypatch.setattr('builtins.input', lambda prompt: 'Remember to call mom')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 6, 2))
        main()
        
        # Verify the journal file
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        
        expected_content = (
            "2023-06-01 Morning coffee and planning\n"
            "2023-06-01 Completed project milestone\n"
            "2023-06-02 Remember to call mom\n"
        )
        assert file_content == expected_content
        
        # Verify file structure
        lines = file_content.strip().split('\n')
        assert len(lines) == 3
        
        # Verify each line has correct format: DATE TEXT
        for line in lines:
            parts = line.split(' ', 1)  # Split on first space only
            assert len(parts) == 2, f"Line should have date and text: {line}"
            # Verify date format (YYYY-MM-DD)
            date_part = parts[0]
            assert len(date_part) == 10, f"Date should be YYYY-MM-DD format: {date_part}"
            assert date_part[4] == '-' and date_part[7] == '-', f"Invalid date format: {date_part}"

class TestJotErrorHandling:
    """
    Tests for error handling and edge cases.
    
    STUDENT NOTE: These tests verify the program handles unusual situations gracefully
    """
    
    def test_very_long_input(self, monkeypatch, tmp_path):
        """
        Test jot with very long user input.
        
        EDUCATIONAL FOCUS: Handling edge cases in user input
        """
        # Create a very long string
        long_text = "A" * 1000 + " This is a very long jot entry " + "B" * 1000
        
        monkeypatch.setattr('builtins.input', lambda prompt: long_text)
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        
        # Verify the long text is properly saved
        assert long_text in file_content
        assert file_content.startswith("2023-01-01 ")
        assert file_content.endswith("\n")
    
    def test_newlines_in_input(self, monkeypatch, tmp_path):
        """
        Test how jot handles input containing newline characters.
        
        STUDENT NOTE: Tests what happens with multi-line input
        """
        multiline_text = "First line\nSecond line\nThird line"
        
        monkeypatch.setattr('builtins.input', lambda prompt: multiline_text)
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        
        # Verify the multiline text is preserved
        expected_content = f"2023-01-01 {multiline_text}\n"
        assert file_content == expected_content
    
    def test_unicode_and_emoji_input(self, monkeypatch, tmp_path):
        """
        Test jot with Unicode characters and emojis.
        
        STUDENT NOTE: Modern applications should handle international text
        """
        unicode_text = "Hello 世界! 🌍 Café naïve résumé"
        
        monkeypatch.setattr('builtins.input', lambda prompt: unicode_text)
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text(encoding='utf-8')
        
        expected_content = f"2023-01-01 {unicode_text}\n"
        assert file_content == expected_content

class TestJotAlternativeMockingApproaches:
    """
    Alternative mocking approaches for educational comparison.
    
    STUDENT NOTE: This shows different ways to achieve the same mocking goals
    """
    
    def test_with_patch_decorator(self, tmp_path):
        """
        Example using @patch decorator instead of monkeypatch.
        
        EDUCATIONAL COMPARISON: Shows patch decorator vs monkeypatch
        STUDENT NOTE: Both approaches work, but monkeypatch is often cleaner
        """
        with patch('builtins.input', return_value='Patch decorator test'):
            with patch('jot.date.today', return_value=date(2023, 1, 1)):
                with patch('jot.Path.home', return_value=tmp_path):
                    main()
        
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        assert file_content == "2023-01-01 Patch decorator test\n"
    
    def test_with_context_manager_mocking(self, tmp_path):
        """
        Example using context managers for mocking.
        
        EDUCATIONAL COMPARISON: Shows context manager approach
        STUDENT NOTE: Useful when you need mocks for only part of a test
        """
        # Using patch as context manager
        with patch('builtins.input') as mock_input, \
             patch('jot.date.today') as mock_today, \
             patch('jot.Path.home') as mock_home:
            
            # Set up mock return values
            mock_input.return_value = 'Context manager test'
            mock_today.return_value = date(2023, 2, 2)
            mock_home.return_value = tmp_path
            
            main()
        
        test_jot_file = tmp_path / "jot.txt"
        file_content = test_jot_file.read_text()
        assert file_content == "2023-02-02 Context manager test\n"

class TestJotFileSystemBehavior:
    """
    Tests focusing on file system interactions.
    
    STUDENT NOTE: These tests verify proper file handling
    """
    
    def test_creates_file_if_not_exists(self, monkeypatch, tmp_path):
        """
        Test that jot creates the file if it doesn't exist.
        
        EDUCATIONAL FOCUS: File creation behavior
        """
        monkeypatch.setattr('builtins.input', lambda prompt: 'First entry')
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        test_jot_file = tmp_path / "jot.txt"
        
        # Verify file doesn't exist initially
        assert not test_jot_file.exists()
        
        main()
        
        # Verify file was created
        assert test_jot_file.exists()
        assert test_jot_file.is_file()
    
    def test_file_encoding_handling(self, monkeypatch, tmp_path):
        """
        Test that the file is written with proper encoding.
        
        STUDENT NOTE: Important for international character support
        """
        test_text = "Encoding test: àáâãäå æç èéêë ìíîï ñ òóôõö ùúûü ý"
        
        monkeypatch.setattr('builtins.input', lambda prompt: test_text)
        monkeypatch.setattr('jot.date.today', lambda: date(2023, 1, 1))
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        main()
        
        test_jot_file = tmp_path / "jot.txt"
        
        # Test reading with explicit encoding
        file_content = test_jot_file.read_text(encoding='utf-8')
        assert test_text in file_content
        
        # Test that file is readable with default encoding too
        file_content_default = test_jot_file.read_text()
        assert test_text in file_content_default

class TestJotDocumentationExamples:
    """
    Examples that serve as documentation for students.
    
    STUDENT NOTE: These are complete examples you can use as templates
    """
    
    def test_complete_example_template(self, monkeypatch, tmp_path):
        """
        DOCUMENTATION EXAMPLE: Complete test template for jot functionality.
        
        This example shows the standard pattern for testing jot:
        1. Mock user input
        2. Mock current date  
        3. Mock file path to use tmp_path
        4. Run main()
        5. Verify file contents
        
        STUDENT NOTE: Copy this pattern for your own jot tests
        """
        # Step 1: Mock user input
        test_input = "This is my jot entry"
        monkeypatch.setattr('builtins.input', lambda prompt: test_input)
        
        # Step 2: Mock current date
        test_date = date(2023, 7, 15)
        monkeypatch.setattr('jot.date.today', lambda: test_date)
        
        # Step 3: Mock file path to use temporary directory
        monkeypatch.setattr('jot.Path.home', lambda: tmp_path)
        
        # Step 4: Run the function
        main()
        
        # Step 5: Verify file contents
        jot_file = tmp_path / "jot.txt"
        assert jot_file.exists()
        
        content = jot_file.read_text()
        expected = "2023-07-15 This is my jot entry\n"
        assert content == expected
        
        # Additional verification examples:
        assert content.startswith("2023-07-15 ")
        assert content.endswith("\n")
        assert "This is my jot entry" in content

if __name__ == "__main__":
    pytest.main([__file__, "-v"])