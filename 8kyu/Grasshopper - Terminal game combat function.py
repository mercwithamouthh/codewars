def combat(health, damage):
    damagetaken = health - damage

    if damagetaken > 0:
        return damagetaken
    else:
        return 0
    