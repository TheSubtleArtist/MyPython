# dollars_test_refactored.py
'''
Key Improvements Through Parametrization:
Original vs. Refactored Test Count:
Original: ~35+ individual test methods
Refactored: 8 parametrized test methods covering the same scenarios
Benefits of This Refactoring:
✅ Massive Reduction in Code:

Consolidated similar tests into parametrized groups
Eliminated repetitive test code
Maintained comprehensive coverage
✅ Better Organization:

TestFormatDollars : All format_dollars testing in one parametrized method
TestMainFunctionValid : All valid main() scenarios together
TestMainFunctionInvalid : All invalid input scenarios together
TestErrorMessages : Consolidated error message verification
✅ Enhanced Readability:

Added description parameter to make test failures more understandable
Clear parameter names that explain what's being tested
Logical grouping of related test cases
✅ Easier Maintenance:

Adding new test cases is just adding a new parameter tuple
Changes to test logic only need to be made in one place
Consistent test patterns across all scenarios
✅ Student-Friendly Features:

Clear documentation explaining the parametrization benefits
Descriptive parameter names and comments
Backwards compatibility section preserving original test cases
What Was Consolidated:
12 individual format_dollars tests → 1 parametrized test with 23 scenarios
8 main function valid input tests → 1 parametrized test with 20 scenarios
13 invalid input tests → 2 parametrized tests (by error type)
Multiple error message tests → 1 parametrized test
Edge case tests → Integrated into main parametrized tests
This refactoring demonstrates how @pytest.mark.parametrize can dramatically reduce test code while maintaining (and often improving) test coverage and readability.
'''
import pytest
import sys
from unittest.mock import patch

# Import the functions we're testing
from dollars import format_dollars, main

# Custom fixture to control command-line arguments
@pytest.fixture
def args(monkeypatch):
    """
    PYTEST FEATURE: Custom fixture for controlling command-line arguments
    BENEFIT: Reusable way to set sys.argv for testing main() function
    STUDENT NOTE: This fixture uses monkeypatch to safely modify sys.argv
    """
    def _set_args(arg_list):
        """Set sys.argv to the provided argument list."""
        full_args = ["dollars.py"] + arg_list
        monkeypatch.setattr(sys, 'argv', full_args)
    return _set_args

class TestFormatDollars:
    """Consolidated tests for the format_dollars function using parametrize."""
    
    @pytest.mark.parametrize("amount,expected,description", [
        # Basic amounts
        (0, "$0.00", "zero amount"),
        (1, "$1.00", "simple integer"),
        (10, "$10.00", "double digit"),
        (100, "$100.00", "hundreds"),
        (1000, "$1000.00", "thousands"),
        
        # Decimal amounts
        (0.01, "$0.01", "smallest cent"),
        (0.99, "$0.99", "under dollar"),
        (123.45, "$123.45", "standard decimal"),
        (9999.99, "$9999.99", "large decimal"),
        
        # Rounding scenarios
        (999.999, "$1000.00", "round up to next dollar"),
        (123.456, "$123.46", "round up cents"),
        (123.454, "$123.45", "round down cents"),
        (1.005, "$1.01", "banker's rounding up"),
        (1.004, "$1.00", "round down"),
        (2.995, "$3.00", "round up to dollar"),
        (2.994, "$2.99", "round down from dollar"),
        
        # Negative amounts
        (-1, "$-1.00", "negative integer"),
        (-123.45, "$-123.45", "negative decimal"),
        (-0.01, "$-0.01", "negative cent"),
        
        # Large amounts
        (1000000, "$1000000.00", "million"),
        (999999999.99, "$999999999.99", "very large amount"),
        
        # Precision edge cases
        (0.1, "$0.10", "floating point 0.1"),
        (0.2, "$0.20", "floating point 0.2"),
        (0.30000000000000004, "$0.30", "floating point precision"),
    ])
    def test_format_dollars_comprehensive(self, amount, expected, description):
        """
        PYTEST FEATURE: Comprehensive parametrized testing
        BENEFIT: All format_dollars scenarios in one test with descriptions
        STUDENT NOTE: Description parameter makes test failures easier to understand
        """
        result = format_dollars(amount)
        assert result == expected, f"Failed for {description}: {amount}"

