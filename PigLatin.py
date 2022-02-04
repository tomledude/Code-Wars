def pig_it(text):
    text = text.split()
    new_text = []
    for x in text:
        if x.isalpha():
            x = x[1:]+x[0]
            x = x + 'ay'
        new_text.append(x)
    
    new_text = ' '.join(new_text)
    return new_text
