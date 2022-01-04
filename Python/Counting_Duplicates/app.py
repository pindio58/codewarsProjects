from collections import Counter
def duplicate_count(text):
    text=text.lower()
    values=Counter(text) 
    return len(list(filter(lambda x:values[x]>1 ,values)))
    