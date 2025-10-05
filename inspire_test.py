from inspire import get_all_quotes


def test_quote_with_comma(tmp_path):
    """Test parsing a quote that contains commas - this will fail."""
    quotes_file = tmp_path / 'quotes.csv'
    quotes_file.write_text('Dr. Seuss,"One fish, two fish, red fish, blue fish"\n')

    # This test will fail with "ValueError: too many values to unpack"
    result = get_all_quotes(str(quotes_file))
    expected = [("Dr. Seuss", "One fish, two fish, red fish, blue fish")]
    assert result == expected