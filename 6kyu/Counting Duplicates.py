def duplicate_count(text):
    # Convert the text to lowercase to handle case insensitivity
    text = text.lower()

    # Create a dictionary to count occurrences of each character
    counts = {}

    # Iterate through the text and count characters
    for char in text:
        counts[char] = counts.get(char, 0) + 1

    # Count how many characters occur more than once
    duplicates = sum(1 for count in counts.values() if count > 1)

    return duplicates
