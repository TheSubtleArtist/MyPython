# test_dollars.py
import pytest
import sys
from unittest.mock import patch
from argparse import ArgumentParser

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
    """Tests for the format_dollars function."""
    
    @pytest.mark.parametrize("amount,expected", [
        (0, "$0.00"),
        (1, "$1.00"),
        (10, "$10.00"),
        (100, "$100.00"),
        (1000, "$1000.00"),
        (9999.99, "$9999.99"),
        (0.01, "$0.01"),
        (0.99, "$0.99"),
        (123.45, "$123.45"),
        (999.999, "$1000.00"),  # Should round up
        (123.456, "$123.46"),   # Should round up
        (123.454, "$123.45"),   # Should round down
    ])
    def test_format_dollars_various_amounts(self, amount, expected):
        """
        PYTEST FEATURE: Parametrized testing with various dollar amounts
        BENEFIT: Test many scenarios efficiently in one test function
        STUDENT NOTE: Each parameter set creates a separate test case
        """
        result = format_dollars(amount)
        assert result == expected
    
    def test_format_dollars_negative_amounts(self):
        """Test format_dollars with negative amounts."""
        assert format_dollars(-1) == "$-1.00"
        assert format_dollars(-123.45) == "$-123.45"
        assert format_dollars(-0.01) == "$-0.01"
    
    def test_format_dollars_very_large_amounts(self):
        """Test format_dollars with very large amounts."""
        assert format_dollars(1000000) == "$1000000.00"
        assert format_dollars(999999999.99) == "$999999999.99"
    
    def test_format_dollars_precision_rounding(self):
        """Test format_dollars rounding behavior with high precision inputs."""
        # Test various rounding scenarios
        assert format_dollars(1.005) == "$1.01"  # Round up
        assert format_dollars(1.004) == "$1.00"  # Round down
        assert format_dollars(2.995) == "$3.00"  # Round up
        assert format_dollars(2.994) == "$2.99"  # Round down

