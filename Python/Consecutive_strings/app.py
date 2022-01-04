def longest_consec(strarr, k):
    if not strarr:
        return ''
    if (not k) or (k<=0):
        return ''
    if k>len(strarr):
        return ''
    ourDict,counter={},0
    for num in range(len(strarr)-k+1):
        word=''.join(strarr[counter:k])
        ourDict[word]=len(word)
        counter+=1; k+=1
    return max(ourDict, key=ourDict.get)