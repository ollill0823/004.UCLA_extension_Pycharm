def time(a):
    list = []
    for i in range(a):
        list.append([])    ## define list number at first
        for j in range(a):
            cal=(i+1)*(j+1)
            list[i].append(cal)  #based on list[i] to put data into it
    return list


b=time(5)
print(b)