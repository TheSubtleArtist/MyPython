import pytest
import sys

def altprint(text):
    """Print text in aLtErNaTiNg CaPiTaLiZaTiOn."""
    result = ""
    capitalize_next = False
    for char in text:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
            else:
                result += char.lower()
            capitalize_next = not capitalize_next
        else:
            result += char
    sys.stdout.write(result + "\n")

class TestAltprintBasic:
    """Basic functionality tests for the altprint function."""
    
    def test_altprint_simple_word(self, capsys):
        """Test altprint with a simple word."""
        altprint("hello")
        captured = capsys.readouterr()
        assert captured.out == "hElLo\n"
        assert captured.err == ""
    
    def test_altprint_single_character(self, capsys):
        """Test altprint with a single character."""
        altprint("a")
        captured = capsys.readouterr()
        assert captured.out == "a\n"
        assert captured.err == ""
    
    def test_altprint_two_characters(self, capsys):
        """Test altprint with two characters."""
        altprint("ab")
        captured = capsys.readouterr()
        assert captured.out == "aB\n"
        assert captured.err == ""
    
    def test_altprint_empty_string(self, capsys):
        """Test altprint with empty string."""
        altprint("")
        captured = capsys.readouterr()
        assert captured.out == "\n"
        assert captured.err == ""
    
    def test_altprint_multiple_words(self, capsys):
        """Test altprint with multiple words separated by spaces."""
        altprint("hello world")
        captured = capsys.readouterr()
        assert captured.out == "hElLo WoRlD\n"
        assert captured.err == ""

class TestAltprintSpecialCharacters:
    """Tests for altprint function with special characters."""
    
    def test_altprint_with_numbers(self, capsys):
        """Test altprint with numbers (should not affect alternating pattern)."""
        altprint("hello123world")
        captured = capsys.readouterr()
        assert captured.out == "hElLo123WoRlD\n"
        assert captured.err == ""
    
    def test_altprint_with_punctuation(self, capsys):
        """Test altprint with punctuation marks."""
        altprint("hello, world!")
        captured = capsys.readouterr()
        assert captured.out == "hElLo, WoRlD!\n"
        assert captured.err == ""
    
    def test_altprint_with_spaces(self, capsys):
        """Test altprint with multiple spaces."""
        altprint("a   b")
        captured = capsys.readouterr()
        assert captured.out == "a   B\n"
        assert captured.err == ""
    
    def test_altprint_with_mixed_characters(self, capsys):
        """Test altprint with mixed alphabetic and non-alphabetic characters."""
        altprint("a1b2c3d")
        captured = capsys.readouterr()
        assert captured.out == "a1B2c3D\n"
        assert captured.err == ""
    
    def test_altprint_with_symbols(self, capsys):
        """Test altprint with various symbols."""
        altprint("test@email.com")
        captured = capsys.readouterr()
        assert captured.out == "tEsT@eMaIl.CoM\n"
        assert captured.err == ""

class TestAltprintEdgeCases:
    """Edge case tests for the altprint function."""
    
    def test_altprint_only_numbers(self, capsys):
        """Test altprint with only numbers."""
        altprint("12345")
        captured = capsys.readouterr()
        assert captured.out == "12345\n"
        assert captured.err == ""
    
    def test_altprint_only_symbols(self, capsys):
        """Test altprint with only symbols."""
        altprint("!@#$%")
        captured = capsys.readouterr()
        assert captured.out == "!@#$%\n"
        assert captured.err == ""
    
    def test_altprint_only_spaces(self, capsys):
        """Test altprint with only spaces."""
        altprint("     ")
        captured = capsys.readouterr()
        assert captured.out == "     \n"
        assert captured.err == ""
    
    def test_altprint_newline_in_text(self, capsys):
        """Test altprint with newline character in input."""
        altprint("hello\nworld")
        captured = capsys.readouterr()
        assert captured.out == "hElLo\nWoRlD\n"
        assert captured.err == ""
    
    def test_altprint_tab_in_text(self, capsys):
        """Test altprint with tab character in input."""
        altprint("hello\tworld")
        captured = capsys.readouterr()
        assert captured.out == "hElLo\tWoRlD\n"
        assert captured.err == ""

class TestAltprintParameterized:
    """Parameterized tests for the altprint function."""
    
    @pytest.mark.parametrize("input_text,expected_output", [
        ("a", "a\n"),
        ("ab", "aB\n"),
        ("abc", "aBc\n"),
        ("abcd", "aBcD\n"),
        ("hello", "hElLo\n"),
        ("HELLO", "hElLo\n"),
        ("HeLLo", "hElLo\n"),
        ("test", "tEsT\n"),
        ("python", "pYtHoN\n"),
        ("programming", "pRoGrAmMiNg\n"),
    ])
    def test_altprint_various_words(self, capsys, input_text, expected_output):
        """Test altprint with various word inputs."""
        altprint(input_text)
        captured = capsys.readouterr()
        assert captured.out == expected_output
        assert captured.err == ""
    
    @pytest.mark.parametrize("input_text,expected_output", [
        ("a1b", "a1B\n"),
        ("a b", "a B\n"),
        ("a!b", "a!B\n"),
        ("a@b", "a@B\n"),
        ("a.b.c", "a.B.c\n"),
        ("a-b-c-d", "a-B-c-D\n"),
        ("a_b_c_d_e", "a_B_c_D_e\n"),
    ])
    def test_altprint_with_separators(self, capsys, input_text, expected_output):
        """Test altprint with various non-alphabetic separators."""
        altprint(input_text)
        captured = capsys.readouterr()
        assert captured.out == expected_output
        assert captured.err == ""
    
    @pytest.mark.parametrize("input_text,expected_output", [
        ("", "\n"),
        ("123", "123\n"),
        ("!@#", "!@#\n"),
        ("   ", "   \n"),
        ("\t\t", "\t\t\n"),
        ("\n", "\n\n"),
    ])
    def test_altprint_non_alphabetic_only(self, capsys, input_text, expected_output):
        """Test altprint with inputs containing no alphabetic characters."""
        altprint(input_text)
        captured = capsys.readouterr()
        assert captured.out == expected_output
        assert captured.err == ""

