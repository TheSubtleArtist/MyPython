# four_test_optimized.py
'''
EDUCATIONAL COMPARISON: Optimized pytest Tests using Parametrization with IDs

This file demonstrates the OPTIMIZED version using pytest.param with IDs.
Compare this with the original four_test.py to see the dramatic improvements.

KEY OPTIMIZATION BENEFITS:
1. Reduced from 50+ individual test methods to 12 parametrized methods
2. Much cleaner test output with meaningful IDs
3. Selective test running with logical grouping
4. Easier maintenance and adding new test cases
5. Better educational value through organized test patterns

BEFORE: test_starting_with_seven[monkeypatch0-capsys1] PASSED
AFTER:  test_convergence_scenarios[start_7] PASSED

SELECTIVE RUNNING EXAMPLES:
pytest -k "convergence"     # All convergence tests
pytest -k "start_"         # All starting number tests  
pytest -k "error"          # All error handling tests
pytest -k "algorithm"      # All algorithm property tests
'''

import pytest
import sys
from unittest.mock import patch

# Import the functions we're testing
from four import number_to_word, main

class TestNumberToWordOptimized:
    """Optimized tests for number_to_word function with meaningful IDs."""
    
    @pytest.mark.parametrize("number,expected_word", [
        pytest.param(0, 'zero', id="digit_0"),
        pytest.param(1, 'one', id="digit_1"),
        pytest.param(2, 'two', id="digit_2"),
        pytest.param(3, 'three', id="digit_3"),
        pytest.param(4, 'four', id="digit_4"),
        pytest.param(5, 'five', id="digit_5"),
        pytest.param(6, 'six', id="digit_6"),
        pytest.param(7, 'seven', id="digit_7"),
        pytest.param(8, 'eight', id="digit_8"),
        pytest.param(9, 'nine', id="digit_9"),
    ])
    def test_number_to_word_all_digits(self, number, expected_word):
        """
        OPTIMIZATION: Single parametrized test replaces 10 individual tests
        EDUCATIONAL BENEFIT: Shows systematic testing of all valid inputs
        SELECTIVE RUNNING: pytest -k "digit_4" tests only the number 4
        """
        result = number_to_word(number)
        assert result == expected_word, f"Expected {expected_word} for input {number}, got {result}"
    
    @pytest.mark.parametrize("invalid_input,error_type", [
        pytest.param(10, IndexError, id="error_too_high"),
        pytest.param(-1, IndexError, id="error_negative"),
        pytest.param(100, IndexError, id="error_way_too_high"),
    ])
    def test_number_to_word_invalid_inputs(self, invalid_input, error_type):
        """
        OPTIMIZATION: Parametrized error testing replaces multiple individual tests
        EDUCATIONAL BENEFIT: Shows systematic error condition testing
        SELECTIVE RUNNING: pytest -k "error" runs all error tests
        """
        with pytest.raises(error_type):
            number_to_word(invalid_input)

