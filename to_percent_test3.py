# test_to_percent_with_ids.py
'''
EDUCATIONAL COMPARISON: pytest.param with IDs vs Basic Parametrization

This file demonstrates the ENHANCED version using pytest.param with IDs.
Compare this with the original to_percent_test2.py to see the differences.

KEY LEARNING POINTS:
1. pytest.param allows custom test IDs for better readability
2. Test output becomes much clearer and easier to debug
3. Selective test running becomes possible with meaningful names
4. Organized IDs help group related test cases logically
5. Better CI/CD integration with actionable test names

BENEFITS OF IDs:
- test_comprehensive[zero] vs test_comprehensive[0.0-0.0%-zero ratio]
- Easy selective running: pytest -k "rounding" or pytest -k "business"
- Clearer failure reports in CI/CD pipelines
- Logical grouping of test scenarios
'''

import pytest
import math

# Import the function we're testing
from to_percent import to_percent

class TestToPercentComprehensive:
    """Comprehensive tests using pytest.param with meaningful IDs."""
    
    @pytest.mark.parametrize("ratio,expected,description", [
        # STUDENT NOTE: Compare these clean IDs with the original verbose parameter display
        
        # Basic ratios - grouped with simple, memorable IDs
        pytest.param(0.0, "0.0%", "zero ratio", id="zero"),
        pytest.param(0.5, "50.0%", "half ratio", id="half"),
        pytest.param(1.0, "100.0%", "complete ratio", id="complete"),
        pytest.param(0.25, "25.0%", "quarter ratio", id="quarter"),
        pytest.param(0.75, "75.0%", "three-quarters ratio", id="three_quarters"),
        
        # Common percentages - organized by percentage value
        pytest.param(0.1, "10.0%", "ten percent", id="10_pct"),
        pytest.param(0.01, "1.0%", "one percent", id="1_pct"),
        pytest.param(0.001, "0.1%", "one-tenth percent", id="0_1_pct"),
        pytest.param(0.9, "90.0%", "ninety percent", id="90_pct"),
        pytest.param(0.99, "99.0%", "ninety-nine percent", id="99_pct"),
        pytest.param(0.999, "99.9%", "ninety-nine point nine percent", id="99_9_pct"),
        
        # Values over 100% - clear progression IDs
        pytest.param(1.5, "150.0%", "one and half times", id="150_pct"),
        pytest.param(2.0, "200.0%", "double", id="double"),
        pytest.param(10.0, "1000.0%", "ten times", id="1000_pct"),
        pytest.param(1.25, "125.0%", "twenty-five percent increase", id="125_pct"),
        pytest.param(3.14159, "314.2%", "pi ratio", id="pi_ratio"),
        
        # Small values - organized by magnitude
        pytest.param(0.0001, "0.0%", "very small positive - rounds to zero", id="tiny_rounds_zero"),
        pytest.param(0.00001, "0.0%", "extremely small positive", id="micro_rounds_zero"),
        pytest.param(0.05, "5.0%", "five percent", id="5_pct"),
        pytest.param(0.005, "0.5%", "half percent", id="half_pct"),
        pytest.param(0.0005, "0.1%", "tenth of percent", id="tenth_pct"),
        pytest.param(0.00005, "0.0%", "rounds down to zero", id="nano_rounds_zero"),
        
        # Rounding behavior - grouped by rounding scenario
        pytest.param(0.1234, "12.3%", "round down case", id="round_down_12_3"),
        pytest.param(0.1235, "12.4%", "round up case", id="round_up_12_4"),
        pytest.param(0.1236, "12.4%", "round up case 2", id="round_up_12_4_clear"),
        pytest.param(0.999, "99.9%", "close to 100%", id="close_to_100"),
        pytest.param(0.9999, "100.0%", "rounds to 100%", id="rounds_to_100"),
        pytest.param(0.9994, "99.9%", "rounds down from 100%", id="down_from_100"),
        pytest.param(0.9995, "100.0%", "rounds up to 100%", id="up_to_100"),
        
        # Negative values - systematic negative IDs
        pytest.param(-0.1, "-10.0%", "negative ten percent", id="neg_10"),
        pytest.param(-0.5, "-50.0%", "negative fifty percent", id="neg_50"),
        pytest.param(-1.0, "-100.0%", "negative one hundred percent", id="neg_100"),
        pytest.param(-0.25, "-25.0%", "negative quarter", id="neg_quarter"),
        pytest.param(-2.0, "-200.0%", "negative double", id="neg_double"),
        pytest.param(-0.001, "-0.1%", "small negative", id="neg_small"),
        pytest.param(-0.0001, "-0.0%", "very small negative - rounds to zero", id="neg_tiny_zero"),
        
        # Large values - magnitude-based IDs
        pytest.param(100.0, "10000.0%", "one hundred times", id="hundred_x"),
        pytest.param(1000.0, "100000.0%", "one thousand times", id="thousand_x"),
        pytest.param(0.00123456, "0.1%", "many decimals - rounds down", id="many_dec_down"),
        pytest.param(0.00156789, "0.2%", "many decimals - rounds up", id="many_dec_up"),
        
        # Mathematical fractions - fraction-based IDs
        pytest.param(1/3, "33.3%", "one third", id="one_third"),
        pytest.param(2/3, "66.7%", "two thirds", id="two_thirds"),
        pytest.param(1/6, "16.7%", "one sixth", id="one_sixth"),
        pytest.param(1/7, "14.3%", "one seventh", id="one_seventh"),
        pytest.param(1/8, "12.5%", "one eighth", id="one_eighth"),
        pytest.param(1/9, "11.1%", "one ninth", id="one_ninth"),
        
        # Mathematical constants - constant-based IDs
        pytest.param(math.e - 2, "71.8%", "e minus 2", id="e_minus_2"),
        pytest.param(math.sqrt(2) - 1, "41.4%", "sqrt(2) minus 1", id="sqrt2_minus_1"),
        pytest.param(math.pi/10, "31.4%", "pi divided by 10", id="pi_over_10"),
        
        # Decimal precision patterns - pattern-based IDs
        pytest.param(0.1111, "11.1%", "repeating ones", id="repeat_1"),
        pytest.param(0.2222, "22.2%", "repeating twos", id="repeat_2"),
        pytest.param(0.3333, "33.3%", "repeating threes", id="repeat_3"),
        pytest.param(0.6666, "66.7%", "repeating sixes", id="repeat_6"),
        pytest.param(0.7777, "77.8%", "repeating sevens", id="repeat_7"),
        pytest.param(0.8888, "88.9%", "repeating eights", id="repeat_8"),
        pytest.param(0.9999, "100.0%", "repeating nines", id="repeat_9"),
        
        # Business/Financial scenarios - domain-specific IDs
        pytest.param(0.15, "15.0%", "typical tax rate", id="tax_rate"),
        pytest.param(0.08, "8.0%", "typical interest rate", id="interest_rate"),
        pytest.param(0.03, "3.0%", "inflation rate", id="inflation"),
        pytest.param(0.065, "6.5%", "sales tax rate", id="sales_tax"),
        pytest.param(1.20, "120.0%", "twenty percent markup", id="markup_20"),
        pytest.param(0.80, "80.0%", "twenty percent discount", id="discount_20"),
        
        # Scientific notation - sci notation IDs
        pytest.param(1e6, "100000000.0%", "million ratio", id="million"),
        pytest.param(1e-6, "0.0%", "millionth ratio - rounds to zero", id="millionth"),
        
        # Boundary testing - boundary-specific IDs
        pytest.param(0.049, "4.9%", "just under 5%", id="under_5"),
        pytest.param(0.051, "5.1%", "just over 5%", id="over_5"),
        pytest.param(0.099, "9.9%", "just under 10%", id="under_10"),
        pytest.param(0.101, "10.1%", "just over 10%", id="over_10"),
        pytest.param(0.499, "49.9%", "just under 50%", id="under_50"),
        pytest.param(0.501, "50.1%", "just over 50%", id="over_50"),
        pytest.param(0.999, "99.9%", "just under 100%", id="under_100"),
        pytest.param(1.001, "100.1%", "just over 100%", id="over_100"),
    ])
    def test_to_percent_comprehensive(self, ratio, expected, description):
        """
        EDUCATIONAL COMPARISON: Notice how pytest.param with IDs makes test output cleaner
        
        WITHOUT IDs: test_comprehensive[0.1234-12.3%-round down case] 
        WITH IDs:    test_comprehensive[round_down_12_3]
        
        STUDENT BENEFIT: Much easier to identify failing tests and run specific scenarios
        """
        result = to_percent(ratio)
        assert result == expected, f"Failed for {description}: input={ratio}, got={result}, expected={expected}"

