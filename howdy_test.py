import pytest

def howdy(name):
    """Print a howdy greeting for the given name."""
    print(f"Howdy {name}!")

class TestHowdyFunction:
    """Test suite for the howdy function using pytest."""
    
    def test_howdy_with_regular_name(self, capsys):
        """Test howdy function with a regular name."""
        howdy("Alice")
        captured = capsys.readouterr()
        assert captured.out == "Howdy Alice!\n"
        assert captured.err == ""
    
    def test_howdy_with_empty_string(self, capsys):
        """Test howdy function with an empty string."""
        howdy("")
        captured = capsys.readouterr()
        assert captured.out == "Howdy !\n"
        assert captured.err == ""
    
    def test_howdy_with_whitespace_name(self, capsys):
        """Test howdy function with whitespace characters."""
        howdy("   ")
        captured = capsys.readouterr()
        assert captured.out == "Howdy    !\n"
        assert captured.err == ""
    
    def test_howdy_with_long_name(self, capsys):
        """Test howdy function with a very long name."""
        long_name = "A" * 100
        howdy(long_name)
        captured = capsys.readouterr()
        assert captured.out == f"Howdy {long_name}!\n"
        assert captured.err == ""
    
    def test_howdy_with_special_characters(self, capsys):
        """Test howdy function with special characters in name."""
        special_name = "José-María O'Connor"
        howdy(special_name)
        captured = capsys.readouterr()
        assert captured.out == f"Howdy {special_name}!\n"
        assert captured.err == ""
    
    def test_howdy_with_numbers(self, capsys):
        """Test howdy function with numeric characters."""
        howdy("User123")
        captured = capsys.readouterr()
        assert captured.out == "Howdy User123!\n"
        assert captured.err == ""
    
    def test_howdy_with_unicode_characters(self, capsys):
        """Test howdy function with Unicode characters."""
        unicode_name = "山田太郎"  # Japanese characters
        howdy(unicode_name)
        captured = capsys.readouterr()
        assert captured.out == f"Howdy {unicode_name}!\n"
        assert captured.err == ""
    
    def test_howdy_with_numeric_input(self, capsys):
        """Test howdy function with numeric input (should convert to string)."""
        howdy(42)
        captured = capsys.readouterr()
        assert captured.out == "Howdy 42!\n"
        assert captured.err == ""
    
    def test_howdy_with_boolean_input(self, capsys):
        """Test howdy function with boolean input."""
        howdy(True)
        captured = capsys.readouterr()
        assert captured.out == "Howdy True!\n"
        assert captured.err == ""
    
    def test_howdy_with_list_input(self, capsys):
        """Test howdy function with list input (should convert to string)."""
        howdy([1, 2, 3])
        captured = capsys.readouterr()
        assert captured.out == "Howdy [1, 2, 3]!\n"
        assert captured.err == ""
    
    def test_howdy_with_none_input(self):
        """Test howdy function with None input (should raise TypeError)."""
        with pytest.raises(TypeError):
            howdy(None)

class TestHowdyParameterized:
    """Parameterized tests for the howdy function."""
    
    @pytest.mark.parametrize("name,expected", [
        ("John", "Howdy John!\n"),
        ("Mary Jane", "Howdy Mary Jane!\n"),
        ("Dr. Smith", "Howdy Dr. Smith!\n"),
        ("user@email.com", "Howdy user@email.com!\n"),
        ("123-456", "Howdy 123-456!\n"),
        ("", "Howdy !\n"),
        ("   ", "Howdy    !\n"),
        ("André", "Howdy André!\n"),
        ("User123", "Howdy User123!\n"),
    ])
    def test_howdy_with_various_names(self, capsys, name, expected):
        """Test howdy function with various name inputs."""
        howdy(name)
        captured = capsys.readouterr()
        assert captured.out == expected
        assert captured.err == ""
    
    @pytest.mark.parametrize("input_value,expected_output", [
        (42, "Howdy 42!\n"),
        (3.14, "Howdy 3.14!\n"),
        (True, "Howdy True!\n"),
        (False, "Howdy False!\n"),
        ([1, 2, 3], "Howdy [1, 2, 3]!\n"),
        ({"key": "value"}, "Howdy {'key': 'value'}!\n"),
        ((1, 2, 3), "Howdy (1, 2, 3)!\n"),
    ])
    def test_howdy_with_non_string_types(self, capsys, input_value, expected_output):
        """Test howdy function with various non-string input types."""
        howdy(input_value)
        captured = capsys.readouterr()
        assert captured.out == expected_output
        assert captured.err == ""

