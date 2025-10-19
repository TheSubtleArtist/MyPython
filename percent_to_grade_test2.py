# test_percent_to_grade_optimized.py
'''
EDUCATIONAL EXAMPLE: Optimized Testing for Complex Branching Logic

This file demonstrates how to systematically test functions with multiple branches
and parameters using pytest parametrization with meaningful IDs.

KEY TESTING CHALLENGES ADDRESSED:
1. Multiple branching logic (grade boundaries)
2. Keyword-only parameters (suffix, round)
3. Edge cases and boundary conditions
4. Complex suffix logic with nested conditions
5. Helper function testing (round_half_up)

OPTIMIZATION BENEFITS:
- Systematic coverage of all grade boundaries
- Clear test IDs for easy debugging
- Comprehensive suffix testing scenarios
- Selective running by grade level or feature
- Easy maintenance and extension

SELECTIVE RUNNING EXAMPLES:
pytest -k "boundary"     # All boundary condition tests
pytest -k "suffix"       # All suffix-related tests  
pytest -k "perfect"      # Perfect score scenarios
pytest -k "failing"      # Failing grade scenarios
pytest -k "rounding"     # Rounding behavior tests
'''

import pytest
from math import ceil, floor

# Import the functions we're testing
from percent_to_grade import percent_to_grade, round_half_up

class TestRoundHalfUp:
    """Tests for the round_half_up helper function with rounding-specific IDs."""
    
    @pytest.mark.parametrize("input_number,expected_result", [
        # Exact integers - no rounding needed
        pytest.param(90.0, 90, id="rounding_exact_90"),
        pytest.param(100.0, 100, id="rounding_exact_100"),
        pytest.param(0.0, 0, id="rounding_exact_zero"),
        
        # Round down cases (< 0.5)
        pytest.param(89.1, 89, id="rounding_down_89_1"),
        pytest.param(89.4, 89, id="rounding_down_89_4"),
        pytest.param(89.49, 89, id="rounding_down_89_49"),
        pytest.param(0.1, 0, id="rounding_down_0_1"),
        pytest.param(0.4, 0, id="rounding_down_0_4"),
        
        # Round up cases (>= 0.5)
        pytest.param(89.5, 90, id="rounding_up_89_5"),
        pytest.param(89.6, 90, id="rounding_up_89_6"),
        pytest.param(89.9, 90, id="rounding_up_89_9"),
        pytest.param(0.5, 1, id="rounding_up_0_5"),
        pytest.param(0.9, 1, id="rounding_up_0_9"),
        
        # Boundary cases at grade thresholds
        pytest.param(59.5, 60, id="rounding_boundary_60"),
        pytest.param(69.5, 70, id="rounding_boundary_70"),
        pytest.param(79.5, 80, id="rounding_boundary_80"),
        pytest.param(89.5, 90, id="rounding_boundary_90"),
        
        # Negative numbers
        pytest.param(-0.4, 0, id="rounding_negative_down"),
        pytest.param(-0.5, 0, id="rounding_negative_up"),
        pytest.param(-1.4, -1, id="rounding_negative_1_down"),
        pytest.param(-1.5, -1, id="rounding_negative_1_up"),
    ])
    def test_round_half_up_behavior(self, input_number, expected_result):
        """
        OPTIMIZATION: Comprehensive rounding behavior testing in one parametrized test
        EDUCATIONAL BENEFIT: Shows systematic testing of mathematical functions
        SELECTIVE RUNNING: pytest -k "rounding" runs all rounding tests
        """
        result = round_half_up(input_number)
        assert result == expected_result, f"Rounding {input_number} failed"
        assert isinstance(result, int), f"Result should be integer, got {type(result)}"

