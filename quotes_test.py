from quotes import get_all_quotes

def test_get_all_quotes(tmp_path):
    """Test reading quotes from CSV file."""
    quotes_file = tmp_path / "quotes.csv"
    csv_content = """Einstein,Imagination is more important than knowledge
Twain,The secret of getting ahead is getting started
Jobs,Innovation distinguishes between a leader and a follower"""

    quotes_file.write_text(csv_content)

    quotes = get_all_quotes(quotes_file)

    assert len(quotes) == 3
    assert quotes[0].author == "Einstein"
    assert quotes[0].text == "Imagination is more important than knowledge"
    assert quotes[1].author == "Twain"
    assert quotes[2].text == "Innovation distinguishes between a leader and a follower"
