def breakChocolate(n, m):
    if not n or not m:
        return 0
    if n<=0 and m <0:
        return 0
    
    return (m-1) + ((n-1)*(m))
    