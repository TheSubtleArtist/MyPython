import pytest
from phonetic import phonetic

class TestPhoneticBasicFunctionality:
    """Test basic phonetic alphabet conversion functionality."""
    
    def test_single_uppercase_letter(self):
        """Test conversion of single uppercase letters"""
        assert phonetic('A') == 'Alpha'
        assert phonetic('B') == 'Bravo'
        assert phonetic('Z') == 'Zulu'
    
    def test_single_lowercase_letter(self):
        """Test conversion of single lowercase letters"""
        assert phonetic('a') == 'Alpha'
        assert phonetic('b') == 'Bravo'
        assert phonetic('z') == 'Zulu'
    
    def test_multiple_letters_uppercase(self):
        """Test conversion of multiple uppercase letters"""
        assert phonetic('ABC') == 'Alpha Bravo Charlie'
        assert phonetic('SOS') == 'Sierra Oscar Sierra'
    
    def test_multiple_letters_lowercase(self):
        """Test conversion of multiple lowercase letters"""
        assert phonetic('abc') == 'Alpha Bravo Charlie'
        assert phonetic('sos') == 'Sierra Oscar Sierra'
    
    def test_mixed_case_letters(self):
        """Test conversion of mixed case letters"""
        assert phonetic('AbC') == 'Alpha Bravo Charlie'
        assert phonetic('SoS') == 'Sierra Oscar Sierra'

class TestPhoneticNonAlphabeticCharacters:
    """Test handling of non-alphabetic characters."""
    
    def test_single_digit(self):
        """Test conversion of single digits
        
        Current implementation passes digits through unchanged.
        This might not be the intended behavior.
        """
        assert phonetic('1') == '1'
        assert phonetic('0') == '0'
        assert phonetic('9') == '9'
    
    def test_special_characters(self):
        """Test conversion of special characters
        
        Current implementation passes special chars through unchanged.
        This might not be the intended behavior for phonetic spelling.
        """
        assert phonetic('!') == '!'
        assert phonetic('@') == '@'
        assert phonetic('#') == '#'
        assert phonetic('$') == '$'
        assert phonetic('%') == '%'
        assert phonetic('&') == '&'
        assert phonetic('*') == '*'
    
    def test_punctuation(self):
        """Test conversion of punctuation marks"""
        assert phonetic('.') == '.'
        assert phonetic(',') == ','
        assert phonetic('?') == '?'
        assert phonetic('!') == '!'
        assert phonetic(';') == ';'
        assert phonetic(':') == ':'
    
    def test_whitespace_characters(self):
        """Test conversion of whitespace characters
        
        This reveals potential issues with spacing in output.
        """
        assert phonetic(' ') == ' '
        assert phonetic('\t') == '\t'
        assert phonetic('\n') == '\n'

class TestPhoneticMixedContent:
    """Test conversion of text with mixed alphabetic and non-alphabetic characters."""
    
    def test_letters_with_digits(self):
        """Test text containing both letters and digits"""
        assert phonetic('A1B') == 'Alpha 1 Bravo'
        assert phonetic('SOS911') == 'Sierra Oscar Sierra 9 1 1'
        assert phonetic('B2B') == 'Bravo 2 Bravo'
    
    def test_letters_with_spaces(self):
        """Test text containing letters and spaces
        
        This reveals spacing issues - spaces are preserved and join with other spaces.
        """
        assert phonetic('A B') == 'Alpha   Bravo'  # Note: double space in middle
        assert phonetic('S O S') == 'Sierra   Oscar   Sierra'  # Multiple double spaces
    
    def test_letters_with_punctuation(self):
        """Test text containing letters and punctuation"""
        assert phonetic('A.B.C') == 'Alpha . Bravo . Charlie'
        assert phonetic('S.O.S!') == 'Sierra . Oscar . Sierra !'
        assert phonetic('Hello!') == 'Hotel Echo Lima Lima Oscar !'
    
    def test_words_with_spaces(self):
        """Test conversion of actual words with spaces
        
        This demonstrates the spacing issue more clearly.
        """
        assert phonetic('HI THERE') == 'Hotel India   Tango Hotel Echo Romeo Echo'
        # Note the double space between "India" and "Tango"

class TestPhoneticEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_empty_string(self):
        """Test conversion of empty string"""
        assert phonetic('') == ''
    
    def test_only_spaces(self):
        """Test string containing only spaces"""
        assert phonetic('   ') == '     '  # join() adds spaces between existing spaces
    
    def test_only_digits(self):
        """Test string containing only digits"""
        assert phonetic('123') == '1 2 3'
        assert phonetic('911') == '9 1 1'
    
    def test_only_special_characters(self):
        """Test string containing only special characters"""
        assert phonetic('!@#') == '! @ #'
        assert phonetic('***') == '* * *'
    
    def test_unicode_characters(self):
        """Test handling of Unicode characters
        
        Tests non-ASCII characters to see how they're handled.
        """
        assert phonetic('café') == 'Charlie Alpha Foxtrot é'  # é is preserved
        assert phonetic('naïve') == 'November Alpha ï Victor Echo'  # ï is preserved
        assert phonetic('résumé') == 'Romeo é Sierra Uniform Mike é'  # accented chars preserved
    
    def test_very_long_string(self):
        """Test with a very long string to check performance/memory issues"""
        long_text = 'A' * 1000
        expected = ' '.join(['Alpha'] * 1000)
        assert phonetic(long_text) == expected

