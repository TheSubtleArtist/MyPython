from rock import rock

def test_rock():
    # assert rock as winner
    assert rock("rock", "scissors") == ("rock", "crushes", "scissors"), "Player 1 as winner test failed"
    assert rock("scissors", "rock") == ("rock", "crushes", "scissors"), "Player 2 as winner test failed"
    assert rock("rock","rock") == None, "Tie assertion failed"
    assert rock("invalid", "rock") == ValueError, "Player 1 invalid input test failed"
    assert rock("rock", "invalid") == ValueError, "Player 2 invalid input test failed"