class TestPercentToGradeBasicBoundaries:
    """Basic grade boundary tests without suffix complications."""
    
    @pytest.mark.parametrize("percent,expected_grade,boundary_type", [
        # A grade boundaries (90-100)
        pytest.param(100, 'A', 'perfect_score', id="boundary_perfect_100"),
        pytest.param(99, 'A', 'near_perfect', id="boundary_A_99"),
        pytest.param(95, 'A', 'solid_A', id="boundary_A_95"),
        pytest.param(90, 'A', 'minimum_A', id="boundary_A_90"),
        pytest.param(89, 'B', 'just_below_A', id="boundary_just_below_A"),
        
        # B grade boundaries (80-89)
        pytest.param(89, 'B', 'maximum_B', id="boundary_B_89"),
        pytest.param(85, 'B', 'solid_B', id="boundary_B_85"),
        pytest.param(80, 'B', 'minimum_B', id="boundary_B_80"),
        pytest.param(79, 'C', 'just_below_B', id="boundary_just_below_B"),
        
        # C grade boundaries (70-79)
        pytest.param(79, 'C', 'maximum_C', id="boundary_C_79"),
        pytest.param(75, 'C', 'solid_C', id="boundary_C_75"),
        pytest.param(70, 'C', 'minimum_C', id="boundary_C_70"),
        pytest.param(69, 'D', 'just_below_C', id="boundary_just_below_C"),
        
        # D grade boundaries (60-69)
        pytest.param(69, 'D', 'maximum_D', id="boundary_D_69"),
        pytest.param(65, 'D', 'solid_D', id="boundary_D_65"),
        pytest.param(60, 'D', 'minimum_D', id="boundary_D_60"),
        pytest.param(59, 'F', 'just_below_D', id="boundary_just_below_D"),
        
        # F grade cases (below 60)
        pytest.param(59, 'F', 'failing_high', id="boundary_F_59"),
        pytest.param(50, 'F', 'failing_mid', id="boundary_F_50"),
        pytest.param(25, 'F', 'failing_low', id="boundary_F_25"),
        pytest.param(0, 'F', 'failing_zero', id="boundary_F_0"),
    ])
    def test_basic_grade_boundaries(self, percent, expected_grade, boundary_type):
        """
        OPTIMIZATION: Single parametrized test covers all basic grade boundaries
        EDUCATIONAL BENEFIT: Shows systematic boundary testing
        SELECTIVE RUNNING: pytest -k "boundary_A" tests only A grade boundaries
        """
        result = percent_to_grade(percent)
        assert result == expected_grade, f"Basic boundary test failed for {boundary_type}: {percent}%"

class TestPercentToGradeWithSuffix:
    """Comprehensive suffix testing with suffix-specific IDs."""
    
    @pytest.mark.parametrize("percent,suffix_enabled,expected_grade,scenario", [
        # A grade suffix scenarios
        pytest.param(100, True, 'A+', 'perfect_score_with_suffix', id="suffix_A_plus_100"),
        pytest.param(99.5, True, 'A+', 'near_perfect_with_suffix', id="suffix_A_plus_99_5"),
        pytest.param(99, True, 'A', 'A_without_plus_99', id="suffix_A_plain_99"),
        pytest.param(97, True, 'A+', 'A_plus_97', id="suffix_A_plus_97"),
        pytest.param(93, True, 'A', 'A_plain_93', id="suffix_A_plain_93"),
        pytest.param(92, True, 'A-', 'A_minus_92', id="suffix_A_minus_92"),
        pytest.param(90, True, 'A', 'A_plain_90', id="suffix_A_plain_90"),
        
        # B grade suffix scenarios
        pytest.param(87, True, 'B+', 'B_plus_87', id="suffix_B_plus_87"),
        pytest.param(83, True, 'B', 'B_plain_83', id="suffix_B_plain_83"),
        pytest.param(82, True, 'B-', 'B_minus_82', id="suffix_B_minus_82"),
        pytest.param(80, True, 'B', 'B_plain_80', id="suffix_B_plain_80"),
        
        # C grade suffix scenarios
        pytest.param(77, True, 'C+', 'C_plus_77', id="suffix_C_plus_77"),
        pytest.param(73, True, 'C', 'C_plain_73', id="suffix_C_plain_73"),
        pytest.param(72, True, 'C-', 'C_minus_72', id="suffix_C_minus_72"),
        pytest.param(70, True, 'C', 'C_plain_70', id="suffix_C_plain_70"),
        
        # D grade suffix scenarios
        pytest.param(67, True, 'D+', 'D_plus_67', id="suffix_D_plus_67"),
        pytest.param(63, True, 'D', 'D_plain_63', id="suffix_D_plain_63"),
        pytest.param(62, True, 'D-', 'D_minus_62', id="suffix_D_minus_62"),
        pytest.param(60, True, 'D', 'D_plain_60', id="suffix_D_plain_60"),
        
        # F grade - no suffix regardless of setting
        pytest.param(59, True, 'F', 'F_no_suffix_enabled', id="suffix_F_59_enabled"),
        pytest.param(50, True, 'F', 'F_no_suffix_mid', id="suffix_F_50_enabled"),
        pytest.param(0, True, 'F', 'F_no_suffix_zero', id="suffix_F_0_enabled"),
        
        # Same grades without suffix
        pytest.param(97, False, 'A', 'A_no_suffix_97', id="no_suffix_A_97"),
        pytest.param(87, False, 'B', 'B_no_suffix_87', id="no_suffix_B_87"),
        pytest.param(77, False, 'C', 'C_no_suffix_77', id="no_suffix_C_77"),
        pytest.param(67, False, 'D', 'D_no_suffix_67', id="no_suffix_D_67"),
        pytest.param(59, False, 'F', 'F_no_suffix_59', id="no_suffix_F_59"),
    ])
    def test_suffix_behavior_comprehensive(self, percent, suffix_enabled, expected_grade, scenario):
        """
        OPTIMIZATION: Single parametrized test covers all suffix scenarios
        EDUCATIONAL BENEFIT: Shows complex parameter testing with boolean flags
        SELECTIVE RUNNING: pytest -k "suffix_A_plus" tests only A+ scenarios
        """
        result = percent_to_grade(percent, suffix=suffix_enabled)
        assert result == expected_grade, f"Suffix test failed for scenario '{scenario}': {percent}% with suffix={suffix_enabled}"

