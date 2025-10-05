from vote_tally import get_vote_tally


def test_get_vote_tally():
    assert get_vote_tally("") == [], "Empty Input Assertion failed"
    assert get_vote_tally("42") == [(1,[42])], "Single Vote Assertion failed"
    assert get_vote_tally("hello world") == [], "Text with no numbers Assertion failed"


if __name__ == "__main__":
    test_get_vote_tally()
