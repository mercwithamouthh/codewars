def is_square(n):
    if n < 0:
        return False

    square = int(n ** .5)

    return square * square == n
