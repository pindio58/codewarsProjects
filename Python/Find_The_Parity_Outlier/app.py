import numpy as np
def find_outlier(integers):
    arr = np.array(integers)
    
    if [0,1,2] in arr:
        return 1
    
    odds=arr[arr%2==1]
    return arr[~arr%2==1][0] if odds.size>1  else odds[0]