def order(sentence):
    lissy = []
    for num in range(len(sentence.split(' '))):
        lissy.append('')
    print(lissy)
    for name in sentence.split(' '):
        for num in name:
            if num.isdigit():
                lissy[int(num)-1] = name
                print(lissy)
    return ' '.join( numm for numm in lissy if numm != '')