class TestToPercentSpecialValues:
    """Special floating-point values with descriptive IDs."""
    
    @pytest.mark.parametrize("special_value,expected_behavior,description", [
        pytest.param(float('inf'), "inf%", "positive infinity", id="pos_infinity"),
        pytest.param(float('-inf'), "-inf%", "negative infinity", id="neg_infinity"),
        pytest.param(float('nan'), "nan%", "not a number", id="nan"),
        pytest.param(0.0, "0.0%", "positive zero", id="pos_zero"),
        pytest.param(-0.0, "0.0%", "negative zero", id="neg_zero"),
    ])
    def test_special_floating_point_values(self, special_value, expected_behavior, description):
        """
        EDUCATIONAL NOTE: Compare test names:
        BEFORE: test_special_floating_point_values[inf-inf%-positive infinity]
        AFTER:  test_special_floating_point_values[pos_infinity]
        """
        result = to_percent(special_value)
        
        if "inf" in expected_behavior:
            assert "inf" in result.lower(), f"Failed for {description}: expected inf in result"
        elif "nan" in expected_behavior:
            assert "nan" in result.lower(), f"Failed for {description}: expected nan in result"
        else:
            assert result == expected_behavior, f"Failed for {description}"

class TestToPercentPrecisionAndRounding:
    """Rounding behavior tests with precision-focused IDs."""
    
    @pytest.mark.parametrize("input_value,expected_output,rounding_case", [
        # Rounding at .1% precision - organized by rounding direction
        pytest.param(0.12349, "12.3%", "round down at .49", id="down_at_49"),
        pytest.param(0.12350, "12.4%", "round up at .50", id="up_at_50"),  
        pytest.param(0.12351, "12.4%", "round up at .51", id="up_at_51"),
        pytest.param(0.99949, "99.9%", "round down near 100%", id="near_100_down"),
        pytest.param(0.99950, "100.0%", "round up to 100%", id="to_100_up"),
        pytest.param(0.99951, "100.0%", "round up past 100%", id="past_100_up"),
        
        # Negative rounding - negative rounding IDs
        pytest.param(-0.12349, "-12.3%", "negative round down", id="neg_down_49"),
        pytest.param(-0.12350, "-12.4%", "negative round up", id="neg_up_50"),
        pytest.param(-0.99950, "-100.0%", "negative round to -100%", id="neg_to_100"),
        
        # Small value rounding - small value IDs
        pytest.param(0.00049, "0.0%", "small value rounds to zero", id="small_to_zero"),
        pytest.param(0.00050, "0.1%", "small value rounds up", id="small_up"),
        pytest.param(0.00051, "0.1%", "small value rounds up clearly", id="small_up_clear"),
        
        # Large magnitude rounding - magnitude-based IDs
        pytest.param(1.2349, "123.5%", "round up over 100%", id="over_100_up"),
        pytest.param(1.2344, "123.4%", "round down over 100%", id="over_100_down"),
        pytest.param(10.2349, "1023.5%", "round up at 1000%+", id="over_1000_up"),
        pytest.param(10.2344, "1023.4%", "round down at 1000%+", id="over_1000_down"),
    ])
    def test_precision_rounding_behavior(self, input_value, expected_output, rounding_case):
        """
        EDUCATIONAL ADVANTAGE: Selective testing becomes powerful
        Run only rounding tests: pytest -k "rounding"
        Run only up-rounding: pytest -k "up"
        Run only down-rounding: pytest -k "down"
        """
        result = to_percent(input_value)
        assert result == expected_output, f"Rounding failed for {rounding_case}: input={input_value}"

