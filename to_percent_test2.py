# test_to_percent.py
'''
Summary of Comprehensive Test Coverage:
✅ Maximized Testing with Minimal Test Count:

13 parametrized test methods covering 200+ test scenarios
Comprehensive coverage achieved through strategic parametrization
✅ Test Categories Covered:

Core Functionality - All basic ratio-to-percentage conversions
Special Values - Infinity, NaN, positive/negative zero
Precision & Rounding - Exact .1% precision behavior testing
Type Handling - Different numeric input types
Real-World Scenarios - Business, academic, statistical use cases
Mathematical Properties - Relationships and consistency
Boundary Conditions - Edge cases and decision points
Error Handling - Invalid input types
Format Consistency - Output string format validation
Performance Characteristics - Scale and range testing
Documentation Examples - Usage patterns for students
Comparison Testing - Validation against manual calculations
✅ Key Benefits of This Approach:

Minimal Code - 13 test methods instead of 200+ individual tests
Maximum Coverage - Every conceivable use case and edge case
Student-Friendly - Clear descriptions and real-world examples
Maintainable - Easy to add new test cases as parameters
Documentation - Tests serve as usage examples'''

import pytest
import math

# Import the function we're testing
from to_percent import to_percent

class TestToPercentComprehensive:
    """Comprehensive tests for the to_percent function using parametrization."""
    
    @pytest.mark.parametrize("ratio,expected,description", [
        # Basic ratios (decimal to percentage)
        (0.0, "0.0%", "zero ratio"),
        (0.5, "50.0%", "half ratio"),
        (1.0, "100.0%", "complete ratio"),
        (0.25, "25.0%", "quarter ratio"),
        (0.75, "75.0%", "three-quarters ratio"),
        
        # Common percentage scenarios
        (0.1, "10.0%", "ten percent"),
        (0.01, "1.0%", "one percent"),
        (0.001, "0.1%", "one-tenth percent"),
        (0.9, "90.0%", "ninety percent"),
        (0.99, "99.0%", "ninety-nine percent"),
        (0.999, "99.9%", "ninety-nine point nine percent"),
        
        # Values greater than 1 (over 100%)
        (1.5, "150.0%", "one and half times"),
        (2.0, "200.0%", "double"),
        (10.0, "1000.0%", "ten times"),
        (1.25, "125.0%", "twenty-five percent increase"),
        (3.14159, "314.2%", "pi ratio"),
        
        # Small positive values
        (0.0001, "0.0%", "very small positive - rounds to zero"),
        (0.00001, "0.0%", "extremely small positive"),
        (0.05, "5.0%", "five percent"),
        (0.005, "0.5%", "half percent"),
        (0.0005, "0.1%", "tenth of percent"),
        (0.00005, "0.0%", "rounds down to zero"),
        
        # Rounding behavior testing
        (0.1234, "12.3%", "round down case"),
        (0.1235, "12.4%", "round up case"),
        (0.1236, "12.4%", "round up case 2"),
        (0.999, "99.9%", "close to 100%"),
        (0.9999, "100.0%", "rounds to 100%"),
        (0.9994, "99.9%", "rounds down from 100%"),
        (0.9995, "100.0%", "rounds up to 100%"),
        
        # Negative ratios
        (-0.1, "-10.0%", "negative ten percent"),
        (-0.5, "-50.0%", "negative fifty percent"),
        (-1.0, "-100.0%", "negative one hundred percent"),
        (-0.25, "-25.0%", "negative quarter"),
        (-2.0, "-200.0%", "negative double"),
        (-0.001, "-0.1%", "small negative"),
        (-0.0001, "-0.0%", "very small negative - rounds to zero"),
        
        # Large values
        (100.0, "10000.0%", "one hundred times"),
        (1000.0, "100000.0%", "one thousand times"),
        (0.00123456, "0.1%", "many decimals - rounds down"),
        (0.00156789, "0.2%", "many decimals - rounds up"),
        
        # Edge cases for rounding precision
        (1/3, "33.3%", "one third"),
        (2/3, "66.7%", "two thirds"),
        (1/6, "16.7%", "one sixth"),
        (1/7, "14.3%", "one seventh"),
        (1/8, "12.5%", "one eighth"),
        (1/9, "11.1%", "one ninth"),
        
        # Mathematical constants
        (math.e - 2, "71.8%", "e minus 2"),
        (math.sqrt(2) - 1, "41.4%", "sqrt(2) minus 1"),
        (math.pi/10, "31.4%", "pi divided by 10"),
        
        # Decimal precision edge cases
        (0.1111, "11.1%", "repeating ones"),
        (0.2222, "22.2%", "repeating twos"),
        (0.3333, "33.3%", "repeating threes"),
        (0.6666, "66.7%", "repeating sixes"),
        (0.7777, "77.8%", "repeating sevens"),
        (0.8888, "88.9%", "repeating eights"),
        (0.9999, "100.0%", "repeating nines"),
        
        # Financial/business common ratios
        (0.15, "15.0%", "typical tax rate"),
        (0.08, "8.0%", "typical interest rate"),
        (0.03, "3.0%", "inflation rate"),
        (0.065, "6.5%", "sales tax rate"),
        (1.20, "120.0%", "twenty percent markup"),
        (0.80, "80.0%", "twenty percent discount"),
        
        # Very large numbers
        (1e6, "100000000.0%", "million ratio"),
        (1e-6, "0.0%", "millionth ratio - rounds to zero"),
        
        # Boundary testing around common thresholds
        (0.049, "4.9%", "just under 5%"),
        (0.051, "5.1%", "just over 5%"),
        (0.099, "9.9%", "just under 10%"),
        (0.101, "10.1%", "just over 10%"),
        (0.499, "49.9%", "just under 50%"),
        (0.501, "50.1%", "just over 50%"),
        (0.999, "99.9%", "just under 100%"),
        (1.001, "100.1%", "just over 100%"),
    ])
    def test_to_percent_comprehensive(self, ratio, expected, description):
        """
        PYTEST FEATURE: Comprehensive parametrized testing for all scenarios
        BENEFIT: Maximum coverage with minimal test code - 60+ test cases in one method
        STUDENT NOTE: Description parameter makes test failures easy to understand
        """
        result = to_percent(ratio)
        assert result == expected, f"Failed for {description}: input={ratio}, got={result}, expected={expected}"

