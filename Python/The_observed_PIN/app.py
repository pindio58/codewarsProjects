from itertools import product
def get_pins(observed):
    our_dict={
        '1':[1,2,4],
        '2':[1,2,3,5],
        '3':[2,3,6],
        '4':[1,4,5,7],
        '5':[2,4,5,6,8],
        '6':[3,5,6,9],
        '7':[4,7,8],
        '8':[5,7,8,9,0],
        '9':[6,8,9],
        '0':[0,8]
    }
    our_list=list(str(observed))
    
    x=[our_dict[num] for num in our_list]
    k=list(product(*x))
    p=[]
    
    for kk in k:
        p.append(''.join(str(e) for e in kk))
    
    return p