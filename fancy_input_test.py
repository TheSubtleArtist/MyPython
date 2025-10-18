# fancy_input_test.py
import pytest
from unittest.mock import Mock, patch
from io import StringIO

# Import the function we're testing
from fancy_input import fancy_input

class TestFancyInputWithMockerPatch:
    """
    Tests using pytest-mock's mocker.patch functionality.
    
    STUDENT NOTE: These tests use the pytest-mock plugin which provides
    the 'mocker' fixture. Install with: pip install pytest-mock
    """
    
    def test_valid_input_first_try_mocker(self, mocker, capsys):
        """
        PYTEST FEATURE: Using mocker.patch to mock builtins.input
        BENEFIT: Clean, pytest-integrated mocking with automatic cleanup
        STUDENT NOTE: mocker.patch is part of pytest-mock plugin
        """
        # ANNOTATION: Using mocker.patch here
        mock_input = mocker.patch('builtins.input', return_value='42')
        
        def int_validator(value):
            return int(value)
        
        result = fancy_input("Enter a number:", int_validator)
        
        assert result == 42
        mock_input.assert_called_once_with("Enter a number: ")
        
        # Check no error message was printed
        captured = capsys.readouterr()
        assert "Please enter a valid response" not in captured.out
    
    def test_invalid_then_valid_input_mocker(self, mocker, capsys):
        """
        PYTEST FEATURE: Using mocker.patch with side_effect for multiple calls
        BENEFIT: Simulate multiple user inputs in sequence
        STUDENT NOTE: side_effect allows different return values for each call
        """
        # ANNOTATION: Using mocker.patch with side_effect here
        mock_input = mocker.patch('builtins.input', side_effect=['invalid', '25'])
        
        def int_validator(value):
            return int(value)
        
        result = fancy_input("Enter a number:", int_validator)
        
        assert result == 25
        assert mock_input.call_count == 2
        mock_input.assert_any_call("Enter a number: ")
        
        # Check error message was printed once
        captured = capsys.readouterr()
        assert "Please enter a valid response" in captured.out
    
    def test_multiple_invalid_attempts_mocker(self, mocker, capsys):
        """Test multiple invalid attempts before valid input using mocker."""
        # ANNOTATION: Using mocker.patch with multiple invalid inputs
        mock_input = mocker.patch(
            'builtins.input', 
            side_effect=['abc', 'xyz', '123.45', '100']
        )
        
        def int_validator(value):
            return int(value)
        
        result = fancy_input("Enter an integer:", int_validator)
        
        assert result == 100
        assert mock_input.call_count == 4
        
        # Check error messages were printed for each invalid attempt
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == 3  # Three invalid attempts
    
    def test_email_validation_mocker(self, mocker, capsys):
        """Test email validation using mocker.patch."""
        # ANNOTATION: Using mocker.patch for email validation scenario
        mock_input = mocker.patch(
            'builtins.input',
            side_effect=['invalid-email', 'test@example.com']
        )
        
        def email_validator(value):
            if '@' not in value:
                raise ValueError("Invalid email")
            return value
        
        result = fancy_input("Enter your email:", email_validator)
        
        assert result == "test@example.com"
        assert mock_input.call_count == 2
        
        captured = capsys.readouterr()
        assert "Please enter a valid response" in captured.out
    
    def test_custom_validator_exception_mocker(self, mocker, capsys):
        """Test custom validator with specific exception using mocker."""
        # ANNOTATION: Using mocker.patch to test custom exception handling
        mock_input = mocker.patch(
            'builtins.input',
            side_effect=['negative', '42']
        )
        
        def positive_int_validator(value):
            num = int(value)
            if num <= 0:
                raise ValueError("Must be positive")
            return num
        
        result = fancy_input("Enter a positive number:", positive_int_validator)
        
        assert result == 42
        assert mock_input.call_count == 2

