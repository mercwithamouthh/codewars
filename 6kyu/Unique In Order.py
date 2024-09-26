def unique_in_order(sequence):
    # Initialize an empty list to store the result
    result = []

    # Loop through the sequence and append an item to the result
    # only if it's different from the last appended item
    for i, item in enumerate(sequence):
        if i == 0 or item != sequence[i-1]:
            result.append(item)
    return result
#or another way i liked

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result