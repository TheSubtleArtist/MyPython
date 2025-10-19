import pytest

from calculate_total import calculate_total

@pytest.mark.parametrize("apply_tax", [True, False])
@pytest.mark.parametrize("tax_rate", [0.05, 0.10, 0.15])
def test_calculate_total_cross_product(apply_tax, tax_rate):
    amounts = [10.00, 5.50]
    result = calculate_total(amounts, apply_tax=apply_tax, tax_rate=tax_rate)

    expected = 15.50 * (1 + tax_rate if apply_tax else 1)
    assert result == round(expected, 2)