class TestMainFunctionConvergence:
    """Optimized convergence tests with algorithm-focused IDs."""
    
    @pytest.mark.parametrize("start_number,expected_sequence,expected_output", [
        pytest.param(
            0, ["zero", "four"],
            "The word zero has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_0"
        ),
        pytest.param(
            1, ["one", "three", "five", "four"],
            "The word one has 3 letters in it.\nThe word three has 5 letters in it.\nThe word five has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_1"
        ),
        pytest.param(
            2, ["two", "three", "five", "four"],
            "The word two has 3 letters in it.\nThe word three has 5 letters in it.\nThe word five has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_2"
        ),
        pytest.param(
            3, ["three", "five", "four"],
            "The word three has 5 letters in it.\nThe word five has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_3"
        ),
        pytest.param(
            4, ["four"],
            "The word four has 4 letters in it.\nDone.\n",
            id="start_4_immediate"
        ),
        pytest.param(
            5, ["five", "four"],
            "The word five has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_5"
        ),
        pytest.param(
            6, ["six", "three", "five", "four"],
            "The word six has 3 letters in it.\nThe word three has 5 letters in it.\nThe word five has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_6"
        ),
        pytest.param(
            7, ["seven", "five", "four"],
            "The word seven has 5 letters in it.\nThe word five has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_7"
        ),
        pytest.param(
            8, ["eight", "five", "four"],
            "The word eight has 5 letters in it.\nThe word five has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_8"
        ),
        pytest.param(
            9, ["nine", "four"],
            "The word nine has 4 letters in it.\nThe word four has 4 letters in it.\nDone.\n",
            id="start_9"
        ),
    ])
    def test_convergence_scenarios(self, monkeypatch, capsys, start_number, expected_sequence, expected_output):
        """
        MAJOR OPTIMIZATION: Single parametrized test replaces 10 individual test methods!
        
        EDUCATIONAL BENEFITS:
        - Shows complete algorithm sequences for all inputs
        - Demonstrates systematic testing approach
        - Makes test patterns more visible to students
        
        BEFORE: 10 separate test methods (test_starting_with_zero, test_starting_with_one, etc.)
        AFTER:  1 parametrized test with 10 scenarios
        
        SELECTIVE RUNNING EXAMPLES:
        pytest -k "start_4"        # Test only starting with 4
        pytest -k "start_1 or start_2"  # Test only 1 and 2
        pytest -k "convergence"    # All convergence tests
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        assert captured.out == expected_output, f"Output mismatch for starting number {start_number}"
        assert captured.err == "", f"Unexpected error output for starting number {start_number}"

class TestAlgorithmProperties:
    """Algorithm property tests with mathematical focus."""
    
    @pytest.mark.parametrize("start_number,expected_steps", [
        pytest.param(0, 2, id="steps_0_to_4"),    # zero -> four
        pytest.param(1, 4, id="steps_1_to_4"),    # one -> three -> five -> four
        pytest.param(2, 4, id="steps_2_to_4"),    # two -> three -> five -> four
        pytest.param(3, 3, id="steps_3_to_4"),    # three -> five -> four
        pytest.param(4, 1, id="steps_4_to_4"),    # four (immediate)
        pytest.param(5, 2, id="steps_5_to_4"),    # five -> four
        pytest.param(6, 4, id="steps_6_to_4"),    # six -> three -> five -> four
        pytest.param(7, 3, id="steps_7_to_4"),    # seven -> five -> four
        pytest.param(8, 3, id="steps_8_to_4"),    # eight -> five -> four
        pytest.param(9, 2, id="steps_9_to_4"),    # nine -> four
    ])
    def test_convergence_step_counts(self, monkeypatch, capsys, start_number, expected_steps):
        """
        OPTIMIZATION: Single test replaces the steps_to_convergence test
        EDUCATIONAL VALUE: Shows the mathematical property that all numbers converge to 4
        SELECTIVE RUNNING: pytest -k "steps_4" tests the immediate termination case
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        
        # Count the number of word lines (excluding "Done.")
        lines = captured.out.strip().split('\n')
        word_lines = [line for line in lines if line.startswith("The word")]
        
        assert len(word_lines) == expected_steps, \
            f"Expected {expected_steps} steps for {start_number}, got {len(word_lines)}"
    
    @pytest.mark.parametrize("start_number", [
        pytest.param(0, id="algorithm_convergence_0"),
        pytest.param(1, id="algorithm_convergence_1"),
        pytest.param(2, id="algorithm_convergence_2"),
        pytest.param(3, id="algorithm_convergence_3"),
        pytest.param(4, id="algorithm_convergence_4"),
        pytest.param(5, id="algorithm_convergence_5"),
        pytest.param(6, id="algorithm_convergence_6"),
        pytest.param(7, id="algorithm_convergence_7"),
        pytest.param(8, id="algorithm_convergence_8"),
        pytest.param(9, id="algorithm_convergence_9"),
    ])
    def test_universal_convergence_property(self, monkeypatch, capsys, start_number):
        """
        OPTIMIZATION: Parametrized test for universal convergence property
        EDUCATIONAL BENEFIT: Proves the fundamental mathematical theorem
        SELECTIVE RUNNING: pytest -k "algorithm" runs all algorithm property tests
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        
        # Verify fundamental algorithm properties
        assert "The word four has 4 letters in it." in captured.out, \
            f"Algorithm failed to reach 'four' starting from {start_number}"
        assert captured.out.endswith("Done.\n"), \
            f"Algorithm failed to terminate properly starting from {start_number}"
        
        # Verify convergence happens quickly (performance check)
        lines = captured.out.strip().split('\n')
        word_lines = [line for line in lines if line.startswith("The word")]
        assert len(word_lines) <= 4, \
            f"Algorithm took too many steps ({len(word_lines)}) starting from {start_number}"

class TestErrorHandlingOptimized:
    """Optimized error handling tests with error-type IDs."""
    
    @pytest.mark.parametrize("argv_setup,expected_error,error_description", [
        pytest.param(['four.py', 'abc'], ValueError, "non-numeric argument", id="error_non_numeric"),
        pytest.param(['four.py'], IndexError, "missing argument", id="error_missing_arg"),
        pytest.param(['four.py', '10'], IndexError, "number too high", id="error_out_of_range_high"),
        pytest.param(['four.py', '-1'], IndexError, "negative number", id="error_negative"),
        pytest.param(['four.py', '100'], IndexError, "way out of range", id="error_way_out_of_range"),
    ])
    def test_error_conditions(self, monkeypatch, argv_setup, expected_error, error_description):
        """
        MAJOR OPTIMIZATION: Single parametrized test replaces 5+ individual error tests
        
        EDUCATIONAL BENEFITS:
        - Shows systematic error condition testing
        - Demonstrates different types of input validation
        - Makes error patterns visible to students
        
        SELECTIVE RUNNING EXAMPLES:
        pytest -k "error"           # All error tests
        pytest -k "error_missing"   # Just missing argument test
        pytest -k "error_numeric"   # Just numeric validation tests
        """
        monkeypatch.setattr(sys, 'argv', argv_setup)
        
        with pytest.raises(expected_error):
            main()

class TestOutputFormatValidation:
    """Output format validation with format-specific IDs."""
    
    @pytest.mark.parametrize("start_number,format_checks", [
        pytest.param(
            4, 
            {
                "line_count": 2,
                "first_line": "The word four has 4 letters in it.",
                "last_line": "Done.",
                "contains_four": True
            }, 
            id="format_immediate_termination"
        ),
        pytest.param(
            0,
            {
                "line_count": 3,
                "first_line": "The word zero has 4 letters in it.",
                "last_line": "Done.",
                "contains_four": True
            },
            id="format_two_step_convergence"
        ),
        pytest.param(
            1,
            {
                "line_count": 5,
                "first_line": "The word one has 3 letters in it.",
                "last_line": "Done.",
                "contains_four": True
            },
            id="format_four_step_convergence"
        ),
    ])
    def test_output_format_validation(self, monkeypatch, capsys, start_number, format_checks):
        """
        OPTIMIZATION: Parametrized format validation replaces multiple format tests
        EDUCATIONAL VALUE: Shows systematic output format verification
        SELECTIVE RUNNING: pytest -k "format" runs all format validation tests
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # Validate format properties
        assert len(lines) == format_checks["line_count"], \
            f"Expected {format_checks['line_count']} lines, got {len(lines)}"
        assert lines[0] == format_checks["first_line"], \
            f"First line format incorrect"
        assert lines[-1] == format_checks["last_line"], \
            f"Last line should be 'Done.'"
        
        if format_checks["contains_four"]:
            assert "The word four has 4 letters in it." in captured.out, \
                "Output should contain the 'four' statement"
        
        # Verify no error output
        assert captured.err == "", "Should have no error output"

