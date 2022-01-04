def sum_pairs(l,s):
    
    fill_return={}
    for num in l:
        temp = s-num
        if temp in fill_return.values():
            return list((temp,num))
        else:
            fill_return[temp]=num 
    
    return None
    
    return None