from calculate_total import calculate_total


def test_varying_amounts():
    assert calculate_total([3.49]) == 3.84
    assert calculate_total([3.49, 13.89]) == 19.12 

def test_no_tax():
    assert calculate_total([3.49], apply_tax=False) == 3.49
    assert calculate_total([3.49, 13.89], apply_tax=False) == 17.38