class TestToPercentTypeHandling:
    """Type handling tests with type-specific IDs."""
    
    @pytest.mark.parametrize("input_value,input_type,expected", [
        # Integer inputs - int-based IDs
        pytest.param(0, "int", "0.0%", id="int_zero"),
        pytest.param(1, "int", "100.0%", id="int_one"),
        pytest.param(2, "int", "200.0%", id="int_two"),
        pytest.param(-1, "int", "-100.0%", id="int_neg_one"),
        
        # Float inputs - float-based IDs
        pytest.param(0.5, "float", "50.0%", id="float_half"),
        pytest.param(1.5, "float", "150.0%", id="float_one_half"),
        pytest.param(-0.5, "float", "-50.0%", id="float_neg_half"),
        
        # Boolean inputs - bool-based IDs
        pytest.param(True, "bool True", "100.0%", id="bool_true"),
        pytest.param(False, "bool False", "0.0%", id="bool_false"),
    ])
    def test_different_input_types(self, input_value, input_type, expected):
        """
        EDUCATIONAL BENEFIT: Type-specific IDs make it easy to test specific types
        Run only integer tests: pytest -k "int"
        Run only boolean tests: pytest -k "bool"
        """
        result = to_percent(input_value)
        assert result == expected, f"Failed for {input_type} input: {input_value}"

