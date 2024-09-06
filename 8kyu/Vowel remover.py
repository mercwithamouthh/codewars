def shortcut(s):
    vowels = "aeiou"
    result = ''.join([i for i in s if i not in vowels])
    return result