class TestMainFunctionValid:
    """Consolidated tests for main function with valid inputs."""
    
    @pytest.mark.parametrize("input_str,expected_output,description", [
        # Integer inputs
        ("0", "$0.00\n", "zero"),
        ("1", "$1.00\n", "simple integer"),
        ("100", "$100.00\n", "hundreds"),
        ("42", "$42.00\n", "integer without decimal"),
        
        # Float inputs
        ("123.45", "$123.45\n", "standard decimal"),
        ("10.5", "$10.50\n", "single decimal place"),
        ("100.99", "$100.99\n", "ninety-nine cents"),
        ("0.01", "$0.01\n", "smallest amount"),
        ("999999.99", "$999999.99\n", "large amount"),
        
        # Negative inputs
        ("-50.25", "$-50.25\n", "negative amount"),
        ("-25.75", "$-25.75\n", "negative decimal"),
        
        # Special numeric formats
        ("1e2", "$100.00\n", "scientific notation"),
        ("+50.25", "$50.25\n", "explicit positive sign"),
        ("0050.25", "$50.25\n", "leading zeros"),
        ("50.250", "$50.25\n", "trailing zeros"),
        
        # Rounding cases
        ("0.001", "$0.00\n", "round down to zero"),
        ("99.999", "$100.00\n", "round up to hundred"),
        ("1.234", "$1.23\n", "round down cents"),
        ("1.235", "$1.24\n", "banker's rounding up"),
        ("1.236", "$1.24\n", "round up cents"),
        ("2.344", "$2.34\n", "round down"),
        ("2.345", "$2.35\n", "banker's rounding"),
        ("2.346", "$2.35\n", "round up"),
    ])
    def test_main_valid_inputs(self, args, capsys, input_str, expected_output, description):
        """
        PYTEST FEATURE: Parametrized test covering all valid main function scenarios
        BENEFIT: Comprehensive testing with clear descriptions for debugging
        STUDENT NOTE: Combines command-line testing with output verification
        """
        args([input_str])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == expected_output, f"Failed for {description}: {input_str}"
        assert captured.err == "", f"Unexpected error output for {description}"

class TestMainFunctionInvalid:
    """Consolidated tests for main function with invalid inputs."""
    
    @pytest.mark.parametrize("invalid_input,description", [
        # Non-numeric strings
        ("abc", "alphabetic string"),
        ("hello world", "multiple words"),
        ("fifty", "spelled out number"),
        ("", "empty string"),
        
        # Invalid numeric formats
        ("12.34.56", "multiple decimal points"),
        ("$100", "dollar sign prefix"),
        ("50%", "percentage sign"),
        ("1,000.50", "comma separator"),
        ("100.50.25", "multiple decimals"),
        (".", "decimal point only"),
        
        # Special values
        ("NaN", "not a number"),
        ("inf", "infinity"),
        ("-inf", "negative infinity"),
        ("null", "null string"),
        ("true", "boolean string"),
        ("false", "boolean string"),
    ])
    def test_main_invalid_inputs(self, args, invalid_input, description):
        """
        PYTEST FEATURE: Parametrized testing for all invalid inputs
        BENEFIT: Systematic testing of error conditions
        STUDENT NOTE: Verifies argparse properly rejects invalid inputs
        """
        args([invalid_input])
        with pytest.raises(SystemExit), pytest.warns(None) as warning_list:
            main()
        # Verify no unexpected warnings
        assert len(warning_list) == 0, f"Unexpected warnings for {description}"
    
    @pytest.mark.parametrize("arg_count,test_args,description", [
        (0, [], "no arguments"),
        (2, ["100", "200"], "too many arguments"),
        (3, ["100", "200", "300"], "way too many arguments"),
    ])
    def test_main_argument_count_errors(self, args, arg_count, test_args, description):
        """
        PYTEST FEATURE: Parametrized testing for argument count errors
        BENEFIT: Tests different argument count scenarios systematically
        STUDENT NOTE: Verifies argparse handles wrong number of arguments
        """
        args(test_args)
        with pytest.raises(SystemExit):
            main()

