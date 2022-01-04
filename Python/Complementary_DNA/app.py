def DNA_strand(dna):
    word = ''
    for letter in dna:
        if letter == 'A':
            word+='T'
        elif letter =='T':
            word+='A'
        elif letter == 'G':
            word +='C'
        else:
            word+='G'    
    return word