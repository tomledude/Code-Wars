def productFib(prod):
    n1, n2 = 0, 1
    
    while prod > n2*n1:
        n_new = n1 + n2
        n1 = n2
        n2 = n_new

    return [n1, n2, prod == n2*n1]