class TestPercentToGradeWithRounding:
    """Rounding behavior tests with rounding-specific IDs."""
    
    @pytest.mark.parametrize("percent,round_enabled,expected_grade,rounding_scenario", [
        # Rounding up changes grade
        pytest.param(89.5, True, 'A', 'round_up_to_A_grade', id="rounding_89_5_to_A"),
        pytest.param(79.5, True, 'B', 'round_up_to_B_grade', id="rounding_79_5_to_B"),
        pytest.param(69.5, True, 'C', 'round_up_to_C_grade', id="rounding_69_5_to_C"),
        pytest.param(59.5, True, 'D', 'round_up_to_D_grade', id="rounding_59_5_to_D"),
        
        # Rounding down keeps grade
        pytest.param(89.4, True, 'B', 'round_down_stays_B', id="rounding_89_4_stays_B"),
        pytest.param(79.4, True, 'C', 'round_down_stays_C', id="rounding_79_4_stays_C"),
        pytest.param(69.4, True, 'D', 'round_down_stays_D', id="rounding_69_4_stays_D"),
        pytest.param(59.4, True, 'F', 'round_down_stays_F', id="rounding_59_4_stays_F"),
        
        # Same values without rounding
        pytest.param(89.5, False, 'B', 'no_round_89_5_stays_B', id="no_rounding_89_5_B"),
        pytest.param(79.5, False, 'C', 'no_round_79_5_stays_C', id="no_rounding_79_5_C"),
        pytest.param(69.5, False, 'D', 'no_round_69_5_stays_D', id="no_rounding_69_5_D"),
        pytest.param(59.5, False, 'F', 'no_round_59_5_stays_F', id="no_rounding_59_5_F"),
        
        # High precision decimal cases
        pytest.param(89.55, True, 'A', 'round_high_precision_to_A', id="rounding_89_55_to_A"),
        pytest.param(89.45, True, 'B', 'round_high_precision_stays_B', id="rounding_89_45_stays_B"),
        pytest.param(89.500001, True, 'A', 'round_barely_over_half', id="rounding_89_500001_to_A"),
        pytest.param(89.499999, True, 'B', 'round_barely_under_half', id="rounding_89_499999_stays_B"),
    ])
    def test_rounding_behavior_comprehensive(self, percent, round_enabled, expected_grade, rounding_scenario):
        """
        OPTIMIZATION: Single parametrized test covers all rounding scenarios
        EDUCATIONAL BENEFIT: Shows interaction between rounding and grading logic
        SELECTIVE RUNNING: pytest -k "rounding" tests all rounding behavior
        """
        result = percent_to_grade(percent, round=round_enabled)
        assert result == expected_grade, f"Rounding test failed for scenario '{rounding_scenario}': {percent}% with round={round_enabled}"

