def interest(n):
    double= 1+n
    sum=1
    while double**(sum+1)<2:
        sum += 1
    return sum+1

a=interest(0.07)
print(a)
