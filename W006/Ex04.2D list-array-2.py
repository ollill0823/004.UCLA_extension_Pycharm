def time(a):
    list = []
    for i in range(a):
        list.append([])    ## define list number at first
        for j in range(a):
            cal=(i+1)*(j+1)
            list[i].append(cal)  #based on list[i] to put data into it
    return list


b=time(12)
print(b)

for c in b:
    row= ''
    for d in c:
        array='{:4}'.format(d)
        row=row+array
    print(row)