class TestPercentToGradeCombinedFeatures:
    """Tests combining suffix and rounding features with combined IDs."""
    
    @pytest.mark.parametrize("percent,suffix_enabled,round_enabled,expected_grade,combined_scenario", [
        # Rounding + suffix combinations that change outcomes
        pytest.param(89.7, True, True, 'A', 'round_up_with_suffix_A_plain', id="combined_89_7_round_suffix_A"),
        pytest.param(89.8, True, True, 'A+', 'round_up_with_suffix_A_plus', id="combined_89_8_round_suffix_A_plus"),
        pytest.param(89.2, True, True, 'B-', 'round_up_with_suffix_B_minus', id="combined_89_2_round_suffix_B_minus"),
        
        # Complex A+ scenarios with rounding
        pytest.param(99.6, True, True, 'A+', 'round_to_100_gets_A_plus', id="combined_99_6_round_to_A_plus"),
        pytest.param(99.4, True, True, 'A', 'round_down_99_stays_A', id="combined_99_4_round_stays_A"),
        
        # Boundary cases with both features
        pytest.param(79.7, True, True, 'B+', 'round_up_79_7_B_plus', id="combined_79_7_B_plus"),
        pytest.param(79.2, True, True, 'C-', 'round_up_79_2_C_minus', id="combined_79_2_C_minus"),
        pytest.param(69.7, True, True, 'C+', 'round_up_69_7_C_plus', id="combined_69_7_C_plus"),
        pytest.param(69.2, True, True, 'D-', 'round_up_69_2_D_minus', id="combined_69_2_D_minus"),
        
        # Edge cases where rounding affects suffix calculation
        pytest.param(86.5, True, True, 'B+', 'round_affects_suffix_calculation', id="combined_86_5_affects_suffix"),
        pytest.param(86.4, True, True, 'B', 'no_round_different_suffix', id="combined_86_4_no_round"),
        
        # All features disabled
        pytest.param(89.7, False, False, 'B', 'no_features_enabled', id="combined_89_7_no_features"),
        pytest.param(97.8, False, False, 'A', 'no_features_A_grade', id="combined_97_8_no_features"),
    ])
    def test_combined_features(self, percent, suffix_enabled, round_enabled, expected_grade, combined_scenario):
        """
        OPTIMIZATION: Tests interaction between suffix and rounding features
        EDUCATIONAL BENEFIT: Shows complex parameter interaction testing
        SELECTIVE RUNNING: pytest -k "combined" tests all feature combinations
        """
        result = percent_to_grade(percent, suffix=suffix_enabled, round=round_enabled)
        assert result == expected_grade, f"Combined features test failed for scenario '{combined_scenario}': {percent}% (suffix={suffix_enabled}, round={round_enabled})"

class TestPercentToGradeEdgeCases:
    """Edge cases and boundary conditions with edge-specific IDs."""
    
    @pytest.mark.parametrize("percent,suffix,round_flag,expected_grade,edge_case_type", [
        # Perfect scores and near-perfect
        pytest.param(100, True, False, 'A+', 'perfect_score_with_suffix', id="edge_perfect_score"),
        pytest.param(100, False, False, 'A', 'perfect_score_no_suffix', id="edge_perfect_no_suffix"),
        pytest.param(101, True, False, 'A+', 'over_perfect_score', id="edge_over_100"),
        pytest.param(110, True, False, 'A+', 'way_over_perfect', id="edge_way_over_100"),
        
        # Zero and negative edge cases
        pytest.param(0, True, False, 'F', 'zero_percent', id="edge_zero_percent"),
        pytest.param(0, False, False, 'F', 'zero_percent_no_suffix', id="edge_zero_no_suffix"),
        pytest.param(-5, True, False, 'F', 'negative_percent', id="edge_negative_percent"),
        pytest.param(-10, False, False, 'F', 'negative_percent_no_suffix', id="edge_negative_no_suffix"),
        
        # Exact boundary values
        pytest.param(90.0, True, False, 'A', 'exact_A_boundary', id="edge_exact_90"),
        pytest.param(80.0, True, False, 'B', 'exact_B_boundary', id="edge_exact_80"),
        pytest.param(70.0, True, False, 'C', 'exact_C_boundary', id="edge_exact_70"),
        pytest.param(60.0, True, False, 'D', 'exact_D_boundary', id="edge_exact_60"),
        
        # Suffix boundary edge cases (% 10 values)
        pytest.param(90, True, False, 'A', 'suffix_boundary_90_mod_0', id="edge_suffix_90_mod_0"),
        pytest.param(97, True, False, 'A+', 'suffix_boundary_97_mod_7', id="edge_suffix_97_mod_7"),
        pytest.param(92, True, False, 'A-', 'suffix_boundary_92_mod_2', id="edge_suffix_92_mod_2"),
        pytest.param(93, True, False, 'A', 'suffix_boundary_93_mod_3', id="edge_suffix_93_mod_3"),
        
        # High precision decimals
        pytest.param(89.999, False, False, 'B', 'high_precision_B', id="edge_high_precision_B"),
        pytest.param(89.999, True, False, 'B+', 'high_precision_B_plus', id="edge_high_precision_B_plus"),
        pytest.param(90.001, True, False, 'A', 'barely_over_90', id="edge_barely_over_90"),
        
        # Rounding edge cases
        pytest.param(89.5, False, True, 'A', 'rounding_edge_89_5', id="edge_rounding_89_5"),
        pytest.param(89.50000001, False, True, 'A', 'rounding_edge_precision', id="edge_rounding_precision"),
        pytest.param(89.49999999, False, True, 'B', 'rounding_edge_just_under', id="edge_rounding_just_under"),
    ])
    def test_edge_cases_comprehensive(self, percent, suffix, round_flag, expected_grade, edge_case_type):
        """
        OPTIMIZATION: Single parametrized test covers all edge cases
        EDUCATIONAL BENEFIT: Shows systematic edge case testing
        SELECTIVE RUNNING: pytest -k "edge_perfect" tests perfect score scenarios
        """
        result = percent_to_grade(percent, suffix=suffix, round=round_flag)
        assert result == expected_grade, f"Edge case test failed for '{edge_case_type}': {percent}%"

