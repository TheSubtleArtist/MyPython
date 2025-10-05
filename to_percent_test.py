from to_percent import to_percent

def test_to_percent():
    assert to_percent(0.25) == "25.0%", "Assertion failed"
    assert to_percent(1.0) == "100.0%", "Assertion failed"
    assert to_percent(0.7248) == "72.5%", "Assertion failed"

if __name__ == "__main__":
    test_to_percent()