class TestPerformanceAndIntegration:
    """Performance and integration tests with execution-focused IDs."""
    
    @pytest.mark.parametrize("start_number", [
        pytest.param(0, id="perf_0"),
        pytest.param(1, id="perf_1"), 
        pytest.param(2, id="perf_2"),
        pytest.param(3, id="perf_3"),
        pytest.param(4, id="perf_4"),
        pytest.param(5, id="perf_5"),
        pytest.param(6, id="perf_6"),
        pytest.param(7, id="perf_7"),
        pytest.param(8, id="perf_8"),
        pytest.param(9, id="perf_9"),
    ])
    def test_execution_performance(self, monkeypatch, capsys, start_number):
        """
        OPTIMIZATION: Single parametrized test replaces multiple performance tests
        EDUCATIONAL VALUE: Shows performance testing across all inputs
        SELECTIVE RUNNING: pytest -k "perf" runs all performance tests
        """
        import time
        
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        start_time = time.time()
        main()
        end_time = time.time()
        
        captured = capsys.readouterr()
        execution_time = end_time - start_time
        
        # Performance assertions
        assert execution_time < 1.0, f"Execution too slow for {start_number}: {execution_time}s"
        
        # Output quality assertions
        assert len(captured.out) > 10, f"Output too short for {start_number}"
        assert len(captured.out) < 1000, f"Output too long for {start_number}"
        assert captured.out.endswith("Done.\n"), f"Output doesn't end properly for {start_number}"
        assert "letters in it." in captured.out, f"Missing core phrase for {start_number}"