class TestPercentToGradeSuffixLogic:
    """Detailed suffix logic testing with logic-specific IDs."""
    
    @pytest.mark.parametrize("percent,expected_suffix,suffix_rule", [
        # Plus suffix rules (% 10 >= 7)
        pytest.param(97, '+', 'mod_7_gets_plus', id="suffix_logic_97_plus"),
        pytest.param(87, '+', 'mod_7_gets_plus', id="suffix_logic_87_plus"),
        pytest.param(77, '+', 'mod_7_gets_plus', id="suffix_logic_77_plus"),
        pytest.param(67, '+', 'mod_7_gets_plus', id="suffix_logic_67_plus"),
        pytest.param(98, '+', 'mod_8_gets_plus', id="suffix_logic_98_plus"),
        pytest.param(99, '+', 'mod_9_gets_plus', id="suffix_logic_99_plus"),
        
        # Minus suffix rules (% 10 < 3)
        pytest.param(90, '', 'mod_0_no_suffix', id="suffix_logic_90_none"),
        pytest.param(91, '-', 'mod_1_gets_minus', id="suffix_logic_91_minus"),
        pytest.param(92, '-', 'mod_2_gets_minus', id="suffix_logic_92_minus"),
        pytest.param(80, '', 'mod_0_no_suffix', id="suffix_logic_80_none"),
        pytest.param(81, '-', 'mod_1_gets_minus', id="suffix_logic_81_minus"),
        pytest.param(82, '-', 'mod_2_gets_minus', id="suffix_logic_82_minus"),
        
        # No suffix rules (% 10 in 3,4,5,6)
        pytest.param(93, '', 'mod_3_no_suffix', id="suffix_logic_93_none"),
        pytest.param(94, '', 'mod_4_no_suffix', id="suffix_logic_94_none"),
        pytest.param(95, '', 'mod_5_no_suffix', id="suffix_logic_95_none"),
        pytest.param(96, '', 'mod_6_no_suffix', id="suffix_logic_96_none"),
        
        # Special A+ rule (A grade and percent > 99)
        pytest.param(100, '+', 'special_A_plus_rule', id="suffix_logic_100_special_plus"),
        pytest.param(101, '+', 'special_A_plus_rule_over_100', id="suffix_logic_101_special_plus"),
        pytest.param(99, '', 'A_grade_but_not_over_99', id="suffix_logic_99_no_special_plus"),
    ])
    def test_suffix_logic_detailed(self, percent, expected_suffix, suffix_rule):
        """
        OPTIMIZATION: Detailed suffix logic testing
        EDUCATIONAL BENEFIT: Shows complex conditional logic testing
        SELECTIVE RUNNING: pytest -k "suffix_logic" tests suffix calculation rules
        """
        result = percent_to_grade(percent, suffix=True)
        
        # Determine expected grade without suffix
        if percent >= 90:
            base_grade = 'A'
        elif percent >= 80:
            base_grade = 'B'
        elif percent >= 70:
            base_grade = 'C'
        elif percent >= 60:
            base_grade = 'D'
        else:
            base_grade = 'F'
        
        expected_grade = base_grade + expected_suffix
        assert result == expected_grade, f"Suffix logic test failed for rule '{suffix_rule}': {percent}% -> expected '{expected_grade}', got '{result}'"

