def divisor(n):
    divisor=[]
    for i in range(1,n+1):
        if n%i==0:
            divisor.append(i)
    return divisor
    return divisor
a= divisor(6)
print(a)