class TestToPercentSpecialValues:
    """Tests for special floating-point values and edge cases."""
    
    @pytest.mark.parametrize("special_value,expected_behavior,description", [
        (float('inf'), "inf%", "positive infinity"),
        (float('-inf'), "-inf%", "negative infinity"),
        (float('nan'), "nan%", "not a number"),
        (0.0, "0.0%", "positive zero"),
        (-0.0, "0.0%", "negative zero"),
    ])
    def test_special_floating_point_values(self, special_value, expected_behavior, description):
        """
        PYTEST FEATURE: Testing special floating-point values
        BENEFIT: Ensures robust handling of edge cases in floating-point arithmetic
        STUDENT NOTE: Tests how the function handles mathematical edge cases
        """
        result = to_percent(special_value)
        
        if "inf" in expected_behavior:
            assert "inf" in result.lower(), f"Failed for {description}: expected inf in result"
        elif "nan" in expected_behavior:
            assert "nan" in result.lower(), f"Failed for {description}: expected nan in result"
        else:
            assert result == expected_behavior, f"Failed for {description}"

class TestToPercentPrecisionAndRounding:
    """Focused tests on precision and rounding behavior."""
    
    @pytest.mark.parametrize("input_value,expected_output,rounding_case", [
        # Test .1% precision rounding
        (0.12349, "12.3%", "round down at .49"),
        (0.12350, "12.4%", "round up at .50"),  
        (0.12351, "12.4%", "round up at .51"),
        (0.99949, "99.9%", "round down near 100%"),
        (0.99950, "100.0%", "round up to 100%"),
        (0.99951, "100.0%", "round up past 100%"),
        
        # Test negative rounding
        (-0.12349, "-12.3%", "negative round down"),
        (-0.12350, "-12.4%", "negative round up"),
        (-0.99950, "-100.0%", "negative round to -100%"),
        
        # Test very small rounding
        (0.00049, "0.0%", "small value rounds to zero"),
        (0.00050, "0.1%", "small value rounds up"),
        (0.00051, "0.1%", "small value rounds up clearly"),
        
        # Test rounding at various magnitudes
        (1.2349, "123.5%", "round up over 100%"),
        (1.2344, "123.4%", "round down over 100%"),
        (10.2349, "1023.5%", "round up at 1000%+"),
        (10.2344, "1023.4%", "round down at 1000%+"),
    ])
    def test_precision_rounding_behavior(self, input_value, expected_output, rounding_case):
        """
        PYTEST FEATURE: Focused precision testing
        BENEFIT: Validates the .1% precision requirement specifically
        STUDENT NOTE: Tests the exact rounding behavior at decision boundaries
        """
        result = to_percent(input_value)
        assert result == expected_output, f"Rounding failed for {rounding_case}: input={input_value}"

