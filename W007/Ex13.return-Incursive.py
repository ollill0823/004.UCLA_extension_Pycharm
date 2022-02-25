def recNeg(lst):
    if len(lst) ==0:
        return False
    else:
        return recNeg(lst[:-1]) or lst[-1] <0


a=[3,1,-1,5]
b=recNeg(a)
print(b)










