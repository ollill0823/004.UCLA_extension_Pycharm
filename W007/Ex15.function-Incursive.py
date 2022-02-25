def recMap(lst,f):
    if len(lst)==0:
        return []
    return recMap(lst[:-1],f ) + [f(lst[-1])]

from math import sqrt
a=[2,5,10,17,26]
b=sqrt
print(recMap(a,b))








