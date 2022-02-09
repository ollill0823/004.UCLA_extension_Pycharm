def print2D(t):
    for i in range(len(t)):
        for j in range(len(t[0])):
            t[i][j] +=1
        print('')



t=[[4,7,2,5], [5,1,9,2],[8,3,6,6]]
a=print2D(t)


