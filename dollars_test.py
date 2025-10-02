from dollars import format_dollars

def test_dollars():
    assert format_dollars(80) == "$80.00"
    assert format_dollars(3.048) == "3.05"
    assert format_dollars(0.05) == "$0.05"

if __name__ == "__main__":
    test_dollars()