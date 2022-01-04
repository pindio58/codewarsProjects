import string
puncs = string.punctuation

def pig_it(text):
    req_list=[]
    for letter in text.split():
        
        if letter not in puncs: req_list.append(letter[1:]+letter[0]+'ay')
        else: req_list.append(letter)
    
    return' '.join(letter for letter in req_list)