class TestToPercentRealWorldScenarios:
    """Real-world scenarios with domain-specific IDs."""
    
    @pytest.mark.parametrize("scenario,ratio,expected,context", [
        # Academic grading - academic domain IDs
        pytest.param("perfect_score", 1.0, "100.0%", "student got all questions right", id="academic_perfect"),
        pytest.param("passing_grade", 0.7, "70.0%", "minimum passing grade", id="academic_passing"),
        pytest.param("failing_grade", 0.59, "59.0%", "just below passing", id="academic_failing"),
        pytest.param("extra_credit", 1.05, "105.0%", "student earned extra credit", id="academic_extra_credit"),
        
        # Business metrics - business domain IDs
        pytest.param("profit_margin", 0.15, "15.0%", "healthy profit margin", id="business_profit"),
        pytest.param("market_share", 0.23, "23.0%", "company market share", id="business_market_share"),
        pytest.param("growth_rate", 0.08, "8.0%", "annual growth rate", id="business_growth"),
        pytest.param("discount_rate", 0.20, "20.0%", "customer discount", id="business_discount"),
        pytest.param("tax_rate", 0.0875, "8.8%", "sales tax rate", id="business_tax"),
        
        # Statistics and probability - stats domain IDs
        pytest.param("confidence_level", 0.95, "95.0%", "statistical confidence", id="stats_confidence"),
        pytest.param("error_rate", 0.02, "2.0%", "acceptable error rate", id="stats_error"),
        pytest.param("success_probability", 0.333, "33.3%", "one in three chance", id="stats_probability"),
        pytest.param("rare_event", 0.001, "0.1%", "one in thousand chance", id="stats_rare_event"),
        
        # Financial ratios - finance domain IDs
        pytest.param("interest_rate", 0.045, "4.5%", "mortgage interest rate", id="finance_interest"),
        pytest.param("inflation_rate", 0.025, "2.5%", "annual inflation", id="finance_inflation"),
        pytest.param("savings_rate", 0.12, "12.0%", "personal savings rate", id="finance_savings"),
        pytest.param("debt_ratio", 0.35, "35.0%", "debt to income ratio", id="finance_debt"),
        
        # Performance metrics - performance domain IDs
        pytest.param("cpu_usage", 0.85, "85.0%", "high CPU utilization", id="perf_cpu"),
        pytest.param("memory_usage", 0.67, "67.0%", "memory consumption", id="perf_memory"),
        pytest.param("accuracy_rate", 0.992, "99.2%", "model accuracy", id="perf_accuracy"),
        pytest.param("completion_rate", 0.88, "88.0%", "project completion", id="perf_completion"),
        
        # Survey and polling - survey domain IDs
        pytest.param("approval_rating", 0.52, "52.0%", "political approval", id="survey_approval"),
        pytest.param("satisfaction_score", 0.78, "78.0%", "customer satisfaction", id="survey_satisfaction"),
        pytest.param("response_rate", 0.34, "34.0%", "survey response rate", id="survey_response"),
        pytest.param("agreement_level", 0.91, "91.0%", "strongly agree responses", id="survey_agreement"),
    ])
    def test_real_world_scenarios(self, scenario, ratio, expected, context):
        """
        EDUCATIONAL ADVANTAGE: Domain-specific IDs enable targeted testing
        Run only business tests: pytest -k "business"
        Run only academic tests: pytest -k "academic"
        Run only finance tests: pytest -k "finance"
        """
        result = to_percent(ratio)
        assert result == expected, f"Failed {scenario} scenario ({context}): {ratio} -> {result}, expected {expected}"

