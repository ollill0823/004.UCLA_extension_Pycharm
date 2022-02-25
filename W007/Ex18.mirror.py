def mirror(word):
    array = ''
    for j in word:
        if j =='b':
            array +='d'
        elif j =='d':
            array +='b'
        else:
            array += j
    change = ''
    for i in range(len(array)):
        if array[i] in 'bdimnotuvwx':
            change += array[-1-i]
        else:
            change = 'INVALID'
            break
    return change



b='bed'
a=mirror(b)
print(a)






