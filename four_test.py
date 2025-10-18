# four_test.py
import pytest
import sys
from unittest.mock import patch

# Import the functions we're testing
from four import number_to_word, main

class TestNumberToWord:
    """Tests for the number_to_word function."""
    
    @pytest.mark.parametrize("number,expected_word", [
        (0, 'zero'),
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
        (6, 'six'),
        (7, 'seven'),
        (8, 'eight'),
        (9, 'nine'),
    ])
    def test_number_to_word_all_digits(self, number, expected_word):
        """
        Test number_to_word function with all single digits.
        
        PYTEST FEATURE: Parametrized testing for comprehensive coverage
        BENEFIT: Test all valid inputs systematically
        """
        result = number_to_word(number)
        assert result == expected_word
    
    def test_number_to_word_invalid_input(self):
        """Test number_to_word with invalid input (out of range)."""
        with pytest.raises(IndexError):
            number_to_word(10)
        
        with pytest.raises(IndexError):
            number_to_word(-1)

class TestMainFunctionWithMonkeypatch:
    """
    Tests for the main function using monkeypatch.setattr.
    
    STUDENT NOTE: monkeypatch.setattr is the most effective method here because:
    1. It's built into pytest (no external dependencies)
    2. It provides automatic cleanup
    3. It's more understandable - clearly shows what's being mocked
    4. It's simpler for this use case than complex mock objects
    """
    
    def test_starting_with_zero(self, monkeypatch, capsys):
        """
        Test the program starting with 0.
        
        PYTEST FEATURE: Using monkeypatch.setattr to mock sys.argv
        BENEFIT: Clean, understandable way to simulate command-line arguments
        STUDENT NOTE: monkeypatch automatically restores sys.argv after test
        """
        # Mock command-line arguments: four.py 0
        monkeypatch.setattr(sys, 'argv', ['four.py', '0'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word zero has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_one(self, monkeypatch, capsys):
        """Test the program starting with 1."""
        # Mock command-line arguments: four.py 1
        monkeypatch.setattr(sys, 'argv', ['four.py', '1'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word one has 3 letters in it.\n"
            "The word three has 5 letters in it.\n"
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_two(self, monkeypatch, capsys):
        """Test the program starting with 2."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '2'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word two has 3 letters in it.\n"
            "The word three has 5 letters in it.\n"
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_three(self, monkeypatch, capsys):
        """Test the program starting with 3."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '3'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word three has 5 letters in it.\n"
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_four(self, monkeypatch, capsys):
        """Test the program starting with 4 (immediate termination)."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '4'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_five(self, monkeypatch, capsys):
        """Test the program starting with 5."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '5'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_six(self, monkeypatch, capsys):
        """Test the program starting with 6."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '6'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word six has 3 letters in it.\n"
            "The word three has 5 letters in it.\n"
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_seven(self, monkeypatch, capsys):
        """Test the program starting with 7."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '7'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word seven has 5 letters in it.\n"
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_eight(self, monkeypatch, capsys):
        """Test the program starting with 8."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '8'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word eight has 5 letters in it.\n"
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""
    
    def test_starting_with_nine(self, monkeypatch, capsys):
        """Test the program starting with 9."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '9'])
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word nine has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output
        assert captured.err == ""

class TestMainFunctionParametrized:
    """
    Parametrized tests for comprehensive validation of starting numbers.
    
    PYTEST FEATURE: Parametrized testing with complex expected outputs
    BENEFIT: Test variety of starting numbers systematically
    STUDENT NOTE: Each parameter set tests the complete logic chain
    """
    
    @pytest.mark.parametrize("start_number,expected_sequence", [
        (0, ["zero", "four"]),
        (1, ["one", "three", "five", "four"]),
        (2, ["two", "three", "five", "four"]),
        (3, ["three", "five", "four"]),
        (4, ["four"]),
        (5, ["five", "four"]),
        (6, ["six", "three", "five", "four"]),
        (7, ["seven", "five", "four"]),
        (8, ["eight", "five", "four"]),
        (9, ["nine", "four"]),
    ])
    def test_logic_sequences(self, monkeypatch, capsys, start_number, expected_sequence):
        """
        Test the complete logic sequence for each starting number.
        
        PYTEST FEATURE: Complex parametrized testing
        BENEFIT: Validates the entire algorithm logic chain
        STUDENT NOTE: This verifies the mathematical progression of the algorithm
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        
        # Build expected output
        expected_lines = []
        for word in expected_sequence:
            letter_count = len(word)
            expected_lines.append(f"The word {word} has {letter_count} letters in it.")
        expected_lines.append("Done.")
        expected_output = "\n".join(expected_lines) + "\n"
        
        assert captured.out == expected_output
        assert captured.err == ""
    
    @pytest.mark.parametrize("start_number,steps_to_four", [
        (0, 2),  # zero -> four
        (1, 4),  # one -> three -> five -> four
        (2, 4),  # two -> three -> five -> four
        (3, 3),  # three -> five -> four
        (4, 1),  # four (immediate)
        (5, 2),  # five -> four
        (6, 4),  # six -> three -> five -> four
        (7, 3),  # seven -> five -> four
        (8, 3),  # eight -> five -> four
        (9, 2),  # nine -> four
    ])
    def test_steps_to_convergence(self, monkeypatch, capsys, start_number, steps_to_four):
        """
        Test that each number converges to 4 in the expected number of steps.
        
        PYTEST FEATURE: Algorithm verification through step counting
        BENEFIT: Validates the convergence property of the algorithm
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        
        # Count the number of lines (excluding "Done.")
        lines = captured.out.strip().split('\n')
        word_lines = [line for line in lines if line.startswith("The word")]
        
        assert len(word_lines) == steps_to_four

class TestArgsFixtureAlternative:
    """
    Alternative implementation using a custom args fixture.
    
    STUDENT NOTE: This shows how you could create a custom fixture,
    but monkeypatch.setattr is simpler and more understandable for this case.
    """
    
    @pytest.fixture
    def args(self, monkeypatch):
        """
        Custom fixture to set command-line arguments.
        
        PYTEST FEATURE: Custom fixture for argument management
        BENEFIT: Encapsulates argument setting logic
        STUDENT NOTE: While possible, monkeypatch.setattr is more direct
        """
        def _set_args(number):
            monkeypatch.setattr(sys, 'argv', ['four.py', str(number)])
        return _set_args
    
    def test_with_custom_args_fixture(self, args, capsys):
        """
        Example test using the custom args fixture.
        
        COMPARISON: This approach works but is less clear than direct monkeypatch use
        STUDENT NOTE: Direct monkeypatch.setattr is more understandable
        """
        args(5)
        
        main()
        
        captured = capsys.readouterr()
        expected_output = (
            "The word five has 4 letters in it.\n"
            "The word four has 4 letters in it.\n"
            "Done.\n"
        )
        assert captured.out == expected_output

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_invalid_command_line_args(self, monkeypatch):
        """Test behavior with invalid command-line arguments."""
        # Test with non-numeric argument
        monkeypatch.setattr(sys, 'argv', ['four.py', 'abc'])
        
        with pytest.raises(ValueError):
            main()
    
    def test_missing_command_line_args(self, monkeypatch):
        """Test behavior with missing command-line arguments."""
        # Test with no arguments
        monkeypatch.setattr(sys, 'argv', ['four.py'])
        
        with pytest.raises(IndexError):
            main()
    
    def test_out_of_range_number(self, monkeypatch):
        """Test behavior with out-of-range numbers."""
        # Test with number > 9
        monkeypatch.setattr(sys, 'argv', ['four.py', '10'])
        
        with pytest.raises(IndexError):
            main()
        
        # Test with negative number
        monkeypatch.setattr(sys, 'argv', ['four.py', '-1'])
        
        with pytest.raises(IndexError):
            main()

class TestOutputFormat:
    """Test exact output formatting and edge cases."""
    
    def test_exact_output_format_four(self, monkeypatch, capsys):
        """Test exact output format when starting with 4."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '4'])
        
        main()
        
        captured = capsys.readouterr()
        
        # Verify exact format including spacing and punctuation
        lines = captured.out.strip().split('\n')
        assert lines[0] == "The word four has 4 letters in it."
        assert lines[1] == "Done."
        assert len(lines) == 2
    
    def test_no_stderr_output(self, monkeypatch, capsys):
        """Test that no error output is produced during normal operation."""
        test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for number in test_numbers:
            monkeypatch.setattr(sys, 'argv', ['four.py', str(number)])
            
            main()
            
            captured = capsys.readouterr()
            assert captured.err == "", f"Unexpected stderr for input {number}"
    
    def test_output_ends_with_done(self, monkeypatch, capsys):
        """Test that all executions end with 'Done.'"""
        test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for number in test_numbers:
            monkeypatch.setattr(sys, 'argv', ['four.py', str(number)])
            
            main()
            
            captured = capsys.readouterr()
            lines = captured.out.strip().split('\n')
            assert lines[-1] == "Done.", f"Output for {number} doesn't end with 'Done.'"
    
    def test_letter_count_accuracy(self, monkeypatch, capsys):
        """Test that letter counts in output are accurate."""
        monkeypatch.setattr(sys, 'argv', ['four.py', '1'])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # Verify each line has correct letter count
        # "The word one has 3 letters in it."
        assert "one has 3 letters" in lines[0]
        # "The word three has 5 letters in it."
        assert "three has 5 letters" in lines[1]
        # "The word five has 4 letters in it."
        assert "five has 4 letters" in lines[2]
        # "The word four has 4 letters in it."
        assert "four has 4 letters" in lines[3]

class TestAlgorithmProperties:
    """Test mathematical properties of the algorithm."""
    
    def test_all_numbers_converge_to_four(self, monkeypatch, capsys):
        """
        Test that all single digits eventually converge to 4.
        
        PYTEST FEATURE: Comprehensive algorithm validation
        BENEFIT: Proves the mathematical property of the algorithm
        STUDENT NOTE: This tests the fundamental theorem of this algorithm
        """
        for start_number in range(10):
            monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
            
            main()
            
            captured = capsys.readouterr()
            
            # Verify that output contains "four has 4 letters"
            assert "The word four has 4 letters in it." in captured.out
            # Verify that output ends with "Done."
            assert captured.out.endswith("Done.\n")
    
    def test_convergence_within_reasonable_steps(self, monkeypatch, capsys):
        """Test that convergence happens within a reasonable number of steps."""
        max_expected_steps = 5  # Based on algorithm analysis
        
        for start_number in range(10):
            monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
            
            main()
            
            captured = capsys.readouterr()
            lines = captured.out.strip().split('\n')
            word_lines = [line for line in lines if line.startswith("The word")]
            
            assert len(word_lines) <= max_expected_steps, \
                f"Number {start_number} took too many steps: {len(word_lines)}"
    
    def test_four_is_fixed_point(self, monkeypatch, capsys):
        """
        Test that 4 is a fixed point (converges immediately).
        
        PYTEST FEATURE: Fixed point verification
        BENEFIT: Validates the termination condition
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', '4'])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # Should have exactly 2 lines: the four statement and Done
        assert len(lines) == 2
        assert lines[0] == "The word four has 4 letters in it."
        assert lines[1] == "Done."

class TestRealWorldUsage:
    """Test real-world usage scenarios."""
    
    def test_command_line_simulation(self, monkeypatch, capsys):
        """
        Test that simulates actual command-line usage.
        
        PYTEST FEATURE: Real-world scenario testing
        BENEFIT: Tests the program as users would actually run it
        """
        # Simulate: python four.py 7
        monkeypatch.setattr(sys, 'argv', ['four.py', '7'])
        
        main()
        
        captured = capsys.readouterr()
        
        # Verify the complete expected sequence
        expected_lines = [
            "The word seven has 5 letters in it.",
            "The word five has 4 letters in it.",
            "The word four has 4 letters in it.",
            "Done."
        ]
        actual_lines = captured.out.strip().split('\n')
        
        assert actual_lines == expected_lines
    
    @pytest.mark.parametrize("input_as_string", [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ])
    def test_string_to_int_conversion(self, monkeypatch, capsys, input_as_string):
        """
        Test that string command-line arguments are properly converted to integers.
        
        PYTEST FEATURE: Input conversion testing
        BENEFIT: Ensures robust handling of command-line input
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', input_as_string])
        
        # Should not raise any exceptions
        main()
        
        captured = capsys.readouterr()
        # Should produce output and end with Done
        assert captured.out.endswith("Done.\n")
        assert "letters in it." in captured.out

class TestPerformanceAndMemory:
    """Test performance characteristics (simple validation)."""
    
    def test_no_infinite_loops(self, monkeypatch, capsys):
        """
        Test that the algorithm terminates for all valid inputs.
        
        PYTEST FEATURE: Termination testing
        BENEFIT: Ensures the algorithm doesn't hang
        STUDENT NOTE: This is crucial for algorithm correctness
        """
        import time
        
        for start_number in range(10):
            monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
            
            start_time = time.time()
            main()
            end_time = time.time()
            
            # Should complete very quickly (under 1 second)
            execution_time = end_time - start_time
            assert execution_time < 1.0, f"Number {start_number} took too long: {execution_time}s"
    
    def test_reasonable_output_length(self, monkeypatch, capsys):
        """Test that output length is reasonable for all inputs."""
        for start_number in range(10):
            monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
            
            main()
            
            captured = capsys.readouterr()
            
            # Output should be reasonable length (not excessive)
            assert len(captured.out) < 1000, f"Output too long for {start_number}"
            # But should have some content
            assert len(captured.out) > 10, f"Output too short for {start_number}"

class TestIntegrationScenarios:
    """Integration tests combining multiple aspects."""
    
    def test_complete_workflow_validation(self, monkeypatch, capsys):
        """
        Complete workflow test validating all aspects together.
        
        PYTEST FEATURE: Integration testing
        BENEFIT: Tests the entire program workflow
        """
        # Test a complex case (starting with 1)
        monkeypatch.setattr(sys, 'argv', ['four.py', '1'])
        
        main()
        
        captured = capsys.readouterr()
        
        # Validate multiple aspects simultaneously
        lines = captured.out.strip().split('\n')
        
        # Correct number of lines
        assert len(lines) == 5  # 4 word lines + Done
        
        # Correct sequence
        expected_words = ['one', 'three', 'five', 'four']
        for i, expected_word in enumerate(expected_words):
            assert expected_word in lines[i]
        
        # Correct letter counts
        assert "one has 3 letters" in lines[0]
        assert "three has 5 letters" in lines[1]
        assert "five has 4 letters" in lines[2]
        assert "four has 4 letters" in lines[3]
        
        # Proper termination
        assert lines[4] == "Done."
        
        # No errors
        assert captured.err == ""

if __name__ == "__main__":
    pytest.main([__file__, "-v"])