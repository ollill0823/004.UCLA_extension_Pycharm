def recIncr(lst):
    #  incursive restriction item: when len(lst)=0 stop
    if len(lst) ==0:
        return []
    else:
        return recIncr(lst[:-1]) +[lst[-1]+1]


a=[3,1,1,5]
print(recIncr(a))