class TestToPercentMathematicalProperties:
    """Mathematical relationship tests with property-specific IDs."""
    
    @pytest.mark.parametrize("property_name,test_pairs,description", [
        pytest.param("additive_inverse", [(0.5, -0.5), (0.25, -0.25), (1.0, -1.0)], "opposite values", id="additive_inverse"),
        pytest.param("scaling_relationship", [(0.1, 0.2), (0.25, 0.5), (0.4, 0.8)], "double relationships", id="scaling_double"), 
        pytest.param("fractional_relationships", [(0.5, 1.0), (0.25, 0.5), (0.125, 0.25)], "half relationships", id="fractional_half"),
        pytest.param("decimal_shifts", [(0.1, 1.0), (0.01, 0.1), (0.001, 0.01)], "power of 10 relationships", id="decimal_power10"),
    ])
    def test_mathematical_relationships(self, property_name, test_pairs, description):
        """
        EDUCATIONAL BENEFIT: Property-specific IDs for mathematical testing
        Run only scaling tests: pytest -k "scaling"
        Run only fractional tests: pytest -k "fractional"
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
    """Boundary condition tests with boundary-specific IDs."""
    
    @pytest.mark.parametrize("boundary_type,test_values,expected_results", [
        pytest.param("zero_boundary", [0.0, 0.0001, -0.0001], ["0.0%", "0.0%", "0.0%"], id="boundary_zero"),
        pytest.param("one_boundary", [0.999, 1.0, 1.001], ["99.9%", "100.0%", "100.1%"], id="boundary_one"),
        pytest.param("rounding_boundary", [0.12349, 0.12350, 0.12351], ["12.3%", "12.4%", "12.4%"], id="boundary_rounding"),
        pytest.param("small_boundary", [0.0004, 0.0005, 0.0006], ["0.0%", "0.1%", "0.1%"], id="boundary_small"),
        pytest.param("negative_boundary", [-0.0001, -0.0005, -0.001], ["-0.0%", "-0.1%", "-0.1%"], id="boundary_negative"),
    ])
    def test_boundary_conditions(self, boundary_type, test_values, expected_results):
        """
        EDUCATIONAL ADVANTAGE: Boundary-specific IDs for edge case testing
        Run only zero boundary tests: pytest -k "boundary_zero"
        Run only rounding boundary tests: pytest -k "boundary_rounding"
        """
        for value, expected in zip(test_values, expected_results):
            result = to_percent(value)
            assert result == expected, f"Boundary test {boundary_type} failed: {value} -> {result}, expected {expected}"

class TestToPercentErrorConditions:
    """Error condition tests with error-type IDs."""
    
    @pytest.mark.parametrize("invalid_input,error_type,description", [
        pytest.param("not_a_number", TypeError, "string input should raise TypeError", id="error_string"),
        pytest.param(None, TypeError, "None input should raise TypeError", id="error_none"),
        pytest.param([1, 2, 3], TypeError, "list input should raise TypeError", id="error_list"),
        pytest.param({"key": "value"}, TypeError, "dict input should raise TypeError", id="error_dict"),
        pytest.param(complex(1, 2), (TypeError, ValueError), "complex number might raise error", id="error_complex"),
    ])
    def test_invalid_input_types(self, invalid_input, error_type, description):
        """
        EDUCATIONAL BENEFIT: Error-type IDs for systematic error testing
        Run only error tests: pytest -k "error"
        Run specific error types: pytest -k "error_string"
        """
        with pytest.raises(error_type):
            to_percent(invalid_input)

class TestToPercentFormatConsistency:
    """Format consistency tests with format-specific IDs."""
    
    @pytest.mark.parametrize("input_value,format_check,description", [
        pytest.param(0.5, lambda x: x.endswith('%'), "ends with percent sign", id="format_ends_percent"),
        pytest.param(0.5, lambda x: '.' in x, "contains decimal point", id="format_has_decimal"),
        pytest.param(0.5, lambda x: x.count('.') == 1, "exactly one decimal point", id="format_one_decimal"),
        pytest.param(0.5, lambda x: x.split('.')[1][0].isdigit(), "has digit after decimal", id="format_digit_after_decimal"),
        pytest.param(0.5, lambda x: x.split('.')[1].endswith('0%'), "ends with single decimal place", id="format_single_decimal"),
        pytest.param(1.234, lambda x: len(x.split('.')[1]) == 2, "exactly one decimal place plus %", id="format_precision_check"),
        pytest.param(-0.5, lambda x: x.startswith('-'), "negative values start with minus", id="format_negative_sign"),
        pytest.param(0.0, lambda x: not x.startswith('-'), "zero is not negative", id="format_zero_not_negative"),
    ])
    def test_format_consistency(self, input_value, format_check, description):
        """
        EDUCATIONAL ADVANTAGE: Format-specific IDs for format validation
        Run only format tests: pytest -k "format"
        Run only decimal format tests: pytest -k "format_decimal"
        """
        result = to_percent(input_value)
        assert format_check(result), f"Format check failed for {description}: {input_value} -> {result}"

class TestToPercentPerformanceCharacteristics:
    """Performance tests with scale-specific IDs."""
    
    @pytest.mark.parametrize("scale_test,input_range,description", [
        pytest.param("small_scale", [i/1000 for i in range(0, 1001, 100)], "0.0% to 100.0% by 10%", id="scale_small"),
        pytest.param("large_scale", [i for i in range(0, 11)], "0% to 1000% by 100%", id="scale_large"),
        pytest.param("precision_scale", [0.1 + i/10000 for i in range(0, 10)], "around 10% with tiny increments", id="scale_precision"),
        pytest.param("negative_scale", [-i/10 for i in range(0, 11)], "0% to -100% by -10%", id="scale_negative"),
    ])
    def test_scale_behavior(self, scale_test, input_range, description):
        """
        EDUCATIONAL BENEFIT: Scale-specific IDs for performance testing
        Run only large scale tests: pytest -k "scale_large"
        Run only precision tests: pytest -k "scale_precision"
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
    """Documentation examples with usage-specific IDs."""
    
    def test_basic_usage_examples(self):
        """
        DOCUMENTATION EXAMPLE: Basic usage patterns without parametrization
        STUDENT NOTE: Sometimes simple assertions are clearer than parametrized tests
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
        pytest.param("test_score", 0.85, "85.0%", "Student scored 85% on test", id="usage_test_score"),
        pytest.param("discount", 0.20, "20.0%", "20% off sale price", id="usage_discount"),
        pytest.param("tip", 0.18, "18.0%", "18% tip at restaurant", id="usage_tip"),
        pytest.param("tax", 0.0825, "8.3%", "8.25% sales tax (rounded to 8.3%)", id="usage_tax"),
        pytest.param("interest", 0.045, "4.5%", "4.5% annual interest rate", id="usage_interest"),
        pytest.param("growth", 1.25, "125.0%", "25% growth (125% of original)", id="usage_growth"),
        pytest.param("probability", 0.333, "33.3%", "33.3% chance (1 in 3)", id="usage_probability"),
        pytest.param("efficiency", 0.92, "92.0%", "92% efficiency rating", id="usage_efficiency"),
    ])
    def test_real_usage_examples(self, use_case, ratio, expected, explanation):
        """
        EDUCATIONAL ADVANTAGE: Usage-specific IDs for real-world examples
        Run only usage examples: pytest -k "usage"
        Run specific usage: pytest -k "usage_discount"
        """
        result = to_percent(ratio)
        assert result == expected, f"{use_case} example failed: {explanation}"

class TestToPercentComparisonWithAlternatives:
    """Comparison tests with calculation-specific IDs."""
    
    @pytest.mark.parametrize("input_val,to_percent_result,manual_calculation", [
        pytest.param(0.5, "50.0%", "50.0%", id="compare_half"),
        pytest.param(0.123, "12.3%", "12.3%", id="compare_decimal"),
        pytest.param(1.5, "150.0%", "150.0%", id="compare_over_100"),
        pytest.param(0.001, "0.1%", "0.1%", id="compare_small"),
        pytest.param(-0.25, "-25.0%", "-25.0%", id="compare_negative"),
    ])
    def test_consistency_with_manual_calculation(self, input_val, to_percent_result, manual_calculation):
        """
        EDUCATIONAL BENEFIT: Comparison-specific IDs for validation testing
        Run only comparison tests: pytest -k "compare"
        Run specific comparisons: pytest -k "compare_negative"
        """
        actual_result = to_percent(input_val)
        assert actual_result == to_percent_result
        
        # Verify it matches manual calculation
        manual_result = f"{input_val * 100:.1f}%"
        assert actual_result == manual_result, f"Manual calc mismatch: {input_val} -> {actual_result} vs {manual_result}"

class TestToPercentSelectiveRunningExamples:
    """
    EDUCATIONAL DEMONSTRATION: How pytest.param IDs enable selective test running
    
    STUDENT LEARNING: This class shows the power of well-chosen IDs for selective testing
    """
    
    @pytest.mark.parametrize("scenario,input_val,expected", [
        # Critical business scenarios
        pytest.param("profit_margin", 0.15, "15.0%", id="critical_profit"),
        pytest.param("error_rate", 0.02, "2.0%", id="critical_error"),
        pytest.param("success_rate", 0.95, "95.0%", id="critical_success"),
        
        # Edge case scenarios
        pytest.param("boundary_zero", 0.0001, "0.0%", id="edge_tiny"),
        pytest.param("boundary_hundred", 0.9995, "100.0%", id="edge_rounds_100"),
        pytest.param("boundary_negative", -0.0001, "-0.0%", id="edge_neg_tiny"),
        
        # Regression test scenarios
        pytest.param("regression_pi", math.pi/10, "31.4%", id="regression_pi"),
        pytest.param("regression_third", 1/3, "33.3%", id="regression_fraction"),
        pytest.param("regression_large", 1e6, "100000000.0%", id="regression_huge"),
    ])
    def test_selective_running_examples(self, scenario, input_val, expected):
        """
        EDUCATIONAL EXAMPLES of selective test running:
        
        pytest -k "critical"     # Run only critical business tests
        pytest -k "edge"         # Run only edge case tests  
        pytest -k "regression"   # Run only regression tests
        pytest -k "critical_profit" # Run specific profit test
        pytest -k "edge and tiny"   # Run edge cases with tiny values
        pytest -k "not regression"  # Skip regression tests
        """
        result = to_percent(input_val)
        assert result == expected, f"Selective running example failed: {scenario}"

class TestToPercentAdvancedIDPatterns:
    """
    EDUCATIONAL DEMONSTRATION: Advanced ID naming patterns for complex scenarios
    
    STUDENT LEARNING: Shows sophisticated ID strategies for large test suites
    """
    
    @pytest.mark.parametrize("input_val,expected,category,subcategory", [
        # Hierarchical ID pattern: category_subcategory_specific
        pytest.param(0.05, "5.0%", "business", "tax", id="biz_tax_5pct"),
        pytest.param(0.08, "8.0%", "business", "interest", id="biz_interest_8pct"),
        pytest.param(0.15, "15.0%", "business", "profit", id="biz_profit_15pct"),
        
        pytest.param(0.70, "70.0%", "academic", "passing", id="acad_pass_70pct"),
        pytest.param(0.95, "95.0%", "academic", "excellent", id="acad_excel_95pct"),
        pytest.param(1.05, "105.0%", "academic", "bonus", id="acad_bonus_105pct"),
        
        pytest.param(0.001, "0.1%", "technical", "precision", id="tech_prec_0_1pct"),
        pytest.param(1e-6, "0.0%", "technical", "tiny", id="tech_tiny_micro"),
        pytest.param(1e6, "100000000.0%", "technical", "huge", id="tech_huge_million"),
    ])
    def test_advanced_id_patterns(self, input_val, expected, category, subcategory):
        """
        EDUCATIONAL EXAMPLES of advanced selective running:
        
        pytest -k "biz"          # All business scenarios
        pytest -k "acad"         # All academic scenarios  
        pytest -k "tech"         # All technical scenarios
        pytest -k "tax"          # All tax-related tests
        pytest -k "biz and tax"  # Business tax tests only
        pytest -k "acad and pass" # Academic passing tests
        pytest -k "tech and huge" # Technical large value tests
        """
        result = to_percent(input_val)
        assert result == expected, f"Advanced pattern test failed: {category}/{subcategory}"

# EDUCATIONAL SUMMARY SECTION
class TestToPercentEducationalComparison:
    """
    EDUCATIONAL COMPARISON: Side-by-side comparison of approaches
    
    This class demonstrates the difference between basic parametrization and pytest.param with IDs
    """
    
    def test_without_ids_example(self):
        """
        EXAMPLE WITHOUT pytest.param IDs:
        This is how the original tests looked - harder to read and debug
        """
        # This would be parametrized like this in the original:
        # @pytest.mark.parametrize("ratio,expected,description", [
        #     (0.5, "50.0%", "half ratio"),
        #     (0.25, "25.0%", "quarter ratio"),
        #     (-0.1, "-10.0%", "negative ten percent"),
        # ])
        
        # Test output would be:
        # test_example[0.5-50.0%-half ratio] PASSED
        # test_example[0.25-25.0%-quarter ratio] PASSED  
        # test_example[-0.1--10.0%-negative ten percent] PASSED
        
        assert to_percent(0.5) == "50.0%"
        assert to_percent(0.25) == "25.0%"
        assert to_percent(-0.1) == "-10.0%"
    
    @pytest.mark.parametrize("ratio,expected,description", [
        pytest.param(0.5, "50.0%", "half ratio", id="clean_half"),
        pytest.param(0.25, "25.0%", "quarter ratio", id="clean_quarter"),
        pytest.param(-0.1, "-10.0%", "negative ten percent", id="clean_negative"),
    ])
    def test_with_ids_example(self, ratio, expected, description):
        """
        EXAMPLE WITH pytest.param IDs:
        Much cleaner test output and easier selective running
        
        Test output becomes:
        test_with_ids_example[clean_half] PASSED
        test_with_ids_example[clean_quarter] PASSED
        test_with_ids_example[clean_negative] PASSED
        
        Selective running:
        pytest -k "clean_half"     # Run just the half test
        pytest -k "clean_negative" # Run just the negative test
        """
        result = to_percent(ratio)
        assert result == expected, f"Failed for {description}: {ratio} -> {result}"

if __name__ == "__main__":
    """
    EDUCATIONAL EXAMPLES: Different ways to run these tests
    
    # Run all tests
    pytest test_to_percent_with_ids.py -v
    
    # Run tests by category
    pytest -k "business" test_to_percent_with_ids.py -v
    pytest -k "academic" test_to_percent_with_ids.py -v
    pytest -k "rounding" test_to_percent_with_ids.py -v
    pytest -k "boundary" test_to_percent_with_ids.py -v
    
    # Run specific test types
    pytest -k "critical" test_to_percent_with_ids.py -v
    pytest -k "edge" test_to_percent_with_ids.py -v
    pytest -k "format" test_to_percent_with_ids.py -v
    
    # Run combinations
    pytest -k "business and tax" test_to_percent_with_ids.py -v
    pytest -k "academic and pass" test_to_percent_with_ids.py -v
    pytest -k "tech and huge" test_to_percent_with_ids.py -v
    
    # Exclude certain tests
    pytest -k "not regression" test_to_percent_with_ids.py -v
    pytest -k "not tech" test_to_percent_with_ids.py -v
    """
    pytest.main([__file__, "-v"])


'''
    Benefits:
✅ Cleaner Output : Much easier to read test results
✅ Selective Running : pytest -k "business" or pytest -k "rounding"
✅ Logical Grouping : Related tests have similar ID patterns
✅ Faster Debugging : Failed tests are immediately identifiable
✅ Better CI/CD : Cleaner reports in automated systems
✅ Documentation : IDs serve as mini-documentation

Advanced Patterns Demonstrated:
Domain-specific IDs : business_profit, academic_passing, tech_precision
Hierarchical IDs : biz_tax_5pct, acad_excel_95pct
Behavior-specific IDs : round_up_12_4, boundary_zero, edge_tiny
Selective testing : Complex queries like pytest -k "business and tax"
This refactored version shows students the dramatic improvement in test maintainability and usability that comes from thoughtful ID design with pytest.param.'''