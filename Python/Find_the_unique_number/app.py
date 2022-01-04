def find_uniq(arr):
    num = set(arr[1:])
    if len(num) ==1:
        return arr[0]
    arry = [arr[0]]+[a for a in num]
    if arry[0] != arry[1]:
        if arry[1] != arry[2]:
            return arry[1]
        else:
            return arry[0]
    return arry[2]  # n: unique integer in the array