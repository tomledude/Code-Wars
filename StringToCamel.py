def to_camel_case(text):
    lower = False
    if text!='':
        text = text.replace('_','-')
        text = text.split('-')
        text = ' '.join(text)
        print(text)
        lower = text[0].isupper()
        print(lower)
        text = text.title()
        text = text.split(' ')
        text = ''.join(text)
        if lower == False:
            text = text[0].lower() + text[1:]
        return text
    else:   
        return ''
