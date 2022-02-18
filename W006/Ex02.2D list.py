def list(a,b):
    num=[]
    for i in range(len(a)):
        for j in range(len(a[0])):
            final=a[i][j]*b[i][j]
            num.append(final)

    return num

alist=[[1,2,3],[2,4,6],[2,8,18]]
blist=[[4,5,6],[3,5,7],[9,5,42]]

c=list(alist,blist)
print(c)