class TestMainFunctionWithArgs:
    """Tests for the main function using the args fixture."""
    
    def test_main_with_valid_integer(self, args, capsys):
        """
        PYTEST FEATURE: Using custom fixture with capsys
        BENEFIT: Test command-line interface with controlled arguments and output capture
        STUDENT NOTE: args fixture sets command line, capsys captures printed output
        """
        args(["100"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$100.00\n"
        assert captured.err == ""
    
    def test_main_with_valid_float(self, args, capsys):
        """Test main function with float input."""
        args(["123.45"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$123.45\n"
        assert captured.err == ""
    
    def test_main_with_zero(self, args, capsys):
        """Test main function with zero amount."""
        args(["0"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$0.00\n"
        assert captured.err == ""
    
    def test_main_with_negative_amount(self, args, capsys):
        """Test main function with negative amount."""
        args(["-50.25"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$-50.25\n"
        assert captured.err == ""
    
    def test_main_with_very_small_amount(self, args, capsys):
        """Test main function with very small decimal amount."""
        args(["0.01"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$0.01\n"
        assert captured.err == ""
    
    def test_main_with_large_amount(self, args, capsys):
        """Test main function with large amount."""
        args(["999999.99"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$999999.99\n"
        assert captured.err == ""
    
    @pytest.mark.parametrize("amount_str,expected_output", [
        ("0", "$0.00\n"),
        ("1", "$1.00\n"),
        ("10.5", "$10.50\n"),
        ("100.99", "$100.99\n"),
        ("1000", "$1000.00\n"),
        ("-25.75", "$-25.75\n"),
        ("0.001", "$0.00\n"),  # Should round to nearest cent
        ("99.999", "$100.00\n"),  # Should round up
    ])
    def test_main_various_amounts_parametrized(self, args, capsys, amount_str, expected_output):
        """
        PYTEST FEATURE: Parametrized test with fixtures
        BENEFIT: Test multiple scenarios with consistent setup and verification
        """
        args([amount_str])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == expected_output
        assert captured.err == ""

class TestInvalidInputs:
    """Tests for invalid inputs that should cause SystemExit."""
    
    def test_main_with_non_numeric_string(self, args):
        """
        PYTEST FEATURE: Testing SystemExit with pytest.raises
        BENEFIT: Verify that invalid inputs properly exit the program
        STUDENT NOTE: argparse raises SystemExit for invalid type conversions
        """
        args(["abc"])
        with pytest.raises(SystemExit):
            main()
    
    def test_main_with_empty_string(self, args):
        """Test main function with empty string argument."""
        args([""])
        with pytest.raises(SystemExit):
            main()
    
    def test_main_with_multiple_words(self, args):
        """Test main function with multiple word argument."""
        args(["not a number"])
        with pytest.raises(SystemExit):
            main()
    
    def test_main_with_special_characters(self, args):
        """Test main function with special characters."""
        args(["$100"])  # Dollar sign should cause failure
        with pytest.raises(SystemExit):
            main()
    
    def test_main_with_comma_separated_number(self, args):
        """Test main function with comma-separated number."""
        args(["1,000.50"])  # Comma should cause failure
        with pytest.raises(SystemExit):
            main()
    
    def test_main_with_percentage(self, args):
        """Test main function with percentage sign."""
        args(["50%"])
        with pytest.raises(SystemExit):
            main()
    
    def test_main_no_arguments(self, args):
        """
        PYTEST FEATURE: Testing missing required arguments
        BENEFIT: Verify argument parser handles missing inputs correctly
        """
        args([])  # No arguments provided
        with pytest.raises(SystemExit):
            main()
    
    def test_main_too_many_arguments(self, args):
        """Test main function with too many arguments."""
        args(["100", "200"])  # Too many arguments
        with pytest.raises(SystemExit):
            main()
    
    @pytest.mark.parametrize("invalid_input", [
        "abc",
        "12.34.56",
        "hello world", 
        "$50",
        "fifty",
        "1,000",
        "100.50.25",
        "NaN",
        "inf",
        "-inf",
        "null",
        "true",
        "false",
    ])
    def test_main_various_invalid_inputs(self, args, invalid_input):
        """
        PYTEST FEATURE: Parametrized test for multiple invalid inputs
        BENEFIT: Systematically test many invalid input scenarios
        """
        args([invalid_input])
        with pytest.raises(SystemExit):
            main()

class TestErrorMessages:
    """Tests to verify error messages for invalid inputs."""
    
    def test_invalid_input_error_message(self, args, capsys):
        """
        PYTEST FEATURE: Capturing stderr for error messages
        BENEFIT: Verify that helpful error messages are displayed
        STUDENT NOTE: capsys.readouterr() captures both stdout and stderr
        """
        args(["invalid"])
        
        with pytest.raises(SystemExit):
            main()
        
        captured = capsys.readouterr()
        # argparse writes error messages to stderr
        assert "invalid" in captured.err.lower() or "error" in captured.err.lower()
    
    def test_missing_argument_error_message(self, args, capsys):
        """Test error message when no argument is provided."""
        args([])
        
        with pytest.raises(SystemExit):
            main()
        
        captured = capsys.readouterr()
        # Should mention required argument
        assert "required" in captured.err.lower() or "argument" in captured.err.lower()

class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""
    
    def test_scientific_notation_input(self, args, capsys):
        """Test main function with scientific notation (should work)."""
        args(["1e2"])  # Should be parsed as 100.0
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$100.00\n"
    
    def test_positive_sign_input(self, args, capsys):
        """Test main function with explicit positive sign."""
        args(["+50.25"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$50.25\n"
    
    def test_leading_zeros(self, args, capsys):
        """Test main function with leading zeros."""
        args(["0050.25"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$50.25\n"
    
    def test_trailing_zeros_in_input(self, args, capsys):
        """Test main function with trailing zeros in decimal."""
        args(["50.250"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$50.25\n"
    
    def test_no_decimal_point(self, args, capsys):
        """Test main function with integer input (no decimal point)."""
        args(["42"])
        main()
        
        captured = capsys.readouterr()
        assert captured.out == "$42.00\n"
    
    def test_decimal_point_only(self, args):
        """Test main function with just a decimal point."""
        args(["."])
        with pytest.raises(SystemExit):
            main()
    
    def test_multiple_decimal_points(self, args):
        """Test main function with multiple decimal points."""
        args(["12.34.56"])
        with pytest.raises(SystemExit):
            main()

class TestFloatPrecisionAndRounding:
    """Tests specifically for float precision and rounding behavior."""
    
    def test_float_precision_edge_cases(self, args, capsys):
        """Test floating-point precision edge cases."""
        # Test case that might have floating-point precision issues
        args(["0.1"])
        main()
        captured = capsys.readouterr()
        assert captured.out == "$0.10\n"
        
        args(["0.2"])
        main()
        captured = capsys.readouterr()
        assert captured.out == "$0.20\n"
        
        # 0.1 + 0.2 = 0.30000000000000004 in floating point
        args(["0.30000000000000004"])
        main()
        captured = capsys.readouterr()
        assert captured.out == "$0.30\n"
    
    def test_rounding_behavior_detailed(self, args, capsys):
        """Test detailed rounding behavior at cent boundaries."""
        test_cases = [
            ("1.234", "$1.23"),  # Round down
            ("1.235", "$1.24"),  # Round up (banker's rounding)
            ("1.236", "$1.24"),  # Round up
            ("2.344", "$2.34"),  # Round down
            ("2.345", "$2.35"),  # Round up (banker's rounding)  
            ("2.346", "$2.35"),  # Round up
        ]
        
        for input_val, expected in test_cases:
            args([input_val])
            main()
            captured = capsys.readouterr()
            assert captured.out == f"{expected}\n"

class TestIntegrationWithArgumentParser:
    """Integration tests focusing on ArgumentParser behavior."""
    
    def test_help_message(self, args, capsys):
        """Test that help message is available."""
        args(["--help"])
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        # Help should exit with code 0
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        assert "usage:" in captured.out.lower()
    
    def test_version_if_available(self, args):
        """Test version argument if it exists (should fail gracefully if not)."""
        args(["--version"])
        
        # This might raise SystemExit regardless of whether version is implemented
        with pytest.raises(SystemExit):
            main()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])