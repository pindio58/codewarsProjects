from collections import Counter
def duplicate_encode(word):
    data = Counter(word.lower())
    lis= [ ')' if data[letter.lower()]>1 else '(' for letter in word ]
    lis=''.join(lis)
    return lis