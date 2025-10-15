def flip_dict(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    if len(set(dictionary.values())) != len(dictionary):
        raise ValueError("Duplicate dictionary values found")
    return {
        value: key
        for key, value in dictionary.items()
    }

def flip_dict_annotated(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    
    # ERROR 1: No type checking - function will fail with non-dict types
    # This will raise AttributeError if dictionary is None, list, string, etc.
    
    # ERROR 2: Doesn't handle unhashable values
    # If dictionary values contain lists, dicts, sets, etc., this will fail
    # when trying to use them as keys in the returned dictionary
    
    if len(set(dictionary.values())) != len(dictionary):
        # ERROR 3: set() call will fail if values are unhashable
        # Example: {1: [1, 2], 2: [3, 4]} will raise TypeError here
        
        raise ValueError("Duplicate dictionary values found")
        
    return {
        value: key  # ERROR 4: This line will fail if 'value' is unhashable
        for key, value in dictionary.items()
        # ERROR 5: No validation that 'value' can be used as a dictionary key
    }

# ADDITIONAL ISSUES:
# - No handling of empty dictionary (though this actually works fine)
# - No docstring examples showing expected behavior
# - ValueError message could be more descriptive
# - No handling of None values (though None is hashable, so this works)