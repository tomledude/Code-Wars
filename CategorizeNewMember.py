def open_or_senior(data):
    out_list = []
    
    for x in data:
        if (x[0] >= 55) & (x[1] > 7):
            out_list.append('Senior')
        else:
            out_list.append('Open')
            
    return out_list
