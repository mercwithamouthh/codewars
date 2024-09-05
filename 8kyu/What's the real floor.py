def get_real_floor(n):
    if n <= 0:
         return n
    elif n == 1:
        return 0
    elif n == 15:
        return n - 2
    else:
        return n - 1
#this is wrong FIX IT