class TestErrorMessages:
    """Consolidated tests for error message verification."""
    
    @pytest.mark.parametrize("invalid_input,expected_error_keywords", [
        ("invalid", ["invalid", "error"]),
        ("abc", ["invalid", "error", "float"]),
        ("$100", ["invalid", "error"]),
        ("", ["invalid", "error"]),
    ])
    def test_error_messages_contain_keywords(self, args, capsys, invalid_input, expected_error_keywords):
        """
        PYTEST FEATURE: Parametrized error message testing
        BENEFIT: Verifies error messages contain helpful information
        STUDENT NOTE: Checks that users get meaningful error feedback
        """
        args([invalid_input])
        
        with pytest.raises(SystemExit):
            main()
        
        captured = capsys.readouterr()
        error_text = captured.err.lower()
        
        # At least one of the expected keywords should be present
        assert any(keyword in error_text for keyword in expected_error_keywords), \
            f"Error message '{captured.err}' should contain one of {expected_error_keywords}"
    
    def test_missing_argument_error_message(self, args, capsys):
        """Test error message when no argument is provided."""
        args([])
        
        with pytest.raises(SystemExit):
            main()
        
        captured = capsys.readouterr()
        error_text = captured.err.lower()
        assert "required" in error_text or "argument" in error_text, \
            f"Missing argument error should mention 'required' or 'argument': {captured.err}"

class TestSpecialFeatures:
    """Tests for special ArgumentParser features."""
    
    @pytest.mark.parametrize("special_arg,expected_exit_code,output_location", [
        ("--help", 0, "out"),  # Help goes to stdout and exits with 0
        ("-h", 0, "out"),      # Short help flag
    ])
    def test_special_arguments(self, args, capsys, special_arg, expected_exit_code, output_location):
        """
        PYTEST FEATURE: Parametrized testing for special arguments
        BENEFIT: Tests help and other special flags systematically
        STUDENT NOTE: ArgumentParser provides built-in help functionality
        """
        args([special_arg])
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == expected_exit_code
        
        captured = capsys.readouterr()
        if output_location == "out":
            assert "usage:" in captured.out.lower()
        else:
            assert "usage:" in captured.err.lower()

class TestBackwardsCompatibility:
    """Tests to ensure backwards compatibility with original test."""
    
    @pytest.mark.parametrize("amount,expected", [
        (80, "$80.00"),      # From original test_dollars()
        (3.048, "$3.05"),    # From original test_dollars() 
        (0.05, "$0.05"),     # From original test_dollars()
    ])
    def test_original_scenarios(self, amount, expected):
        """
        PYTEST FEATURE: Ensuring backwards compatibility
        BENEFIT: Maintains compatibility with original test cases
        STUDENT NOTE: These are the exact cases from the original dollars_test.py
        """
        assert format_dollars(amount) == expected, "Original test case compatibility"

class TestIntegrationScenarios:
    """Integration tests combining multiple aspects."""
    
    @pytest.mark.parametrize("scenario_name,input_value,verify_output,verify_no_error", [
        ("typical_usage", "25.50", "$25.50\n", True),
        ("zero_dollars", "0", "$0.00\n", True),
        ("large_amount", "1000000", "$1000000.00\n", True),
        ("precise_rounding", "123.456", "$123.46\n", True),
        ("negative_amount", "-50", "$-50.00\n", True),
    ])
    def test_end_to_end_scenarios(self, args, capsys, scenario_name, input_value, verify_output, verify_no_error):
        """
        PYTEST FEATURE: End-to-end integration testing
        BENEFIT: Tests complete workflow from command-line to output
        STUDENT NOTE: This simulates real user interactions with the program
        """
        args([input_value])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == verify_output, f"Failed end-to-end test: {scenario_name}"
        
        if verify_no_error:
            assert captured.err == "", f"Unexpected error in scenario: {scenario_name}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])