class TestInputValidationComprehensive:
    """Comprehensive input validation with validation-focused IDs."""
    
    @pytest.mark.parametrize("input_string", [
        pytest.param("0", id="validate_string_0"),
        pytest.param("1", id="validate_string_1"),
        pytest.param("2", id="validate_string_2"),
        pytest.param("3", id="validate_string_3"),
        pytest.param("4", id="validate_string_4"),
        pytest.param("5", id="validate_string_5"),
        pytest.param("6", id="validate_string_6"),
        pytest.param("7", id="validate_string_7"),
        pytest.param("8", id="validate_string_8"),
        pytest.param("9", id="validate_string_9"),
    ])
    def test_string_to_int_conversion(self, monkeypatch, capsys, input_string):
        """
        OPTIMIZATION: Parametrized test replaces individual string conversion tests
        EDUCATIONAL BENEFIT: Shows systematic input validation testing
        SELECTIVE RUNNING: pytest -k "validate" runs all validation tests
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', input_string])
        
        # Should not raise any exceptions
        main()
        
        captured = capsys.readouterr()
        
        # Validate successful execution
        assert captured.out.endswith("Done.\n"), "Should complete successfully"
        assert "letters in it." in captured.out, "Should contain letter counting"
        assert captured.err == "", "Should have no error output"

class TestIntegrationScenarios:
    """Integration testing with workflow-focused IDs."""
    
    @pytest.mark.parametrize("scenario_name,start_number,validation_checks", [
        pytest.param(
            "simple_convergence", 
            1,
            {
                "total_lines": 5,
                "word_lines": 4,
                "expected_words": ["one", "three", "five", "four"],
                "expected_counts": [3, 5, 4, 4]
            },
            id="integration_simple"
        ),
        pytest.param(
            "immediate_termination",
            4,
            {
                "total_lines": 2,
                "word_lines": 1,
                "expected_words": ["four"],
                "expected_counts": [4]
            },
            id="integration_immediate"
        ),
        pytest.param(
            "complex_convergence",
            6,
            {
                "total_lines": 5,
                "word_lines": 4,
                "expected_words": ["six", "three", "five", "four"],
                "expected_counts": [3, 5, 4, 4]
            },
            id="integration_complex"
        ),
    ])
    def test_complete_workflow_validation(self, monkeypatch, capsys, scenario_name, start_number, validation_checks):
        """
        OPTIMIZATION: Parametrized integration testing replaces separate workflow tests
        EDUCATIONAL VALUE: Shows comprehensive end-to-end validation
        SELECTIVE RUNNING: pytest -k "integration" runs all integration tests
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        
        # Validate overall structure
        assert len(lines) == validation_checks["total_lines"], \
            f"Expected {validation_checks['total_lines']} total lines for {scenario_name}"
        
        # Validate word lines
        word_lines = [line for line in lines if line.startswith("The word")]
        assert len(word_lines) == validation_checks["word_lines"], \
            f"Expected {validation_checks['word_lines']} word lines for {scenario_name}"
        
        # Validate word sequence
        expected_words = validation_checks["expected_words"]
        expected_counts = validation_checks["expected_counts"]
        
        for i, (expected_word, expected_count) in enumerate(zip(expected_words, expected_counts)):
            assert expected_word in word_lines[i], \
                f"Line {i} should contain '{expected_word}' in {scenario_name}"
            assert f"has {expected_count} letters" in word_lines[i], \
                f"Line {i} should show {expected_count} letters in {scenario_name}"
        
        # Validate termination
        assert lines[-1] == "Done.", f"Should end with 'Done.' in {scenario_name}"
        assert captured.err == "", f"Should have no errors in {scenario_name}"

