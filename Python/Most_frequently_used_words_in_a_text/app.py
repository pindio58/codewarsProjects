def top_3_words(text):
    if not text: return []
    if set(text)=={" ","'"}: return []
    
    sp= list ('!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~')
    
    for tx in text:
        if tx in sp: text=text.replace(tx,' ')
    text = [x.lower() for x in text.split()]
    text = dict( zip( list(set(text)), [text.count(x) for x in set(text)]))
    text = {k: v for k, v in sorted(text.items(), key=lambda item: item[1], reverse=True)}
    
    if len(text)<2: return [k for k in list(text)[:1]]
    if len(text)<3: return [k for k in list(text)[:2]]
    
    return [k  for k in list(text)[:3]]