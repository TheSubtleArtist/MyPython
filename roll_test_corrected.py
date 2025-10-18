import pytest
from roll import roll_dice

def test_roll_dice_correct_patch(monkeypatch):
    # Return 2 first, then 4
    monkeypatch.setattr("roll.randint", lambda a, b: 3)
    result = roll_dice(6, 6)  # Roll 2 6-sided die
    assert result == 6, "roll 3 plus roll 3 is 6"