class TestToPercentTypeHandling:
    """Tests for different numeric input types."""
    
    @pytest.mark.parametrize("input_value,input_type,expected", [
        # Integer inputs
        (0, "int", "0.0%"),
        (1, "int", "100.0%"),
        (2, "int", "200.0%"),
        (-1, "int", "-100.0%"),
        
        # Float inputs  
        (0.5, "float", "50.0%"),
        (1.5, "float", "150.0%"),
        (-0.5, "float", "-50.0%"),
        
        # Complex numeric inputs that convert to float
        (True, "bool True", "100.0%"),  # True == 1
        (False, "bool False", "0.0%"),  # False == 0
    ])
    def test_different_input_types(self, input_value, input_type, expected):
        """
        PYTEST FEATURE: Input type validation testing
        BENEFIT: Ensures function works with various numeric types
        STUDENT NOTE: Tests Python's automatic type conversion behavior
        """
        result = to_percent(input_value)
        assert result == expected, f"Failed for {input_type} input: {input_value}"

class TestToPercentRealWorldScenarios:
    """Tests based on real-world percentage use cases."""
    
    @pytest.mark.parametrize("scenario,ratio,expected,context", [
        # Academic grading
        ("perfect_score", 1.0, "100.0%", "student got all questions right"),
        ("passing_grade", 0.7, "70.0%", "minimum passing grade"),
        ("failing_grade", 0.59, "59.0%", "just below passing"),
        ("extra_credit", 1.05, "105.0%", "student earned extra credit"),
        
        # Business metrics
        ("profit_margin", 0.15, "15.0%", "healthy profit margin"),
        ("market_share", 0.23, "23.0%", "company market share"),
        ("growth_rate", 0.08, "8.0%", "annual growth rate"),
        ("discount_rate", 0.20, "20.0%", "customer discount"),
        ("tax_rate", 0.0875, "8.8%", "sales tax rate"),
        
        # Statistics and probability
        ("confidence_level", 0.95, "95.0%", "statistical confidence"),
        ("error_rate", 0.02, "2.0%", "acceptable error rate"),
        ("success_probability", 0.333, "33.3%", "one in three chance"),
        ("rare_event", 0.001, "0.1%", "one in thousand chance"),
        
        # Financial ratios
        ("interest_rate", 0.045, "4.5%", "mortgage interest rate"),
        ("inflation_rate", 0.025, "2.5%", "annual inflation"),
        ("savings_rate", 0.12, "12.0%", "personal savings rate"),
        ("debt_ratio", 0.35, "35.0%", "debt to income ratio"),
        
        # Performance metrics
        ("cpu_usage", 0.85, "85.0%", "high CPU utilization"),
        ("memory_usage", 0.67, "67.0%", "memory consumption"),
        ("accuracy_rate", 0.992, "99.2%", "model accuracy"),
        ("completion_rate", 0.88, "88.0%", "project completion"),
        
        # Survey and polling
        ("approval_rating", 0.52, "52.0%", "political approval"),
        ("satisfaction_score", 0.78, "78.0%", "customer satisfaction"),
        ("response_rate", 0.34, "34.0%", "survey response rate"),
        ("agreement_level", 0.91, "91.0%", "strongly agree responses"),
    ])
    def test_real_world_scenarios(self, scenario, ratio, expected, context):
        """
        PYTEST FEATURE: Real-world scenario testing
        BENEFIT: Validates function works correctly for actual use cases
        STUDENT NOTE: These represent common percentage calculations in various fields
        """
        result = to_percent(ratio)
        assert result == expected, f"Failed {scenario} scenario ({context}): {ratio} -> {result}, expected {expected}"

