def xo(s):
    s = s.lower()
    xx = s.count("x")
    oo = s.count("o")
    if xx == oo:
        return True
    else:
        return False
#or easier and less complicated solution
    return s.lower().count('x') == s.lower().count('o')