class TestHowdyEdgeCases:
    """Edge case tests for the howdy function."""
    
    def test_howdy_with_newline_in_name(self, capsys):
        """Test howdy function with newline character in name."""
        howdy("John\nDoe")
        captured = capsys.readouterr()
        assert captured.out == "Howdy John\nDoe!\n"
        assert captured.err == ""
    
    def test_howdy_with_tab_in_name(self, capsys):
        """Test howdy function with tab character in name."""
        howdy("John\tDoe")
        captured = capsys.readouterr()
        assert captured.out == "Howdy John\tDoe!\n"
        assert captured.err == ""
    
    def test_howdy_with_emoji(self, capsys):
        """Test howdy function with emoji characters."""
        howdy("John 😊")
        captured = capsys.readouterr()
        assert captured.out == "Howdy John 😊!\n"
        assert captured.err == ""
    
    def test_howdy_multiple_calls(self, capsys):
        """Test multiple consecutive calls to howdy function."""
        howdy("Alice")
        howdy("Bob")
        captured = capsys.readouterr()
        assert captured.out == "Howdy Alice!\nHowdy Bob!\n"
        assert captured.err == ""
    
    def test_howdy_with_very_long_string(self, capsys):
        """Test howdy function with extremely long string."""
        long_name = "x" * 10000
        howdy(long_name)
        captured = capsys.readouterr()
        assert captured.out == f"Howdy {long_name}!\n"
        assert captured.err == ""

class TestHowdyMocking:
    """Tests using pytest's monkeypatch for mocking."""
    
    def test_howdy_print_called_correctly(self, monkeypatch, capsys):
        """Test that the print function is called with correct formatting."""
        print_calls = []
        
        def mock_print(*args, **kwargs):
            print_calls.append((args, kwargs))
            # Still call original print to capture output
            __builtins__['print'](*args, **kwargs)
        
        monkeypatch.setattr('builtins.print', mock_print)
        
        howdy("TestUser")
        
        # Verify print was called once with correct arguments
        assert len(print_calls) == 1
        assert print_calls[0][0] == ("Howdy TestUser!",)
        
        # Verify output was correct
        captured = capsys.readouterr()
        assert captured.out == "Howdy TestUser!\n"

# Fixtures for reusable test data
@pytest.fixture
def sample_names():
    """Fixture providing sample names for testing."""
    return [
        "Alice",
        "Bob Smith", 
        "José-María",
        "user@domain.com",
        "123",
        ""
    ]

@pytest.fixture
def special_characters():
    """Fixture providing names with special characters."""
    return [
        "café",
        "naïve",
        "Müller",
        "北京",
        "🎉 Party! 🎉"
    ]

class TestHowdyWithFixtures:
    """Tests using custom fixtures."""
    
    def test_howdy_with_sample_names(self, capsys, sample_names):
        """Test howdy function with fixture-provided sample names."""
        for name in sample_names:
            # Clear previous captures
            capsys.readouterr()
            
            howdy(name)
            captured = capsys.readouterr()
            assert captured.out == f"Howdy {name}!\n"
            assert captured.err == ""
    
    def test_howdy_with_special_characters(self, capsys, special_characters):
        """Test howdy function with fixture-provided special characters."""
        for name in special_characters:
            # Clear previous captures
            capsys.readouterr()
            
            howdy(name)
            captured = capsys.readouterr()
            assert captured.out == f"Howdy {name}!\n"
            assert captured.err == ""

# Custom markers for test organization
pytestmark = pytest.mark.howdy

class TestHowdyMarked:
    """Tests with custom markers for selective running."""
    
    @pytest.mark.slow
    def test_howdy_performance_large_input(self, capsys):
        """Test howdy function performance with very large input."""
        huge_name = "A" * 1000000  # 1 million characters
        howdy(huge_name)
        captured = capsys.readouterr()
        assert captured.out.startswith("Howdy A")
        assert captured.out.endswith("!\n")
        assert len(captured.out) == len(huge_name) + 8  # "Howdy " + "!\n"
    
    @pytest.mark.integration
    def test_howdy_integration_with_input_processing(self, capsys):
        """Integration test simulating real-world usage."""
        # Simulate processing user input
        user_inputs = ["  Alice  ", "BOB", "charlie@email.com"]
        processed_names = [name.strip().title() for name in user_inputs]
        
        for name in processed_names:
            howdy(name)
        
        captured = capsys.readouterr()
        expected = "Howdy Alice!\nHowdy Bob!\nHowdy Charlie@Email.Com!\n"
        assert captured.out == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])