class TestAltprintUnicode:
    """Unicode and international character tests."""
    
    def test_altprint_with_accented_characters(self, capsys):
        """Test altprint with accented characters."""
        altprint("café")
        captured = capsys.readouterr()
        assert captured.out == "cAfÉ\n"
        assert captured.err == ""
    
    def test_altprint_with_german_characters(self, capsys):
        """Test altprint with German characters."""
        altprint("hülle")
        captured = capsys.readouterr()
        assert captured.out == "hÜlLe\n"
        assert captured.err == ""
    
    def test_altprint_with_mixed_unicode(self, capsys):
        """Test altprint with mixed ASCII and Unicode characters."""
        altprint("café au lait")
        captured = capsys.readouterr()
        assert captured.out == "cAfÉ Au LaIt\n"
        assert captured.err == ""

class TestAltprintLongInputs:
    """Tests with long inputs."""
    
    def test_altprint_long_string(self, capsys):
        """Test altprint with a long string."""
        long_input = "a" * 100
        altprint(long_input)
        captured = capsys.readouterr()
        
        # Build expected output: a, A, a, A, ...
        expected = ""
        for i in range(100):
            if i % 2 == 0:
                expected += "a"
            else:
                expected += "A"
        expected += "\n"
        
        assert captured.out == expected
        assert captured.err == ""
    
    def test_altprint_alphabet(self, capsys):
        """Test altprint with the full alphabet."""
        altprint("abcdefghijklmnopqrstuvwxyz")
        captured = capsys.readouterr()
        assert captured.out == "aBcDeFgHiJkLmNoPqRsTuVwXyZ\n"
        assert captured.err == ""

class TestAltprintInputTypes:
    """Tests with different input types (should convert to string)."""
    
    def test_altprint_with_integer(self, capsys):
        """Test altprint with integer input."""
        altprint(123)
        captured = capsys.readouterr()
        assert captured.out == "123\n"
        assert captured.err == ""
    
    def test_altprint_with_float(self, capsys):
        """Test altprint with float input."""
        altprint(3.14)
        captured = capsys.readouterr()
        assert captured.out == "3.14\n"
        assert captured.err == ""
    
    def test_altprint_with_boolean(self, capsys):
        """Test altprint with boolean input."""
        altprint(True)
        captured = capsys.readouterr()
        assert captured.out == "tRuE\n"
        assert captured.err == ""

class TestAltprintAlternatingPattern:
    """Specific tests to verify the alternating pattern logic."""
    
    def test_alternating_pattern_starts_lowercase(self, capsys):
        """Test that alternating pattern always starts with lowercase."""
        test_cases = [
            "ABCD",
            "abcd", 
            "AbCd",
            "aBcD"
        ]
        
        for case in test_cases:
            capsys.readouterr()  # Clear previous output
            altprint(case)
            captured = capsys.readouterr()
            assert captured.out == "aBcD\n"
    
    def test_alternating_pattern_ignores_non_alpha(self, capsys):
        """Test that non-alphabetic characters don't affect the pattern."""
        altprint("a1B2c3D4e")
        captured = capsys.readouterr()
        # Pattern should be: a(lower), B(upper), c(lower), D(upper), e(lower)
        assert captured.out == "a1b2C3d4E\n"
        assert captured.err == ""
    
    def test_alternating_pattern_multiple_separators(self, capsys):
        """Test alternating pattern with multiple consecutive separators."""
        altprint("a!!!B###c")
        captured = capsys.readouterr()
        # Pattern: a(lower), B(upper), c(lower)
        assert captured.out == "a!!!b###C\n"
        assert captured.err == ""

# Fixtures for reusable test data
@pytest.fixture
def sample_words():
    """Fixture providing sample words for testing."""
    return ["hello", "world", "python", "testing", "code"]

@pytest.fixture
def special_strings():
    """Fixture providing strings with special characters."""
    return [
        "hello, world!",
        "test@email.com", 
        "file.txt",
        "user-name",
        "data_file.csv"
    ]

class TestAltprintWithFixtures:
    """Tests using custom fixtures."""
    
    def test_altprint_with_sample_words(self, capsys, sample_words):
        """Test altprint with fixture-provided sample words."""
        expected_outputs = {
            "hello": "hElLo\n",
            "world": "wOrLd\n", 
            "python": "pYtHoN\n",
            "testing": "tEsTiNg\n",
            "code": "cOdE\n"
        }
        
        for word in sample_words:
            capsys.readouterr()  # Clear previous output
            altprint(word)
            captured = capsys.readouterr()
            assert captured.out == expected_outputs[word]
            assert captured.err == ""

# Performance and stress tests
class TestAltprintPerformance:
    """Performance-related tests."""
    
    @pytest.mark.slow
    def test_altprint_very_long_string(self, capsys):
        """Test altprint with very long string."""
        # Create a string with 10,000 characters
        long_string = "abc" * 3334  # 10,002 characters
        altprint(long_string)
        captured = capsys.readouterr()
        
        # Verify it starts and ends correctly
        assert captured.out.startswith("aBc")
        assert captured.out.endswith("c\n")
        assert len(captured.out) == len(long_string) + 1  # +1 for newline

if __name__ == "__main__":
    pytest.main([__file__, "-v"])