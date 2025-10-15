import pytest

def flip_dict(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    if len(set(dictionary.values())) != len(dictionary):
        raise ValueError("Duplicate dictionary values found")
    return {
        value: key
        for key, value in dictionary.items()
    }

class TestFlipDictBasicFunctionality:
    """Tests for basic flip_dict functionality."""
    
    def test_flip_dict_simple(self):
        """Test flip_dict with simple key-value pairs."""
        input_dict = {'a': 1, 'b': 2, 'c': 3}
        expected = {1: 'a', 2: 'b', 3: 'c'}
        result = flip_dict(input_dict)
        assert result == expected
    
    def test_flip_dict_empty_dictionary(self):
        """Test flip_dict with empty dictionary."""
        result = flip_dict({})
        assert result == {}
    
    def test_flip_dict_single_item(self):
        """Test flip_dict with single key-value pair."""
        input_dict = {'hello': 'world'}
        expected = {'world': 'hello'}
        result = flip_dict(input_dict)
        assert result == expected
    
    def test_flip_dict_string_keys_and_values(self):
        """Test flip_dict with string keys and values."""
        input_dict = {'first': 'uno', 'second': 'dos', 'third': 'tres'}
        expected = {'uno': 'first', 'dos': 'second', 'tres': 'third'}
        result = flip_dict(input_dict)
        assert result == expected
    
    def test_flip_dict_mixed_hashable_types(self):
        """Test flip_dict with mixed hashable types."""
        input_dict = {1: 'a', 'b': 2, 3.14: 'pi', 'tuple': (1, 2)}
        expected = {'a': 1, 2: 'b', 'pi': 3.14, (1, 2): 'tuple'}
        result = flip_dict(input_dict)
        assert result == expected

class TestFlipDictDuplicateValues:
    """Tests for flip_dict duplicate value handling."""
    
    def test_flip_dict_duplicate_values_raises_error(self):
        """Test that duplicate values raise ValueError."""
        input_dict = {'a': 1, 'b': 1, 'c': 2}  # 'a' and 'b' both map to 1
        with pytest.raises(ValueError, match="Duplicate dictionary values found"):
            flip_dict(input_dict)
    
    def test_flip_dict_multiple_duplicate_values(self):
        """Test with multiple sets of duplicate values."""
        input_dict = {'a': 1, 'b': 1, 'c': 2, 'd': 2}
        with pytest.raises(ValueError, match="Duplicate dictionary values found"):
            flip_dict(input_dict)
    
    def test_flip_dict_all_same_values(self):
        """Test with all values being the same."""
        input_dict = {'a': 'same', 'b': 'same', 'c': 'same'}
        with pytest.raises(ValueError, match="Duplicate dictionary values found"):
            flip_dict(input_dict)

class TestFlipDictTypeErrors:
    """Tests for flip_dict type-related errors."""
    
    def test_flip_dict_with_none_input(self):
        """Test flip_dict with None input - should raise AttributeError."""
        with pytest.raises(AttributeError):
            flip_dict(None)
    
    def test_flip_dict_with_string_input(self):
        """Test flip_dict with string input - should raise AttributeError."""
        with pytest.raises(AttributeError):
            flip_dict("not a dictionary")
    
    def test_flip_dict_with_list_input(self):
        """Test flip_dict with list input - should raise AttributeError."""
        with pytest.raises(AttributeError):
            flip_dict([1, 2, 3])
    
    def test_flip_dict_with_integer_input(self):
        """Test flip_dict with integer input - should raise AttributeError."""
        with pytest.raises(AttributeError):
            flip_dict(42)

class TestFlipDictUnhashableValues:
    """Tests for flip_dict with unhashable values (main source of errors)."""
    
    def test_flip_dict_with_list_values(self):
        """Test flip_dict with list values - should raise TypeError."""
        input_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        with pytest.raises(TypeError):
            flip_dict(input_dict)
    
    def test_flip_dict_with_dict_values(self):
        """Test flip_dict with dictionary values - should raise TypeError."""
        input_dict = {'a': {'nested': 'dict'}, 'b': {'another': 'dict'}}
        with pytest.raises(TypeError):
            flip_dict(input_dict)
    
    def test_flip_dict_with_set_values(self):
        """Test flip_dict with set values - should raise TypeError."""
        input_dict = {'a': {1, 2, 3}, 'b': {4, 5, 6}}
        with pytest.raises(TypeError):
            flip_dict(input_dict)
    
    def test_flip_dict_mixed_hashable_unhashable_values(self):
        """Test flip_dict with mix of hashable and unhashable values."""
        input_dict = {'a': 1, 'b': [1, 2, 3], 'c': 'string'}
        with pytest.raises(TypeError):
            flip_dict(input_dict)
    
    def test_flip_dict_with_duplicate_list_values(self):
        """Test flip_dict with duplicate list values - fails at set() creation."""
        input_dict = {'a': [1, 2], 'b': [1, 2]}  # Duplicate unhashable values
        with pytest.raises(TypeError):
            flip_dict(input_dict)

class TestFlipDictEdgeCases:
    """Edge case tests for flip_dict."""
    
    def test_flip_dict_with_none_values(self):
        """Test flip_dict with None values (None is hashable)."""
        input_dict = {'a': None, 'b': 'value'}
        expected = {None: 'a', 'value': 'b'}
        result = flip_dict(input_dict)
        assert result == expected
    
    def test_flip_dict_with_boolean_values(self):
        """Test flip_dict with boolean values."""
        input_dict = {'true_key': True, 'false_key': False}
        expected = {True: 'true_key', False: 'false_key'}
        result = flip_dict(input_dict)
        assert result == expected
    
    def test_flip_dict_with_tuple_values(self):
        """Test flip_dict with tuple values (tuples are hashable)."""
        input_dict = {'a': (1, 2), 'b': (3, 4)}
        expected = {(1, 2): 'a', (3, 4): 'b'}
        result = flip_dict(input_dict)
        assert result == expected
    
    def test_flip_dict_with_nested_tuple_containing_unhashable(self):
        """Test flip_dict with tuple containing unhashable elements."""
        # This should fail because tuples containing lists are unhashable
        input_dict = {'a': ([1, 2], 3)}
        with pytest.raises(TypeError):
            flip_dict(input_dict)
    
    def test_flip_dict_zero_and_false_distinction(self):
        """Test that 0 and False are treated as the same key (Python behavior)."""
        input_dict = {'zero': 0, 'false': False}
        # This should raise ValueError because 0 and False are considered equal
        with pytest.raises(ValueError, match="Duplicate dictionary values found"):
            flip_dict(input_dict)
    
    def test_flip_dict_one_and_true_distinction(self):
        """Test that 1 and True are treated as the same key (Python behavior)."""
        input_dict = {'one': 1, 'true': True}
        # This should raise ValueError because 1 and True are considered equal
        with pytest.raises(ValueError, match="Duplicate dictionary values found"):
            flip_dict(input_dict)

class TestFlipDictParameterized:
    """Parameterized tests for flip_dict."""
    
    @pytest.mark.parametrize("input_dict,expected", [
        ({}, {}),
        ({'a': 1}, {1: 'a'}),
        ({'a': 1, 'b': 2}, {1: 'a', 2: 'b'}),
        ({1: 'a', 2: 'b'}, {'a': 1, 'b': 2}),
        ({'x': None}, {None: 'x'}),
        ({'tuple_key': (1, 2, 3)}, {(1, 2, 3): 'tuple_key'}),
    ])
    def test_flip_dict_valid_cases(self, input_dict, expected):
        """Test flip_dict with various valid input cases."""
        result = flip_dict(input_dict)
        assert result == expected
    
    @pytest.mark.parametrize("invalid_input", [
        None,
        "string",
        [1, 2, 3],
        123,
        {1, 2, 3},  # set
        (1, 2, 3),  # tuple
    ])
    def test_flip_dict_invalid_input_types(self, invalid_input):
        """Test flip_dict with invalid input types."""
        with pytest.raises(AttributeError):
            flip_dict(invalid_input)
    
    @pytest.mark.parametrize("dict_with_unhashable", [
        {'a': [1, 2]},  # list value
        {'a': {'nested': 'dict'}},  # dict value
        {'a': {1, 2, 3}},  # set value
        {'a': [1], 'b': 'valid'},  # mixed
    ])
    def test_flip_dict_unhashable_values(self, dict_with_unhashable):
        """Test flip_dict with various unhashable values."""
        with pytest.raises(TypeError):
            flip_dict(dict_with_unhashable)

class TestFlipDictComplexScenarios:
    """Complex scenario tests for flip_dict."""
    
    def test_flip_dict_large_dictionary(self):
        """Test flip_dict with a large dictionary."""
        input_dict = {f'key_{i}': i for i in range(1000)}
        result = flip_dict(input_dict)
        expected = {i: f'key_{i}' for i in range(1000)}
        assert result == expected
        assert len(result) == 1000
    
    def test_flip_dict_double_flip(self):
        """Test that flipping a dictionary twice returns to original."""
        original = {'a': 1, 'b': 2, 'c': 3}
        flipped_once = flip_dict(original)
        flipped_twice = flip_dict(flipped_once)
        assert flipped_twice == original
    
    def test_flip_dict_preserves_type_information(self):
        """Test that flip_dict preserves type information of keys and values."""
        input_dict = {1: 'one', 2.5: 'two_point_five', 'three': 3}
        result = flip_dict(input_dict)
        
        # Check that types are preserved
        assert isinstance(result['one'], int)
        assert isinstance(result['two_point_five'], float)
        assert isinstance(result[3], str)

class TestFlipDictErrorMessages:
    """Tests focusing on error message content and behavior."""
    
    def test_flip_dict_error_message_content(self):
        """Test that the error message is exactly as expected."""
        input_dict = {'a': 1, 'b': 1}
        try:
            flip_dict(input_dict)
            pytest.fail("Expected ValueError was not raised")
        except ValueError as e:
            assert str(e) == "Duplicate dictionary values found"
    
    def test_flip_dict_unhashable_error_type(self):
        """Test that unhashable values raise TypeError, not ValueError."""
        input_dict = {'a': [1, 2, 3]}
        with pytest.raises(TypeError):
            flip_dict(input_dict)
        
        # Make sure it's not raising ValueError
        with pytest.raises(TypeError):
            try:
                flip_dict(input_dict)
            except ValueError:
                pytest.fail("Should raise TypeError, not ValueError")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])