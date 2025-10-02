from to_percent import to_percent

def test_to_percent():
    assert to_percent(0.25) == "25.0%"
    assert to_percent(1.0) =="100.0%"
    assert to_percent(0.7248) == "72.5%"

if __name__ == "__main__":
    test_to_percent()
