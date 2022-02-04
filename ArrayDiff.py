def array_diff(a, b):
    for x in b:
        for y in a:
            if y==x:
                while y in a: a.remove(y)
            
    return a
