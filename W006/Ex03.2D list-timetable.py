def time(a):
    num = []
    for i in range(a):
        list = []
        for j in range(a):
            cal=(i+1)*(j+1)
            list.append(cal)
        num.append(list)
    return num


b=time(12)
print(b)