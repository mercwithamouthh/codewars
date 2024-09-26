def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    northsouth = walk.count('n') - walk.count('s')
    eastwest = walk.count('e') - walk.count('w')

    return northsouth == 0 and eastwest == 0