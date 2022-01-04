from math import sqrt
from copy import deepcopy

def sub_prog(num,req_dict,Out_list,flag_dict,perf_sqrs):
    flag_dict[num]=False
    if len(Out_list)==0:
        Out_list.append(num)
    if num + Out_list[-1] in perf_sqrs and num !=Out_list[-1]:
        Out_list.append(num)
    for x in req_dict[num]:
        if flag_dict[x]:
            sub_prog(x,req_dict,Out_list,flag_dict,perf_sqrs)
            if len(Out_list)==len(req_dict):
                return Out_list
            popped=Out_list.pop()
            flag_dict[popped]=True
    
    # return Out_list
        
def square_sums_row(org):
    nums_sqs = [n for n in range (2*org)]
    nums = [x for x in range(1,org+1)]
    perf_sqrs = [x for x in nums_sqs if int(sqrt(x))**2==x]
    req_dict  = {}
    Out_list  = []
    flag_dict = {}
    
    # making mapped dict
    for n in nums:
        req_dict[n]=[x for x in nums if n!=x and x+n in perf_sqrs]
    
    # making flag dictionary
    for num in nums:
        flag_dict[num]=True
    
    flag_dict_cpy = deepcopy(flag_dict)
    
    for num in nums:
        if sub_prog(num,req_dict,Out_list,flag_dict,perf_sqrs):
            return Out_list
        else:
            flag_dict=deepcopy(flag_dict_cpy)
            Out_list=[]
    
    return False