class TestFancyInputWithMonkeypatch:
    """
    Tests using pytest's built-in monkeypatch fixture.
    
    STUDENT NOTE: monkeypatch is built into pytest core, no additional
    packages required. It's more verbose but gives fine-grained control.
    """
    
    def test_valid_input_first_try_monkeypatch(self, monkeypatch, capsys):
        """
        PYTEST FEATURE: Using monkeypatch.setattr to mock builtins.input
        BENEFIT: Built-in pytest functionality, no external dependencies
        STUDENT NOTE: monkeypatch.setattr is part of core pytest
        """
        # ANNOTATION: Using monkeypatch.setattr here
        monkeypatch.setattr('builtins.input', lambda prompt: '42')
        
        def int_validator(value):
            return int(value)
        
        result = fancy_input("Enter a number:", int_validator)
        
        assert result == 42
        
        # Check no error message was printed
        captured = capsys.readouterr()
        assert "Please enter a valid response" not in captured.out
    
    def test_invalid_then_valid_input_monkeypatch(self, monkeypatch, capsys):
        """
        PYTEST FEATURE: Using monkeypatch with iterator for multiple inputs
        BENEFIT: Demonstrate how to handle multiple calls with monkeypatch
        STUDENT NOTE: More manual setup compared to mocker.patch
        """
        # ANNOTATION: Using monkeypatch.setattr with iterator for multiple inputs
        inputs = iter(['invalid', '25'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def int_validator(value):
            return int(value)
        
        result = fancy_input("Enter a number:", int_validator)
        
        assert result == 25
        
        # Check error message was printed
        captured = capsys.readouterr()
        assert "Please enter a valid response" in captured.out
    
    def test_multiple_invalid_attempts_monkeypatch(self, monkeypatch, capsys):
        """Test multiple invalid attempts using monkeypatch."""
        # ANNOTATION: Using monkeypatch.setattr with iterator for sequence of inputs
        inputs = iter(['abc', 'xyz', '123.45', '100'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def int_validator(value):
            return int(value)
        
        result = fancy_input("Enter an integer:", int_validator)
        
        assert result == 100
        
        # Check error messages were printed for invalid attempts
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == 3
    
    def test_age_validation_monkeypatch(self, monkeypatch, capsys):
        """Test age validation using monkeypatch."""
        # ANNOTATION: Using monkeypatch.setattr for age validation scenario
        inputs = iter(['abc', '-5', '200', '25'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def age_validator(value):
            age = int(value)
            if age < 0 or age > 150:
                raise ValueError("Invalid age range")
            return age
        
        result = fancy_input("Enter your age:", age_validator)
        
        assert result == 25
        
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == 3
    
    def test_custom_validator_with_monkeypatch(self, monkeypatch, capsys):
        """Test custom validator using monkeypatch."""
        # ANNOTATION: Using monkeypatch.setattr for custom validation
        inputs = iter(['short', 'a very long username that exceeds limits', 'validuser'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def username_validator(value):
            if len(value) < 3:
                raise ValueError("Too short")
            if len(value) > 20:
                raise ValueError("Too long")
            return value
        
        result = fancy_input("Enter username:", username_validator)
        
        assert result == "validuser"
        
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == 2

class TestFancyInputMockingComparison:
    """
    Direct comparison tests showing both mocking approaches.
    
    STUDENT NOTE: These tests demonstrate the differences between
    mocker.patch and monkeypatch.setattr for identical scenarios.
    """
    
    def test_float_validation_mocker_approach(self, mocker, capsys):
        """
        MOCKER APPROACH: Clean, automatic cleanup, built-in assertions
        STUDENT NOTE: Notice how mocker.patch provides call tracking automatically
        """
        # ANNOTATION: Using mocker.patch - notice the clean syntax
        mock_input = mocker.patch(
            'builtins.input',
            side_effect=['not_a_number', '3.14159']
        )
        
        def float_validator(value):
            return float(value)
        
        result = fancy_input("Enter a float:", float_validator)
        
        assert result == 3.14159
        # MOCKER BENEFIT: Automatic call tracking and assertions
        assert mock_input.call_count == 2
        mock_input.assert_any_call("Enter a float: ")
    
    def test_float_validation_monkeypatch_approach(self, monkeypatch, capsys):
        """
        MONKEYPATCH APPROACH: More manual setup, but built into pytest
        STUDENT NOTE: Notice the more verbose setup but no external dependencies
        """
        # ANNOTATION: Using monkeypatch.setattr - more manual but flexible
        inputs = iter(['not_a_number', '3.14159'])
        call_count = 0
        calls = []
        
        def mock_input(prompt):
            nonlocal call_count
            call_count += 1
            calls.append(prompt)
            return next(inputs)
        
        monkeypatch.setattr('builtins.input', mock_input)
        
        def float_validator(value):
            return float(value)
        
        result = fancy_input("Enter a float:", float_validator)
        
        assert result == 3.14159
        # MONKEYPATCH: Manual call tracking
        assert call_count == 2
        assert "Enter a float: " in calls

class TestFancyInputAdvancedScenarios:
    """Advanced testing scenarios using both mocking approaches."""
    
    def test_validator_that_returns_different_type_mocker(self, mocker):
        """Test validator that transforms input type using mocker."""
        # ANNOTATION: Using mocker.patch for type transformation testing
        mock_input = mocker.patch('builtins.input', return_value='true')
        
        def bool_validator(value):
            if value.lower() in ['true', '1', 'yes']:
                return True
            elif value.lower() in ['false', '0', 'no']:
                return False
            else:
                raise ValueError("Invalid boolean")
        
        result = fancy_input("Enter true/false:", bool_validator)
        
        assert result is True
        assert isinstance(result, bool)
    
    def test_validator_with_complex_logic_monkeypatch(self, monkeypatch):
        """Test validator with complex logic using monkeypatch."""
        # ANNOTATION: Using monkeypatch.setattr for complex validation
        inputs = iter(['123-45-678', '123-45-6789'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def ssn_validator(value):
            # Simple SSN validation (for demo purposes)
            if len(value) != 11 or value[3] != '-' or value[6] != '-':
                raise ValueError("Invalid SSN format")
            return value
        
        result = fancy_input("Enter SSN (XXX-XX-XXXX):", ssn_validator)
        
        assert result == "123-45-6789"
    
    def test_empty_input_handling_mocker(self, mocker, capsys):
        """Test handling of empty input using mocker."""
        # ANNOTATION: Using mocker.patch to test empty input handling
        mock_input = mocker.patch('builtins.input', side_effect=['', '   ', 'valid'])
        
        def non_empty_validator(value):
            if not value.strip():
                raise ValueError("Cannot be empty")
            return value.strip()
        
        result = fancy_input("Enter something:", non_empty_validator)
        
        assert result == "valid"
        assert mock_input.call_count == 3
    
    def test_exception_types_monkeypatch(self, monkeypatch, capsys):
        """Test that different exception types are all caught using monkeypatch."""
        # ANNOTATION: Using monkeypatch.setattr to test various exception types
        inputs = iter(['type_error_input', 'value_error_input', 'valid'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def multi_exception_validator(value):
            if value == 'type_error_input':
                raise TypeError("Type error")
            elif value == 'value_error_input':
                raise ValueError("Value error")
            return value
        
        result = fancy_input("Enter input:", multi_exception_validator)
        
        assert result == "valid"
        
        # Both exceptions should have triggered error messages
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == 2

class TestMockingBestPractices:
    """
    Demonstrates best practices for both mocking approaches.
    
    STUDENT NOTE: These examples show when to use each approach and why.
    """
    
    def test_when_to_use_mocker_patch(self, mocker):
        """
        WHEN TO USE MOCKER.PATCH:
        - Need detailed call tracking and assertions
        - Want automatic cleanup
        - Working with complex mock scenarios
        - Don't mind the external dependency (pytest-mock)
        
        ANNOTATION: Using mocker.patch - best for complex mocking scenarios
        """
        mock_input = mocker.patch('builtins.input', return_value='test')
        
        def simple_validator(value):
            return value
        
        result = fancy_input("Question:", simple_validator)
        
        # MOCKER ADVANTAGE: Rich assertion methods
        mock_input.assert_called_once_with("Question: ")
        assert result == "test"
    
    def test_when_to_use_monkeypatch(self, monkeypatch):
        """
        WHEN TO USE MONKEYPATCH.SETATTR:
        - Want to avoid external dependencies
        - Need fine-grained control over mock behavior
        - Simple mocking scenarios
        - Learning/educational purposes
        
        ANNOTATION: Using monkeypatch.setattr - best for simple, dependency-free mocking
        """
        monkeypatch.setattr('builtins.input', lambda prompt: 'test')
        
        def simple_validator(value):
            return value
        
        result = fancy_input("Question:", simple_validator)
        
        # MONKEYPATCH: Simple but effective
        assert result == "test"

class TestParametrizedWithBothApproaches:
    """Parametrized tests demonstrating both mocking approaches."""
    
    @pytest.mark.parametrize("mock_approach", ["mocker", "monkeypatch"])
    def test_number_validation_both_approaches(self, request, capsys, mock_approach):
        """
        PYTEST FEATURE: Parametrized test using both mocking approaches
        BENEFIT: Test same logic with different mocking methods
        STUDENT NOTE: Shows how both approaches achieve the same result
        """
        if mock_approach == "mocker":
            # ANNOTATION: Using mocker.patch in parametrized test
            mocker = request.getfixturevalue("mocker")
            mock_input = mocker.patch('builtins.input', side_effect=['abc', '42'])
        else:
            # ANNOTATION: Using monkeypatch.setattr in parametrized test
            monkeypatch = request.getfixturevalue("monkeypatch")
            inputs = iter(['abc', '42'])
            monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def int_validator(value):
            return int(value)
        
        result = fancy_input("Enter number:", int_validator)
        
        assert result == 42
        
        captured = capsys.readouterr()
        assert "Please enter a valid response" in captured.out
    
    @pytest.mark.parametrize("inputs,expected_attempts", [
        (['valid'], 1),
        (['invalid', 'valid'], 2),
        (['bad1', 'bad2', 'valid'], 3),
        (['bad1', 'bad2', 'bad3', 'valid'], 4),
    ])
    def test_attempt_counting_mocker(self, mocker, capsys, inputs, expected_attempts):
        """
        PYTEST FEATURE: Parametrized test with mocker for attempt counting
        ANNOTATION: Using mocker.patch with parametrized inputs
        """
        mock_input = mocker.patch('builtins.input', side_effect=inputs)
        
        def string_validator(value):
            if value == 'valid':
                return value
            raise ValueError("Invalid input")
        
        result = fancy_input("Enter text:", string_validator)
        
        assert result == 'valid'
        assert mock_input.call_count == expected_attempts
        
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == expected_attempts - 1
    
    @pytest.mark.parametrize("inputs,expected_attempts", [
        (['valid'], 1),
        (['invalid', 'valid'], 2),
        (['bad1', 'bad2', 'valid'], 3),
    ])
    def test_attempt_counting_monkeypatch(self, monkeypatch, capsys, inputs, expected_attempts):
        """
        PYTEST FEATURE: Parametrized test with monkeypatch for attempt counting
        ANNOTATION: Using monkeypatch.setattr with parametrized inputs
        """
        input_iter = iter(inputs)
        call_count = 0
        
        def mock_input(prompt):
            nonlocal call_count
            call_count += 1
            return next(input_iter)
        
        monkeypatch.setattr('builtins.input', mock_input)
        
        def string_validator(value):
            if value == 'valid':
                return value
            raise ValueError("Invalid input")
        
        result = fancy_input("Enter text:", string_validator)
        
        assert result == 'valid'
        assert call_count == expected_attempts
        
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == expected_attempts - 1

class TestRealWorldScenarios:
    """Real-world usage scenarios testing both mocking approaches."""
    
    def test_password_validation_mocker(self, mocker, capsys):
        """Test password validation scenario using mocker."""
        # ANNOTATION: Using mocker.patch for password validation
        mock_input = mocker.patch(
            'builtins.input',
            side_effect=['123', 'password', 'MySecurePass123!']
        )
        
        def password_validator(value):
            if len(value) < 8:
                raise ValueError("Password too short")
            if not any(c.isupper() for c in value):
                raise ValueError("Must contain uppercase")
            if not any(c.isdigit() for c in value):
                raise ValueError("Must contain digit")
            return value
        
        result = fancy_input("Enter password:", password_validator)
        
        assert result == "MySecurePass123!"
        assert mock_input.call_count == 3
    
    def test_menu_selection_monkeypatch(self, monkeypatch, capsys):
        """Test menu selection scenario using monkeypatch."""
        # ANNOTATION: Using monkeypatch.setattr for menu selection
        inputs = iter(['0', '5', '3'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def menu_validator(value):
            choice = int(value)
            if choice < 1 or choice > 4:
                raise ValueError("Choice must be 1-4")
            return choice
        
        result = fancy_input("Select option (1-4):", menu_validator)
        
        assert result == 3
        
        captured = capsys.readouterr()
        error_count = captured.out.count("Please enter a valid response")
        assert error_count == 2
    
    def test_file_path_validation_mocker(self, mocker, tmp_path):
        """Test file path validation using mocker."""
        # ANNOTATION: Using mocker.patch for file path validation
        valid_file = tmp_path / "existing.txt"
        valid_file.write_text("content")
        
        mock_input = mocker.patch(
            'builtins.input',
            side_effect=['/nonexistent/path', str(valid_file)]
        )
        
        def file_validator(value):
            from pathlib import Path
            path = Path(value)
            if not path.exists():
                raise FileNotFoundError("File does not exist")
            return str(path)
        
        result = fancy_input("Enter file path:", file_validator)
        
        assert result == str(valid_file)
        assert mock_input.call_count == 2

class TestExactOutputFormatVerification:
    """
    Tests that verify the exact text format and output matching expected format.
    
    STUDENT NOTE: These tests focus specifically on Case 3 - ensuring the exact
    text printed to screen matches the expected format with precise formatting.
    """
    
    def test_exact_error_message_format_mocker(self, mocker, capsys):
        """
        Test that verifies the EXACT error message format using mocker.
        ANNOTATION: Using mocker.patch to verify precise output formatting
        """
        mock_input = mocker.patch('builtins.input', side_effect=['invalid', 'valid'])
        
        def simple_validator(value):
            if value == 'invalid':
                raise ValueError("Invalid")
            return value
        
        result = fancy_input("What is your name?", simple_validator)
        
        captured = capsys.readouterr()
        
        # ✅ More precise format verification - exact newlines and spacing
        assert captured.out == "\nPlease enter a valid response.\n\n"
        
    def test_exact_prompt_format_mocker(self, mocker):
        """
        Test that verifies the exact prompt format using mocker.
        ANNOTATION: Using mocker.patch to verify prompt includes exactly one space
        """
        mock_input = mocker.patch('builtins.input', return_value='test')
        
        def identity_validator(value):
            return value
        
        result = fancy_input("Enter your choice", identity_validator)
        
        # ✅ Verify exact prompt format (question + single space)
        mock_input.assert_called_once_with("Enter your choice ")
    
    def test_exact_error_message_format_monkeypatch(self, monkeypatch, capsys):
        """
        Test exact error message format using monkeypatch.
        ANNOTATION: Using monkeypatch.setattr for precise format verification
        """
        inputs = iter(['invalid', 'valid'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        
        def simple_validator(value):
            if value == 'invalid':
                raise ValueError("Invalid")
            return value
        
        result = fancy_input("Enter data", simple_validator)
        
        captured = capsys.readouterr()
        
        # ✅ Verify exact error message format
        assert captured.out == "\nPlease enter a valid response.\n\n"
    
    def test_multiple_errors_exact_format_mocker(self, mocker, capsys):
        """
        Test exact format when multiple errors occur.
        ANNOTATION: Using mocker.patch to verify repeated error message formatting
        """
        mock_input = mocker.patch('builtins.input', side_effect=['bad1', 'bad2', 'good'])
        
        def validator(value):
            if value.startswith('bad'):
                raise ValueError("Bad input")
            return value
        
        result = fancy_input("Enter something", validator)
        
        captured = capsys.readouterr()
        
        # ✅ Verify exact format for multiple error messages
        expected_output = "\nPlease enter a valid response.\n\n\nPlease enter a valid response.\n\n"
        assert captured.out == expected_output
    
    def test_prompt_with_different_questions_monkeypatch(self, monkeypatch):
        """
        Test that different question formats all get the space appended.
        ANNOTATION: Using monkeypatch.setattr to test various prompt formats
        """
        calls = []
        
        def mock_input(prompt):
            calls.append(prompt)
            return 'answer'
        
        monkeypatch.setattr('builtins.input', mock_input)
        
        def identity_validator(value):
            return value
        
        # Test various question formats
        test_questions = [
            "Simple question",
            "Question with punctuation?",
            "Question with colon:",
            "Question ending with period.",
        ]
        
        for question in test_questions:
            calls.clear()  # Reset calls for each test
            result = fancy_input(question, identity_validator)
            
            # ✅ Verify each question gets exactly one space appended
            assert calls[0] == f"{question} "
    
    def test_no_extra_output_on_success_mocker(self, mocker, capsys):
        """
        Test that successful validation produces no error output.
        ANNOTATION: Using mocker.patch to verify clean success case
        """
        mock_input = mocker.patch('builtins.input', return_value='valid')
        
        def simple_validator(value):
            return value
        
        result = fancy_input("Enter input", simple_validator)
        
        captured = capsys.readouterr()
        
        # ✅ Verify no error messages on successful first attempt
        assert captured.out == ""
        assert captured.err == ""

class TestEdgeCasesAndErrorHandling:
    """Edge cases and error handling with both mocking approaches."""
    
    def test_validator_raises_system_exit_mocker(self, mocker):
        """Test validator that raises SystemExit using mocker."""
        # ANNOTATION: Using mocker.patch to test SystemExit handling
        mock_input = mocker.patch('builtins.input', return_value='exit')
        
        def exit_validator(value):
            if value == 'exit':
                raise SystemExit("User requested exit")
            return value
        
        # SystemExit should propagate, not be caught by fancy_input
        with pytest.raises(SystemExit):
            fancy_input("Enter command:", exit_validator)
    
    def test_validator_raises_keyboard_interrupt_monkeypatch(self, monkeypatch):
        """Test validator that raises KeyboardInterrupt using monkeypatch."""
        # ANNOTATION: Using monkeypatch.setattr to test KeyboardInterrupt handling
        monkeypatch.setattr('builtins.input', lambda prompt: 'interrupt')
        
        def interrupt_validator(value):
            if value == 'interrupt':
                raise KeyboardInterrupt("User interrupted")
            return value
        
        # KeyboardInterrupt should propagate, not be caught by fancy_input
        with pytest.raises(KeyboardInterrupt):
            fancy_input("Enter command:", interrupt_validator)
    
    def test_input_function_raises_exception_mocker(self, mocker, capsys):
        """Test when input() itself raises an exception using mocker."""
        # ANNOTATION: Using mocker.patch to simulate input() raising exception
        mock_input = mocker.patch('builtins.input', side_effect=EOFError("EOF"))
        
        def simple_validator(value):
            return value
        
        # EOFError from input() should propagate
        with pytest.raises(EOFError):
            fancy_input("Enter text:", simple_validator)

class TestDocumentationExamples:
    """Tests that serve as documentation examples for students."""
    
    def test_basic_usage_example_mocker(self, mocker, capsys):
        """
        DOCUMENTATION EXAMPLE: Basic usage with mocker.patch
        
        This example shows the most common pattern students will use:
        1. Mock input with expected user responses
        2. Define a validator function  
        3. Call fancy_input
        4. Assert the result and behavior
        
        ANNOTATION: Using mocker.patch - recommended for most cases
        """
        # Step 1: Mock the input with user responses
        mock_input = mocker.patch(
            'builtins.input', 
            side_effect=['not_a_number', '42']
        )
        
        # Step 2: Define validator
        def number_validator(value):
            return int(value)  # Raises ValueError if not a number
        
        # Step 3: Test the function
        result = fancy_input("Enter a number:", number_validator)
        
        # Step 4: Assert results
        assert result == 42
        assert mock_input.call_count == 2
        
        # Step 5: Verify error message was shown
        captured = capsys.readouterr()
        assert "Please enter a valid response" in captured.out
    
    def test_basic_usage_example_monkeypatch(self, monkeypatch, capsys):
        """
        DOCUMENTATION EXAMPLE: Basic usage with monkeypatch.setattr
        
        This example shows the monkeypatch approach:
        1. Create an iterator of user responses
        2. Patch input with a lambda that uses the iterator
        3. Define validator and test
        4. Manually track calls if needed
        
        ANNOTATION: Using monkeypatch.setattr - good for simple cases
        """
        # Step 1: Create iterator of user responses
        user_inputs = iter(['not_a_number', '42'])
        
        # Step 2: Patch input function
        monkeypatch.setattr('builtins.input', lambda prompt: next(user_inputs))
        
        # Step 3: Define validator
        def number_validator(value):
            return int(value)
        
        # Step 4: Test the function
        result = fancy_input("Enter a number:", number_validator)
        
        # Step 5: Assert results
        assert result == 42
        
        # Step 6: Verify error message
        captured = capsys.readouterr()
        assert "Please enter a valid response" in captured.out

class TestMockingBestPracticesComparison:
    """
    Side-by-side comparison of mocking approaches for educational purposes.
    
    STUDENT LEARNING OBJECTIVES:
    1. Understand when to use each approach
    2. See the trade-offs between complexity and features
    3. Learn best practices for both methods
    """
    
    def test_pros_and_cons_mocker(self, mocker):
        """
        MOCKER.PATCH PROS:
        - Automatic call tracking and rich assertions
        - Clean syntax for complex scenarios
        - Automatic cleanup
        - Great for detailed testing
        
        MOCKER.PATCH CONS:
        - Requires pytest-mock plugin
        - Slightly more overhead
        - May be overkill for simple tests
        
        ANNOTATION: Using mocker.patch - notice the built-in features
        """
        mock_input = mocker.patch('builtins.input', return_value='test')
        
        def identity_validator(value):
            return value
        
        result = fancy_input("Enter:", identity_validator)
        
        # PROS: Rich assertion methods available
        mock_input.assert_called_once_with("Enter: ")
        assert mock_input.call_count == 1
        assert mock_input.return_value == 'test'
        assert result == 'test'
    
    def test_pros_and_cons_monkeypatch(self, monkeypatch):
        """
        MONKEYPATCH.SETATTR PROS:
        - Built into pytest core (no external dependencies)
        - Fine-grained control over mock behavior
        - Simpler for basic scenarios
        - Educational value (shows what's happening)
        
        MONKEYPATCH.SETATTR CONS:
        - More verbose setup
        - Manual call tracking required
        - Less convenient for complex scenarios
        
        ANNOTATION: Using monkeypatch.setattr - notice the manual setup
        """
        call_count = 0
        calls = []
        
        def mock_input(prompt):
            nonlocal call_count
            call_count += 1
            calls.append(prompt)
            return 'test'
        
        monkeypatch.setattr('builtins.input', mock_input)
        
        def identity_validator(value):
            return value
        
        result = fancy_input("Enter:", identity_validator)
        
        # CONS: Manual tracking required, but PROS: full control
        assert call_count == 1
        assert calls == ["Enter: "]
        assert result == 'test'

if __name__ == "__main__":
    pytest.main([__file__, "-v"])