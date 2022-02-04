def find_it(seq):
    int_list = []

    for x in seq:
        if x not in int_list:
            int_list.append(x)
            
    for x in int_list:
        if (seq.count(x)%2 == 1):
            return x