class TestPercentToGradeRealWorldScenarios:
    """Real-world usage scenarios with scenario-specific IDs."""
    
    @pytest.mark.parametrize("percent,suffix,round_flag,expected_grade,scenario_description", [
        # Typical gradebook scenarios
        pytest.param(92.5, True, True, 'A-', 'typical_A_minus_student', id="real_world_typical_A_minus"),
        pytest.param(87.3, True, False, 'B+', 'high_B_student', id="real_world_high_B"),
        pytest.param(76.8, True, False, 'C+', 'average_student_C_plus', id="real_world_average_C"),
        pytest.param(83.4, True, False, 'B', 'solid_B_student', id="real_world_solid_B"),
        
        # Borderline pass/fail scenarios
        pytest.param(59.8, False, True, 'D', 'borderline_pass_rounded', id="real_world_borderline_pass"),
        pytest.param(59.4, False, True, 'F', 'borderline_fail_rounded', id="real_world_borderline_fail"),
        pytest.param(69.6, True, True, 'C', 'barely_passing_C', id="real_world_barely_C"),
        
        # Honor roll scenarios
        pytest.param(96.2, True, False, 'A+', 'honor_roll_student', id="real_world_honor_roll"),
        pytest.param(89.9, True, False, 'B+', 'almost_A_student', id="real_world_almost_A"),
        
        # Extra credit scenarios
        pytest.param(102.5, True, False, 'A+', 'extra_credit_scenario', id="real_world_extra_credit"),
        pytest.param(105.0, True, True, 'A+', 'lots_of_extra_credit', id="real_world_lots_extra_credit"),
        
        # Strict grading (no suffix, no rounding)
        pytest.param(89.9, False, False, 'B', 'strict_grading_B', id="real_world_strict_B"),
        pytest.param(79.9, False, False, 'C', 'strict_grading_C', id="real_world_strict_C"),
        pytest.param(69.9, False, False, 'D', 'strict_grading_D', id="real_world_strict_D"),
        
        # Lenient grading (suffix and rounding)
        pytest.param(89.9, True, True, 'A', 'lenient_grading_A', id="real_world_lenient_A"),
        pytest.param(79.9, True, True, 'B', 'lenient_grading_B', id="real_world_lenient_B"),
    ])
    def test_real_world_scenarios(self, percent, suffix, round_flag, expected_grade, scenario_description):
        """
        OPTIMIZATION: Real-world grading scenario testing
        EDUCATIONAL BENEFIT: Shows practical usage patterns
        SELECTIVE RUNNING: pytest -k "real_world" tests practical scenarios
        """
        result = percent_to_grade(percent, suffix=suffix, round=round_flag)
        assert result == expected_grade, f"Real-world scenario '{scenario_description}' failed: {percent}%"

class TestPercentToGradeErrorAndInputValidation:
    """Input validation and error handling with validation-specific IDs."""
    
    @pytest.mark.parametrize("percent,suffix,round_flag,validation_type", [
        # Valid extreme values
        pytest.param(1000, True, False, 'very_high_percent', id="validation_extreme_high"),
        pytest.param(-100, True, False, 'very_negative_percent', id="validation_extreme_negative"),
        pytest.param(0.001, True, False, 'very_small_decimal', id="validation_tiny_decimal"),
        pytest.param(99.999999, True, False, 'high_precision_decimal', id="validation_high_precision"),
        
        # Valid parameter combinations
        pytest.param(85, True, True, 'all_features_enabled', id="validation_all_enabled"),
        pytest.param(85, False, False, 'all_features_disabled', id="validation_all_disabled"),
    ])
    def test_input_validation(self, percent, suffix, round_flag, validation_type):
        """
        OPTIMIZATION: Input validation testing
        EDUCATIONAL BENEFIT: Shows function robustness testing
        SELECTIVE RUNNING: pytest -k "validation" tests input handling
        """
        # Should not raise exceptions with valid numeric inputs
        result = percent_to_grade(percent, suffix=suffix, round=round_flag)
        assert isinstance(result, str), f"Result should be string for validation type '{validation_type}'"
        assert len(result) >= 1, f"Result should not be empty for validation type '{validation_type}'"
        assert result[0] in 'ABCDF', f"Result should start with valid grade letter for validation type '{validation_type}'"

