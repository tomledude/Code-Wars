def xo(s):
    num_x = s.count('x') + s.count('X')
    num_o = s.count('o') + s.count('O')

    if num_x == num_o:
        return True
    else:
        return False
