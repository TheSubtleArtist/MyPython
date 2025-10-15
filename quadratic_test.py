import pytest
from quadratic import quadratic, QuadraticError

def test_quadratic_normal_case():
    """Test normal quadratic equation solving."""
    # x² - 5x + 6 = 0 should give x = 2 or x = 3
    result = quadratic(1, -5, 6)
    assert result == (3.0, 2.0)

def test_quadratic_zero_a():
    """Test that quadratic raises QuadraticError when a=0."""
    with pytest.raises(QuadraticError):
        quadratic(0, 2, 1)

def test_quadratic_negative_discriminant():
    """Test that quadratic raises QuadraticError for negative discriminant."""
    with pytest.raises(QuadraticError):
        quadratic(1, 0, 1)  # No real solutions

def test_quadratic_zero_a_message():
    """Test that quadratic raises correct message for a=0."""
    with pytest.raises(QuadraticError, match="Variable 'a' cannot be 0"):
        quadratic(0, 2, 1)

def test_quadratic_negative_discriminant_message():
    """Test exception message for negative discriminant."""
    with pytest.raises(QuadraticError, match="Cannot take square root of negative number"):
        quadratic(1, 0, 1)