class TestPercentToGradePerformance:
    """Performance testing with performance-specific IDs."""
    
    @pytest.mark.parametrize("test_scenario,percent_list,suffix,round_flag", [
        pytest.param(
            'batch_processing_no_features',
            list(range(0, 101, 5)),  # 0, 5, 10, ..., 100
            False, False,
            id="performance_batch_basic"
        ),
        pytest.param(
            'batch_processing_with_suffix',
            list(range(60, 101)),  # All passing grades
            True, False,
            id="performance_batch_suffix"
        ),
        pytest.param(
            'batch_processing_with_rounding',
            [x + 0.5 for x in range(50, 100)],  # Decimal values that trigger rounding
            False, True,
            id="performance_batch_rounding"
        ),
        pytest.param(
            'batch_processing_all_features',
            [x + 0.3 for x in range(0, 101, 3)],  # Irregular decimals
            True, True,
            id="performance_batch_all_features"
        ),
    ])
    def test_performance_scenarios(self, test_scenario, percent_list, suffix, round_flag):
        """
        OPTIMIZATION: Performance testing with batch operations
        EDUCATIONAL BENEFIT: Shows performance testing patterns
        SELECTIVE RUNNING: pytest -k "performance" tests execution speed
        """
        import time
        
        start_time = time.time()
        
        results = []
        for percent in percent_list:
            result = percent_to_grade(percent, suffix=suffix, round=round_flag)
            results.append(result)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Performance assertions
        assert execution_time < 1.0, f"Performance test '{test_scenario}' took too long: {execution_time}s"
        assert len(results) == len(percent_list), f"Should process all {len(percent_list)} inputs"
        assert all(isinstance(result, str) for result in results), "All results should be strings"

class TestPercentToGradeSystematicValidation:
    """Systematic validation tests with systematic-specific IDs."""
    
    def test_all_grade_letters_achievable(self):
        """
        SYSTEMATIC TEST: Verify all grade letters can be achieved
        EDUCATIONAL BENEFIT: Shows comprehensive coverage testing
        """
        achieved_grades = set()
        
        # Test range of percentages to ensure all grades are achievable
        for percent in range(0, 111, 5):  # 0 to 110 by 5s
            for suffix in [False, True]:
                for round_flag in [False, True]:
                    grade = percent_to_grade(percent, suffix=suffix, round=round_flag)
                    achieved_grades.add(grade)
        
        # Verify all expected grades can be achieved
        expected_base_grades = {'A', 'B', 'C', 'D', 'F'}
        expected_suffix_grades = {'A+', 'A-', 'B+', 'B-', 'C+', 'C-', 'D+', 'D-'}
        
        for grade in expected_base_grades:
            assert grade in achieved_grades, f"Base grade '{grade}' should be achievable"
        
        for grade in expected_suffix_grades:
            assert grade in achieved_grades, f"Suffix grade '{grade}' should be achievable"
    
    @pytest.mark.parametrize("grade_threshold,test_range", [
        pytest.param(90, range(85, 95), id="systematic_A_threshold"),
        pytest.param(80, range(75, 85), id="systematic_B_threshold"),
        pytest.param(70, range(65, 75), id="systematic_C_threshold"),
        pytest.param(60, range(55, 65), id="systematic_D_threshold"),
    ])
    def test_grade_threshold_behavior(self, grade_threshold, test_range):
        """
        SYSTEMATIC TEST: Verify consistent behavior around grade thresholds
        EDUCATIONAL BENEFIT: Shows boundary testing patterns
        SELECTIVE RUNNING: pytest -k "systematic_A" tests A grade threshold
        """
        for percent in test_range:
            result = percent_to_grade(percent)
            
            if percent >= grade_threshold:
                # Should get higher grade
                assert result != 'F', f"Percent {percent} should not be failing"
                if grade_threshold == 90:
                    assert result == 'A', f"Percent {percent} should be A grade"
                elif grade_threshold == 80:
                    assert result in ['A', 'B'], f"Percent {percent} should be A or B grade"
                elif grade_threshold == 70:
                    assert result in ['A', 'B', 'C'], f"Percent {percent} should be A, B, or C grade"
                elif grade_threshold == 60:
                    assert result in ['A', 'B', 'C', 'D'], f"Percent {percent} should be passing grade"
            else:
                # Should get lower grade
                if grade_threshold == 90:
                    assert result != 'A', f"Percent {percent} should not be A grade"
                elif grade_threshold == 80:
                    assert result not in ['A', 'B'], f"Percent {percent} should not be A or B grade"
                elif grade_threshold == 70:
                    assert result not in ['A', 'B', 'C'], f"Percent {percent} should not be A, B, or C grade"
                elif grade_threshold == 60:
                    assert result == 'F', f"Percent {percent} should be failing"