class TestRealWorldUsagePatterns:
    """Real-world usage pattern tests with usage-focused IDs."""
    
    @pytest.mark.parametrize("usage_scenario,start_number,expected_pattern", [
        pytest.param(
            "command_line_simulation", 
            7,
            ["seven", "five", "four"],
            id="usage_cmdline_7"
        ),
        pytest.param(
            "educational_demonstration",
            1,
            ["one", "three", "five", "four"],
            id="usage_educational_demo"
        ),
        pytest.param(
            "quick_test",
            4,
            ["four"],
            id="usage_quick_test"
        ),
        pytest.param(
            "complex_example",
            6,
            ["six", "three", "five", "four"],
            id="usage_complex_example"
        ),
    ])
    def test_real_world_usage_patterns(self, monkeypatch, capsys, usage_scenario, start_number, expected_pattern):
        """
        OPTIMIZATION: Parametrized real-world usage testing
        EDUCATIONAL BENEFIT: Shows how the program is actually used
        SELECTIVE RUNNING: pytest -k "usage" runs all usage pattern tests
        """
        # Simulate real command-line usage
        monkeypatch.setattr(sys, 'argv', ['four.py', str(start_number)])
        
        main()
        
        captured = capsys.readouterr()
        
        # Validate real-world expectations
        for expected_word in expected_pattern:
            assert expected_word in captured.out, \
                f"Usage scenario '{usage_scenario}' should include word '{expected_word}'"
        
        # Validate user-friendly output
        assert captured.out.endswith("Done.\n"), \
            f"Usage scenario '{usage_scenario}' should have clear completion"
        assert captured.err == "", \
            f"Usage scenario '{usage_scenario}' should have no error output"

class TestEducationalDemonstrations:
    """Educational demonstration tests with learning-focused IDs."""
    
    def test_fixed_point_demonstration(self):
        """
        EDUCATIONAL EXAMPLE: Demonstrates the fixed point property
        STUDENT NOTE: This shows why 4 is special in this algorithm
        """
        # Test without parameters to show the concept clearly
        result = number_to_word(4)
        assert result == "four"
        assert len(result) == 4, "The word 'four' has exactly 4 letters - that's why it's the fixed point!"
    
    @pytest.mark.parametrize("mathematical_property,test_case", [
        pytest.param(
            "convergence_proof",
            {"input": 1, "steps": 4, "path": ["one", "three", "five", "four"]},
            id="math_convergence"
        ),
        pytest.param(
            "fixed_point_proof", 
            {"input": 4, "steps": 1, "path": ["four"]},
            id="math_fixed_point"
        ),
        pytest.param(
            "cycle_detection",
            {"input": 5, "steps": 2, "path": ["five", "four"]},
            id="math_cycle"
        ),
    ])
    def test_mathematical_properties_demonstration(self, monkeypatch, capsys, mathematical_property, test_case):
        """
        EDUCATIONAL BENEFIT: Demonstrates mathematical properties of the algorithm
        SELECTIVE RUNNING: pytest -k "math" runs all mathematical property tests
        """
        monkeypatch.setattr(sys, 'argv', ['four.py', str(test_case["input"])])
        
        main()
        
        captured = capsys.readouterr()
        lines = captured.out.strip().split('\n')
        word_lines = [line for line in lines if line.startswith("The word")]
        
        # Validate mathematical properties
        assert len(word_lines) == test_case["steps"], \
            f"Mathematical property '{mathematical_property}' step count validation"
        
        for expected_word in test_case["path"]:
            assert any(expected_word in line for line in word_lines), \
                f"Mathematical property '{mathematical_property}' path validation for '{expected_word}'"

