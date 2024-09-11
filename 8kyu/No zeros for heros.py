def no_boring_zeros(n):
    # Convert the integer to a string and remove trailing zeros
    str_n = str(n).rstrip('0')
    # Convert back to integer; if the result is an empty string, return 0
    return int(str_n) if str_n else 0