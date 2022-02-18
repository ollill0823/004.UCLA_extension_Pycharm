def list(a,b):
    num=[]
    for i in range(len(a)):
        for j in range(len(b)):
            final=a[i]+b[j]
            num.append(final)
    num.sort()
    return num

alist=[3,15,44]
blist=[4,6,32]

c=list(alist,blist)
print(c)