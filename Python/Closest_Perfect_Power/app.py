#import numpy module
import numpy as np

#This function will calculate the roots from 2 till 10th
def sub_function(num):
    roots=[num**(1/float(val)) for val in range(2,10)]
    return roots

def closest_power(num):
    if num<=4:
        return 4
    
    num=round(num)                                               # round the value to nearest
    arr=[]                                                       # initiated empty array
    
    roots=list(map(round,sub_function(num)))                    # rounded roots
    
    for root in roots:
        for val in range(2,10):
            power=root**val
            arr.append(power)
    
    arr=np.array(arr)
    difference=min(abs(arr-num))
    
    return int(min(arr[abs(arr-num)==difference]))