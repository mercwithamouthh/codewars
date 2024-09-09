def how_much_i_love_you(nb_petals):
    phrases = [
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all"
    ]
    # Use modulus to cycle through the phrases
    return phrases[nb_petals % len(phrases)- 1]
