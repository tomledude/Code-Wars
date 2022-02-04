def duplicate_count(text):
    text = text.lower()
    char_ = []
    dup_sum = 0

    for x in text:
        if x not in char_:
            char_.append(x)

    for x in range(len(char_)):
        if text.count(char_[x]) > 1:
            dup_sum = dup_sum+1

    return dup_sum