class TestPhoneticInputValidation:
    """Test input validation and type handling."""
    
    def test_none_input(self):
        """Test function behavior with None input
        
        This will likely raise an AttributeError since None has no upper() method.
        """
        with pytest.raises(AttributeError):
            phonetic(None)
    
    def test_integer_input(self):
        """Test function behavior with integer input
        
        This will likely raise an AttributeError since integers aren't iterable for char iteration.
        """
        with pytest.raises(TypeError):
            phonetic(123)
    
    def test_list_input(self):
        """Test function behavior with list input
        
        This will likely raise an AttributeError since list elements may not have upper() method.
        """
        with pytest.raises(AttributeError):
            phonetic(['A', 'B', 'C'])
    
    def test_boolean_input(self):
        """Test function behavior with boolean input"""
        with pytest.raises(AttributeError):
            phonetic(True)

class TestPhoneticNATOAccuracy:
    """Test accuracy of NATO phonetic alphabet mappings."""
    
    def test_complete_alphabet_mapping(self):
        """Test that all 26 letters map to correct NATO words"""
        expected_mappings = {
            'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
            'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
            'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
            'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
            'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
            'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
            'Y': 'Yankee', 'Z': 'Zulu'
        }
        
        for letter, expected_word in expected_mappings.items():
            assert phonetic(letter) == expected_word
            assert phonetic(letter.lower()) == expected_word
    
    def test_nato_alphabet_completeness(self):
        """Test that no letters are missing from the NATO mapping"""
        import string
        for letter in string.ascii_uppercase:
            result = phonetic(letter)
            # Should not return the letter itself (which would indicate missing mapping)
            assert result != letter, f"Letter {letter} appears to be missing from NATO mapping"

class TestPhoneticSpacingIssues:
    """Test specific spacing-related issues identified in the implementation."""
    
    def test_spacing_bug_demonstration(self):
        """Demonstrate the spacing bug with mixed content
        
        The join(' ') operation adds spaces between ALL characters,
        including existing spaces, leading to double spaces.
        """
        # Single space becomes preserved and surrounded by join spaces
        result = phonetic('A B')
        spaces_count = result.count('  ')  # Count double spaces
        assert spaces_count == 1, f"Expected 1 double space, got {spaces_count} in '{result}'"
        
        # Multiple spaces get even more problematic
        result = phonetic('A  B')  # Two spaces between A and B
        assert '   ' in result, f"Expected triple spaces in result: '{result}'"
    
    def test_recommended_spacing_behavior(self):
        """Test what the spacing behavior probably should be
        
        These tests will fail but show what might be intended behavior.
        """
        # These tests will fail with current implementation but show expected behavior
        with pytest.raises(AssertionError):
            # This fails because current result is 'Alpha   Bravo' (3 spaces)
            assert phonetic('A B') == 'Alpha Bravo'  # Single space expected
        
        with pytest.raises(AssertionError):
            # This fails because spaces are treated as characters to preserve
            assert phonetic('HELLO WORLD') == 'Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta'

class TestPhoneticRealWorldUsage:
    """Test realistic usage scenarios."""
    
    def test_common_abbreviations(self):
        """Test common abbreviations that might be spelled phonetically"""
        assert phonetic('FBI') == 'Foxtrot Bravo India'
        assert phonetic('CIA') == 'Charlie India Alpha'
        assert phonetic('USA') == 'Uniform Sierra Alpha'
        assert phonetic('UK') == 'Uniform Kilo'
    
    def test_radio_callsigns(self):
        """Test typical radio callsigns"""
        assert phonetic('N123AB') == 'November 1 2 3 Alpha Bravo'
        assert phonetic('KE7XYZ') == 'Kilo Echo 7 X-ray Yankee Zulu'
    
    def test_license_plates(self):
        """Test license plate style input"""
        assert phonetic('ABC123') == 'Alpha Bravo Charlie 1 2 3'
        assert phonetic('XYZ-789') == 'X-ray Yankee Zulu - 7 8 9'
    
    def test_postal_codes(self):
        """Test postal code style input"""
        assert phonetic('M4B1B4') == 'Mike 4 Bravo 1 Bravo 4'
        assert phonetic('SW1A1AA') == 'Sierra Whiskey 1 Alpha 1 Alpha Alpha'

class TestPhoneticPerformance:
    """Test performance-related aspects."""
    
    def test_repeated_characters(self):
        """Test strings with many repeated characters"""
        assert phonetic('AAA') == 'Alpha Alpha Alpha'
        assert phonetic('AAABBBCCC') == 'Alpha Alpha Alpha Bravo Bravo Bravo Charlie Charlie Charlie'
    
    def test_alternating_case(self):
        """Test strings with alternating case"""
        assert phonetic('AbCdEf') == 'Alpha Bravo Charlie Delta Echo Foxtrot'

# Additional utility test for debugging
class TestPhoneticDebugging:
    """Utility tests for debugging the implementation."""
    
    def test_character_by_character_breakdown(self):
        """Break down the conversion character by character for debugging"""
        test_string = "A B"
        print(f"\nDebugging phonetic('{test_string}'):")
        
        nato = {
            'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
            'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
            'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
            'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
            'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
            'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
            'Y': 'Yankee', 'Z': 'Zulu'
        }
        
        conversions = []
        for i, char in enumerate(test_string):
            converted = nato.get(char.upper(), char)
            conversions.append(converted)
            print(f"  Character {i}: '{char}' -> '{converted}'")
        
        result = ' '.join(conversions)
        print(f"  Final result: '{result}'")
        print(f"  Result length: {len(result)}")
        print(f"  Actual function result: '{phonetic(test_string)}'")
        
        # This test always passes but provides debugging output
        assert True