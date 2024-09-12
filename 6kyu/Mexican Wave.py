def wave(people):
    result = []
    for i in range(len(people)):
        if people[i].isalpha():  # Ensure only alphabetic characters are modified
            wave_word = people[:i] + people[i].upper() + people[i+1:]
            result.append(wave_word)
    return result
