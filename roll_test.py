import pytest
from roll import roll_dice

def test_roll_dice(monkeypatch):
    # Return 2 first, then 4
    monkeypatch.setattr("random.randint", lambda a, b: 3)
    result = roll_dice(6, 6)  # Roll 2 6-sided die
    assert result == 6, "roll 3 plus roll 3 is 6"