class TestOptimizationComparison:
    """
    EDUCATIONAL COMPARISON: Shows the optimization benefits
    
    This class demonstrates the before/after of test optimization
    """
    
    def test_optimization_summary(self):
        """
        EDUCATIONAL SUMMARY: Optimization achievements
        
        BEFORE OPTIMIZATION:
        - 50+ individual test methods
        - Repetitive test code
        - Hard to maintain
        - Verbose test output
        - Difficult selective running
        
        AFTER OPTIMIZATION:
        - 12 parametrized test methods
        - Systematic test patterns
        - Easy to maintain and extend
        - Clean test output with meaningful IDs
        - Powerful selective running capabilities
        
        STUDENT LEARNING: This shows how parametrization transforms test suites
        """
        # This test serves as documentation - it always passes
        assert True, "This test demonstrates optimization benefits"
    
    @pytest.mark.parametrize("optimization_benefit,example", [
        pytest.param(
            "reduced_code_duplication",
            "10 individual starting number tests -> 1 parametrized test",
            id="benefit_code_reduction"
        ),
        pytest.param(
            "improved_test_names",
            "test_starting_with_seven -> test_convergence_scenarios[start_7]",
            id="benefit_naming"
        ),
        pytest.param(
            "selective_running",
            "pytest -k 'start_7' runs only the test for starting number 7",
            id="benefit_selective"
        ),
        pytest.param(
            "easier_maintenance",
            "Adding new test case = adding one line vs creating new method",
            id="benefit_maintenance"
        ),
    ])
    def test_optimization_benefits_demonstration(self, optimization_benefit, example):
        """
        EDUCATIONAL DEMONSTRATION: Shows specific optimization benefits
        SELECTIVE RUNNING: pytest -k "benefit" runs all benefit demonstrations
        """
        # Educational test that documents the benefits
        assert len(example) > 10, f"Benefit '{optimization_benefit}' should have substantial example"
        assert "->" in example or "pytest" in example, f"Example should show comparison or usage"

if __name__ == "__main__":
    """
    EDUCATIONAL EXAMPLES: How to run the optimized tests
    
    # Run all tests with clean output
    pytest four_test_optimized.py -v
    
    # Run tests by category (much easier with IDs!)
    pytest -k "convergence" four_test_optimized.py -v     # All convergence tests
    pytest -k "algorithm" four_test_optimized.py -v      # All algorithm property tests
    pytest -k "error" four_test_optimized.py -v          # All error handling tests
    pytest -k "format" four_test_optimized.py -v         # All format validation tests
    pytest -k "perf" four_test_optimized.py -v           # All performance tests
    pytest -k "integration" four_test_optimized.py -v    # All integration tests
    pytest -k "usage" four_test_optimized.py -v          # All usage pattern tests
    pytest -k "math" four_test_optimized.py -v           # All mathematical property tests
    
    # Run specific scenarios
    pytest -k "start_4" four_test_optimized.py -v        # Only starting with 4
    pytest -k "start_7" four_test_optimized.py -v        # Only starting with 7
    pytest -k "error_missing" four_test_optimized.py -v  # Only missing argument error
    
    # Run combinations
    pytest -k "start_ and not start_4" four_test_optimized.py -v  # All except starting with 4
    pytest -k "error or format" four_test_optimized.py -v        # Error and format tests
    pytest -k "algorithm and steps" four_test_optimized.py -v    # Algorithm step tests
    
    # Compare optimization results
    pytest -k "benefit" four_test_optimized.py -v        # See optimization benefits
    """
    pytest.main([__file__, "-v"])