import pytest
from percent_to_grade import percent_to_grade, round_half_up

class TestRoundHalfUp:
    """Test the round_half_up helper function."""
    
    def test_round_half_up_exactly_half(self):
        """Test rounding when number ends in exactly 0.5"""
        assert round_half_up(85.5) == 86
        assert round_half_up(92.5) == 93
        assert round_half_up(0.5) == 1
    
    def test_round_half_up_above_half(self):
        """Test rounding when decimal is above 0.5"""
        assert round_half_up(85.7) == 86
        assert round_half_up(92.9) == 93
    
    def test_round_half_up_below_half(self):
        """Test rounding when decimal is below 0.5"""
        assert round_half_up(85.4) == 85
        assert round_half_up(92.2) == 92
    
    def test_round_half_up_whole_numbers(self):
        """Test rounding whole numbers (should remain unchanged)"""
        assert round_half_up(85.0) == 85
        assert round_half_up(92.0) == 92

class TestPercentToGradeBasicFunctionality:
    """Test basic letter grade assignment without suffix or rounding."""
    
    def test_grade_a_range(self):
        """Test A grade assignments (90-100)"""
        assert percent_to_grade(90) == 'A'
        assert percent_to_grade(95) == 'A'
        assert percent_to_grade(100) == 'A'
    
    def test_grade_b_range(self):
        """Test B grade assignments (80-89)"""
        assert percent_to_grade(80) == 'B'
        assert percent_to_grade(85) == 'B'
        assert percent_to_grade(89) == 'B'
    
    def test_grade_c_range(self):
        """Test C grade assignments (70-79)"""
        assert percent_to_grade(70) == 'C'
        assert percent_to_grade(75) == 'C'
        assert percent_to_grade(79) == 'C'
    
    def test_grade_d_range(self):
        """Test D grade assignments (60-69)"""
        assert percent_to_grade(60) == 'D'
        assert percent_to_grade(65) == 'D'
        assert percent_to_grade(69) == 'D'
    
    def test_grade_f_range(self):
        """Test F grade assignments (below 60)"""
        assert percent_to_grade(59) == 'F'
        assert percent_to_grade(30) == 'F'
        assert percent_to_grade(0) == 'F'
    
    def test_boundary_values(self):
        """Test exact boundary values between grades"""
        assert percent_to_grade(89.9) == 'B'  # Just below A
        assert percent_to_grade(90.0) == 'A'  # Exactly A threshold
        assert percent_to_grade(79.9) == 'C'  # Just below B
        assert percent_to_grade(80.0) == 'B'  # Exactly B threshold

class TestPercentToGradeWithRounding:
    """Test grade assignment with rounding enabled."""
    
    def test_rounding_affects_grade_boundary(self):
        """Test cases where rounding changes the letter grade"""
        # 89.5 should round to 90 and become an A
        assert percent_to_grade(89.5, round=True) == 'A'
        # 79.5 should round to 80 and become a B
        assert percent_to_grade(79.5, round=True) == 'B'
        # 69.5 should round to 70 and become a C
        assert percent_to_grade(69.5, round=True) == 'C'
        # 59.5 should round to 60 and become a D
        assert percent_to_grade(59.5, round=True) == 'D'
    
    def test_rounding_no_grade_change(self):
        """Test cases where rounding doesn't change the letter grade"""
        assert percent_to_grade(89.4, round=True) == 'B'
        assert percent_to_grade(95.7, round=True) == 'A'