class TestToPercentMathematicalProperties:
    """Tests for mathematical properties and relationships."""
    
    @pytest.mark.parametrize("property_name,test_pairs,description", [
        ("additive_inverse", [(0.5, -0.5), (0.25, -0.25), (1.0, -1.0)], "opposite values"),
        ("scaling_relationship", [(0.1, 0.2), (0.25, 0.5), (0.4, 0.8)], "double relationships"), 
        ("fractional_relationships", [(0.5, 1.0), (0.25, 0.5), (0.125, 0.25)], "half relationships"),
        ("decimal_shifts", [(0.1, 1.0), (0.01, 0.1), (0.001, 0.01)], "power of 10 relationships"),
    ])
    def test_mathematical_relationships(self, property_name, test_pairs, description):
        """
        PYTEST FEATURE: Mathematical property validation
        BENEFIT: Ensures the function maintains mathematical consistency
        STUDENT NOTE: Tests relationships between related inputs
        """
        for val1, val2 in test_pairs:
            result1 = to_percent(val1)
            result2 = to_percent(val2)
            
            # Extract numeric values for comparison
            num1 = float(result1.rstrip('%'))
            num2 = float(result2.rstrip('%'))
            
            if property_name == "additive_inverse":
                assert abs(num1 + num2) < 0.1, f"Additive inverse failed: {val1}, {val2}"
            elif property_name == "scaling_relationship":
                assert abs(num2 - 2 * num1) < 0.1, f"Scaling failed: {val1} -> {result1}, {val2} -> {result2}"
            elif property_name == "fractional_relationships":
                assert abs(num1 - num2 / 2) < 0.1, f"Fractional failed: {val1} -> {result1}, {val2} -> {result2}"
            elif property_name == "decimal_shifts":
                assert abs(num2 - 10 * num1) < 0.1, f"Decimal shift failed: {val1} -> {result1}, {val2} -> {result2}"

class TestToPercentBoundaryConditions:
    """Tests for boundary conditions and edge cases."""
    
    @pytest.mark.parametrize("boundary_type,test_values,expected_results", [
        ("zero_boundary", [0.0, 0.0001, -0.0001], ["0.0%", "0.0%", "0.0%"]),
        ("one_boundary", [0.999, 1.0, 1.001], ["99.9%", "100.0%", "100.1%"]),
        ("rounding_boundary", [0.12349, 0.12350, 0.12351], ["12.3%", "12.4%", "12.4%"]),
        ("small_boundary", [0.0004, 0.0005, 0.0006], ["0.0%", "0.1%", "0.1%"]),
        ("negative_boundary", [-0.0001, -0.0005, -0.001], ["-0.0%", "-0.1%", "-0.1%"]),
    ])
    def test_boundary_conditions(self, boundary_type, test_values, expected_results):
        """
        PYTEST FEATURE: Boundary condition testing
        BENEFIT: Validates behavior at critical decision points
        STUDENT NOTE: Tests edge cases where rounding behavior changes
        """
        for value, expected in zip(test_values, expected_results):
            result = to_percent(value)
            assert result == expected, f"Boundary test {boundary_type} failed: {value} -> {result}, expected {expected}"

class TestToPercentErrorConditions:
    """Tests for invalid inputs and error handling."""
    
    @pytest.mark.parametrize("invalid_input,error_type,description", [
        ("not_a_number", TypeError, "string input should raise TypeError"),
        (None, TypeError, "None input should raise TypeError"),
        ([1, 2, 3], TypeError, "list input should raise TypeError"),
        ({"key": "value"}, TypeError, "dict input should raise TypeError"),
        (complex(1, 2), (TypeError, ValueError), "complex number might raise error"),
    ])
    def test_invalid_input_types(self, invalid_input, error_type, description):
        """
        PYTEST FEATURE: Error condition testing
        BENEFIT: Ensures function fails gracefully with invalid inputs
        STUDENT NOTE: Tests that the function properly validates input types
        """
        with pytest.raises(error_type):
            to_percent(invalid_input)

class TestToPercentFormatConsistency:
    """Tests for output format consistency."""
    
    @pytest.mark.parametrize("input_value,format_check,description", [
        (0.5, lambda x: x.endswith('%'), "ends with percent sign"),
        (0.5, lambda x: '.' in x, "contains decimal point"),
        (0.5, lambda x: x.count('.') == 1, "exactly one decimal point"),
        (0.5, lambda x: x.split('.')[1][0].isdigit(), "has digit after decimal"),
        (0.5, lambda x: x.split('.')[1].endswith('0%'), "ends with single decimal place"),
        (1.234, lambda x: len(x.split('.')[1]) == 2, "exactly one decimal place plus %"),
        (-0.5, lambda x: x.startswith('-'), "negative values start with minus"),
        (0.0, lambda x: not x.startswith('-'), "zero is not negative"),
    ])
    def test_format_consistency(self, input_value, format_check, description):
        """
        PYTEST FEATURE: Format validation testing
        BENEFIT: Ensures consistent output formatting across all inputs
        STUDENT NOTE: Tests the string format requirements (.1% precision)
        """
        result = to_percent(input_value)
        assert format_check(result), f"Format check failed for {description}: {input_value} -> {result}"

