def flip_dict(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    if len(set(dictionary.values())) != len(dictionary):
        raise ValueError("Duplicate dictionary values found")
    return {
        value: key
        for key, value in dictionary.items()
    }