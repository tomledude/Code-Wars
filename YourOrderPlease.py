def order(sentence):
    words = sentence.split()
    new_sent = []

    for y in range(10):
        for x in words:
            if str(y) in x:
                new_sent.append(x)
    
    joined_sent = " ".join(new_sent)

    return joined_sent