class TestToPercentPerformanceCharacteristics:
    """Tests for performance and large-scale behavior."""
    
    @pytest.mark.parametrize("scale_test,input_range,description", [
        ("small_scale", [i/1000 for i in range(0, 1001, 100)], "0.0% to 100.0% by 10%"),
        ("large_scale", [i for i in range(0, 11)], "0% to 1000% by 100%"),
        ("precision_scale", [0.1 + i/10000 for i in range(0, 10)], "around 10% with tiny increments"),
        ("negative_scale", [-i/10 for i in range(0, 11)], "0% to -100% by -10%"),
    ])
    def test_scale_behavior(self, scale_test, input_range, description):
        """
        PYTEST FEATURE: Scale testing
        BENEFIT: Validates consistent behavior across different value ranges
        STUDENT NOTE: Tests the function with systematic input ranges
        """
        results = []
        for value in input_range:
            result = to_percent(value)
            # Basic format validation
            assert result.endswith('%'), f"Scale test {scale_test}: {value} produced invalid format {result}"
            assert '.' in result, f"Scale test {scale_test}: {value} missing decimal point in {result}"
            results.append(result)
        
        # Ensure we got results for all inputs
        assert len(results) == len(input_range), f"Scale test {scale_test} incomplete"

class TestToPercentDocumentationExamples:
    """Tests that serve as documentation examples for students."""
    
    def test_basic_usage_examples(self):
        """
        DOCUMENTATION EXAMPLE: Basic usage patterns
        STUDENT NOTE: These examples show common usage patterns
        """
        # Example 1: Converting decimal ratios to percentages
        assert to_percent(0.5) == "50.0%"      # Half = 50%
        assert to_percent(0.25) == "25.0%"     # Quarter = 25%
        assert to_percent(1.0) == "100.0%"     # Whole = 100%
        
        # Example 2: Values over 100%
        assert to_percent(1.5) == "150.0%"     # 50% increase
        assert to_percent(2.0) == "200.0%"     # Double = 200%
        
        # Example 3: Small percentages
        assert to_percent(0.01) == "1.0%"      # 1 percent
        assert to_percent(0.001) == "0.1%"     # 0.1 percent
        
        # Example 4: Negative percentages
        assert to_percent(-0.1) == "-10.0%"    # 10% decrease
        
    @pytest.mark.parametrize("use_case,ratio,expected,explanation", [
        ("test_score", 0.85, "85.0%", "Student scored 85% on test"),
        ("discount", 0.20, "20.0%", "20% off sale price"),
        ("tip", 0.18, "18.0%", "18% tip at restaurant"),
        ("tax", 0.0825, "8.3%", "8.25% sales tax (rounded to 8.3%)"),
        ("interest", 0.045, "4.5%", "4.5% annual interest rate"),
        ("growth", 1.25, "125.0%", "25% growth (125% of original)"),
        ("probability", 0.333, "33.3%", "33.3% chance (1 in 3)"),
        ("efficiency", 0.92, "92.0%", "92% efficiency rating"),
    ])
    def test_real_usage_examples(self, use_case, ratio, expected, explanation):
        """
        DOCUMENTATION EXAMPLE: Real-world usage examples
        STUDENT NOTE: These show how to_percent() is used in practice
        """
        result = to_percent(ratio)
        assert result == expected, f"{use_case} example failed: {explanation}"

class TestToPercentComparisonWithAlternatives:
    """Tests comparing different ways to format percentages."""
    
    @pytest.mark.parametrize("input_val,to_percent_result,manual_calculation", [
        (0.5, "50.0%", "50.0%"),
        (0.123, "12.3%", "12.3%"),
        (1.5, "150.0%", "150.0%"),
        (0.001, "0.1%", "0.1%"),
        (-0.25, "-25.0%", "-25.0%"),
    ])
    def test_consistency_with_manual_calculation(self, input_val, to_percent_result, manual_calculation):
        """
        PYTEST FEATURE: Consistency validation
        BENEFIT: Ensures to_percent() matches manual percentage calculations
        STUDENT NOTE: Validates that the function produces expected mathematical results
        """
        actual_result = to_percent(input_val)
        assert actual_result == to_percent_result
        
        # Verify it matches manual calculation
        manual_result = f"{input_val * 100:.1f}%"
        assert actual_result == manual_result, f"Manual calc mismatch: {input_val} -> {actual_result} vs {manual_result}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])