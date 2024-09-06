def set_alarm(employed, vacation):
    if employed and not vacation:
        return True
    elif not employed and vacation:
        return False
    elif not employed and not vacation:
        return False
    elif employed and vacation:
        return False