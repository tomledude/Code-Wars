import math

def nb_year(p0, percent, aug, p):
    percent  = percent/100
    n=0

    while p0 < p:
        p0 = p0 + p0*percent + aug
        p0 = math.floor(p0)
        n=n+1

    return n
