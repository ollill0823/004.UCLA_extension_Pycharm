def recMap(lst,f):
    if len(lst)==0:
        return []
    return recMap(lst[:-1],f ) + [f(lst[-1])]

from math import sqrt
table=[[1,2,3],[4,5,6]]
b=recMap(table,sum)
print(b)
print([table[-1]])








