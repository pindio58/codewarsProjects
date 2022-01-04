import re

def to_camel_case(text):
    liss = re.split('[- _]',text)
    if text:
        if text[0].isupper():
            return ''.join(name.title() for name in liss)
        else:
            return liss[0]+ ''.join(name.title() for name in liss[1:])
    else:
        return ''