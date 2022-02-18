def pop(x):
    num=0
    while x>=10000:
        num +=1
        x *=0.97
    return num

a=pop(11000)
print(a)