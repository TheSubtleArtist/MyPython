from dollars import format_dollars

def test_dollars():
    assert format_dollars(80) == "$80.00", "Assertion failed"
    assert format_dollars(3.048) == "$3.05", "Assertion failed"
    assert format_dollars(0.05) == "$0.05", "Assertion failed"

if __name__ == "__main__":
    test_dollars()


