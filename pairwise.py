def pairwise(iterable):
    """Return successive overlapping pairs from iterable."""
    result = []
    items = list(iterable)
    for i in range(len(items)):
        if i + 1 < len(items):
            result.append((items[i], items[i + 1]))
        else:
            result.append((items[i], None))
    return result