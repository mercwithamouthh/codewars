def duplicate_encode(word):
    word = word.lower()
    duplicate = ""
    for x in word:
        if word.count(x) > 1:
            duplicate += ")"
        else:
            duplicate += "("
    return duplicate
