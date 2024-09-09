def remove(s):
    if s.endswith("!"):
        return s[:-1]  # Slice the string to remove the last character
    return s