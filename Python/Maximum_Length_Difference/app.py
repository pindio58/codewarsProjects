def mxdiflg(a1, a2):
    if (not a1) or (not a2):
        return -1
    min1=len(min(a1 , key=len))
    max1=len(max(a1 , key=len))
    min2=len(min(a2 , key=len))
    max2=len(max(a2 , key=len))
    
    return max(abs(min1-max2), abs(min2-max1))