def digital_root(n):
    summed = sum([int(num) for num in str(n)])
    if len(str(summed)) == 1:
        return summed
    else:
        return digital_root(summed)