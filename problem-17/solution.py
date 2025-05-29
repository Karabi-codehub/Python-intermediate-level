def flatten_dict(d, parent_key='', sep='.'):
    """
    d: input dictionary to flatten
    parent_key: key prefix (used in recursion to track key hierarchy)
    sep: separator between keys (default is '.')
    """
    items = {}  # final flat dictionary

    for k, v in d.items():
        # create new key: add parent_key + current key
        new_key = parent_key + sep + k if parent_key else k

        # if value is a dictionary, call function recursively
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v  # if not a dictionary, just add the key-value

    return items
nested = {"a": {"b": 1, "c": {"d": 2}}}
flat = flatten_dict(nested)
print(flat)