class TestPercentToGradeWithSuffix:
    """Test grade assignment with suffix enabled."""
    
    def test_plus_suffix_assignment(self):
        """Test + suffix assignment (x7, x8, x9)"""
        assert percent_to_grade(97, suffix=True) == 'A+'
        assert percent_to_grade(87, suffix=True) == 'B+'
        assert percent_to_grade(77, suffix=True) == 'C+'
        assert percent_to_grade(67, suffix=True) == 'D+'
        assert percent_to_grade(98, suffix=True) == 'A+'
        assert percent_to_grade(99, suffix=True) == 'A+'
    
    def test_minus_suffix_assignment(self):
        """Test - suffix assignment (x0, x1, x2)"""
        assert percent_to_grade(90, suffix=True) == 'A-'
        assert percent_to_grade(91, suffix=True) == 'A-'
        assert percent_to_grade(92, suffix=True) == 'A-'
        assert percent_to_grade(80, suffix=True) == 'B-'
        assert percent_to_grade(81, suffix=True) == 'B-'
        assert percent_to_grade(82, suffix=True) == 'B-'
    
    def test_no_suffix_assignment(self):
        """Test cases where no suffix is assigned (x3, x4, x5, x6)"""
        assert percent_to_grade(93, suffix=True) == 'A'
        assert percent_to_grade(94, suffix=True) == 'A'
        assert percent_to_grade(95, suffix=True) == 'A'
        assert percent_to_grade(96, suffix=True) == 'A'
        assert percent_to_grade(83, suffix=True) == 'B'
        assert percent_to_grade(84, suffix=True) == 'B'
    
    def test_special_a_plus_case(self):
        """Test the special A+ case for scores > 99
        
        This test reveals a potential bug: the condition is > 99, 
        meaning 100 gets A+ but scores like 99.5 don't.
        """
        # This should pass based on current logic but might be unexpected behavior
        assert percent_to_grade(100, suffix=True) == 'A+'  # > 99, so gets +
        assert percent_to_grade(99, suffix=True) == 'A+'   # 99 % 10 = 9, >= 7, so gets +
        
        # Edge case that might be unexpected
        assert percent_to_grade(99.5, suffix=True) == 'A+'  # 99.5 % 10 = 9.5, >= 7
    
    def test_f_grade_no_suffix(self):
        """Test that F grades never get suffixes"""
        assert percent_to_grade(50, suffix=True) == 'F'
        assert percent_to_grade(0, suffix=True) == 'F'

class TestPercentToGradeEdgeCases:
    """Test edge cases and potential error conditions."""
    
    def test_negative_percentages(self):
        """Test handling of negative percentages"""
        assert percent_to_grade(-10) == 'F'
        assert percent_to_grade(-5, suffix=True) == 'F'
    
    def test_percentages_over_100(self):
        """Test handling of percentages over 100"""
        assert percent_to_grade(105) == 'A'
        assert percent_to_grade(150, suffix=True) == 'A+'  # 150 > 99, so gets +
    
    def test_decimal_precision_edge_cases(self):
        """Test decimal precision edge cases that might cause issues"""
        # These test floating point precision issues
        assert percent_to_grade(89.999999) == 'B'
        assert percent_to_grade(90.000001) == 'A'
    
    def test_combined_round_and_suffix(self):
        """Test using both round=True and suffix=True together"""
        # 89.5 rounds to 90, which should be A-
        assert percent_to_grade(89.5, round=True, suffix=True) == 'A-'
        # 86.7 rounds to 87, which should be B+
        assert percent_to_grade(86.7, round=True, suffix=True) == 'B+'

class TestParameterValidation:
    """Test parameter validation and type handling."""
    
    def test_invalid_types(self):
        """Test function behavior with invalid input types
        
        These tests check if the function handles invalid inputs gracefully.
        The current code doesn't validate inputs, so these might raise exceptions.
        """
        with pytest.raises(TypeError):
            percent_to_grade("90")
        
        with pytest.raises(TypeError):
            percent_to_grade(None)
    
    def test_keyword_only_parameters(self):
        """Test that suffix and round are keyword-only parameters"""
        # This should work
        percent_to_grade(90, suffix=True, round=False)
        
        # This should raise TypeError due to keyword-only parameters
        with pytest.raises(TypeError):
            percent_to_grade(90, True, False)  # Positional arguments not allowed

class TestPotentialBugs:
    """Tests specifically designed to reveal bugs in the implementation."""
    
    def test_f_grade_suffix_logic_bug(self):
        """Test reveals that F grade handling is inconsistent
        
        The function returns 'F' directly for failing grades but the suffix
        logic has a condition for letter != 'F', which is never reached for F grades.
        """
        # This works correctly
        assert percent_to_grade(50, suffix=True) == 'F'
        
        # But the logic structure suggests potential confusion in the code
        # The F case returns early, bypassing all suffix logic
    
    def test_a_plus_logic_inconsistency(self):
        """Test reveals inconsistency in A+ assignment logic
        
        There are two ways to get A+:
        1. percent > 99 (special case)
        2. percent % 10 >= 7 (general rule)
        
        This creates redundancy and potential confusion.
        """
        # 100 gets A+ via the > 99 condition
        assert percent_to_grade(100, suffix=True) == 'A+'
        
        # 97 gets A+ via the % 10 >= 7 condition  
        assert percent_to_grade(97, suffix=True) == 'A+'
        
        # Both paths lead to A+, but the logic is redundant
    
    def test_round_parameter_name_conflict(self):
        """Test reveals that 'round' parameter shadows built-in round() function
        
        This is a naming issue that could cause confusion.
        """
        # The parameter name 'round' shadows the built-in round function
        # This works but is poor practice
        assert percent_to_grade(89.7, round=True) == 'A'