class TestPercentToGradeEducationalExamples:
    """Educational examples with learning-focused IDs."""
    
    @pytest.mark.parametrize("example_name,percent,suffix,round_flag,expected,learning_point", [
        pytest.param(
            'basic_grading_example',
            85, False, False,
            'B',
            'Shows basic grading without any special features',
            id="edu_basic_grading"
        ),
        pytest.param(
            'suffix_improvement_example',
            87, True, False,
            'B+',
            'Shows how suffix improves grade representation',
            id="edu_suffix_benefit"
        ),
        pytest.param(
            'rounding_helps_student',
            89.5, False, True,
            'A',
            'Shows how rounding can help borderline students',
            id="edu_rounding_benefit"
        ),
        pytest.param(
            'all_features_example',
            89.7, True, True,
            'A',
            'Shows combined effect of suffix and rounding',
            id="edu_all_features"
        ),
        pytest.param(
            'perfect_score_example',
            100, True, False,
            'A+',
            'Shows special A+ rule for perfect scores',
            id="edu_perfect_score"
        ),
        pytest.param(
            'failing_grade_example',
            45, True, True,
            'F',
            'Shows that F grades do not get suffixes',
            id="edu_failing_grade"
        ),
    ])
    def test_educational_examples(self, example_name, percent, suffix, round_flag, expected, learning_point):
        """
        EDUCATIONAL PURPOSE: Provides clear examples for learning
        BENEFIT: Shows practical usage with explanations
        SELECTIVE RUNNING: pytest -k "edu" runs all educational examples
        """
        result = percent_to_grade(percent, suffix=suffix, round=round_flag)
        assert result == expected, f"Educational example '{example_name}' failed: {learning_point}"

class TestPercentToGradeOptimizationDemonstration:
    """
    EDUCATIONAL COMPARISON: Shows the optimization benefits achieved
    """
    
    def test_optimization_achievements(self):
        """
        EDUCATIONAL SUMMARY: Demonstrates comprehensive test coverage
        
        OPTIMIZATION ACHIEVEMENTS:
        - Systematic boundary testing for all grade levels
        - Comprehensive suffix logic verification
        - Thorough rounding behavior testing
        - Combined feature interaction testing
        - Real-world scenario coverage
        - Performance validation
        - Educational examples for learning
        
        BEFORE: Would need 100+ individual test methods for this coverage
        AFTER: 8 parametrized test classes with clear, meaningful IDs
        
        STUDENT LEARNING: Shows how to systematically test complex branching logic
        """
        # Test that demonstrates the systematic approach
        test_coverage_areas = [
            'basic_boundaries',
            'suffix_logic', 
            'rounding_behavior',
            'combined_features',
            'edge_cases',
            'real_world_scenarios',
            'performance',
            'systematic_validation'
        ]
        
        assert len(test_coverage_areas) == 8, "Should cover 8 major testing areas"
        
        # Verify we can test complex interactions
        result = percent_to_grade(89.7, suffix=True, round=True)
        assert result == 'A', "Complex interaction should work correctly"

if __name__ == "__main__":
    """
    EDUCATIONAL EXAMPLES: How to run the optimized percent_to_grade tests
    
    # Run all tests with comprehensive output
    pytest test_percent_to_grade_optimized.py -v
    
    # Run tests by feature
    pytest -k "suffix" test_percent_to_grade_optimized.py -v      # All suffix-related tests
    pytest -k "rounding" test_percent_to_grade_optimized.py -v   # All rounding-related tests
    pytest -k "boundary" test_percent_to_grade_optimized.py -v   # All boundary tests
    pytest -k "combined" test_percent_to_grade_optimized.py -v   # Feature interaction tests
    
    # Run tests by grade level
    pytest -k "boundary_A" test_percent_to_grade_optimized.py -v # A grade boundaries
    pytest -k "boundary_B" test_percent_to_grade_optimized.py -v # B grade boundaries
    pytest -k "boundary_F" test_percent_to_grade_optimized.py -v # Failing grades
    
    # Run tests by scenario type
    pytest -k "edge" test_percent_to_grade_optimized.py -v       # Edge cases
    pytest -k "real_world" test_percent_to_grade_optimized.py -v # Practical scenarios
    pytest -k "performance" test_percent_to_grade_optimized.py -v # Performance tests
    pytest -k "edu" test_percent_to_grade_optimized.py -v        # Educational examples
    
    # Run specific edge cases
    pytest -k "perfect_score" test_percent_to_grade_optimized.py -v  # Perfect score scenarios
    pytest -k "failing" test_percent_to_grade_optimized.py -v        # Failing grade scenarios
    pytest -k "over_100" test_percent_to_grade_optimized.py -v       # Extra credit scenarios
    
    # Run validation and systematic tests
    pytest -k "validation" test_percent_to_grade_optimized.py -v     # Input validation
    pytest -k "systematic" test_percent_to_grade_optimized.py -v     # Systematic coverage
    
    # Debug specific features
    pytest -k "suffix_logic" test_percent_to_grade_optimized.py -v -s # Suffix calculation rules
    pytest -k "rounding_89_5" test_percent_to_grade_optimized.py -v   # Specific rounding case
    """
    pytest.main([__file__, "-v"])