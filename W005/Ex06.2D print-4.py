def add2D(t1,t2):
    w=len(t1)
    x=len(t1[0])
    for i in range(w):
        for j in range(x):
            t1[i][j] +=t2[i][j]
    for row in t1:
        print(row)


t=[[4,7,2,5], [5,1,9,2],[8,3,6,6]]
s=[[0,1,2,0],[0,1,1,1],[0,1,0,0]]

a=add2D(t,s)



