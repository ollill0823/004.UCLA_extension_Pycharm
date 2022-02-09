def bubbleSort(n):
    for j in range(len(n)):
        for i in range(len(n)-j-1):
            if n[i+1]<n[i]:
                n[i+1], n[i] = n[i], n[i+1]
    return n

lst=[3,1,7,4,9,2,5]
a=bubbleSort(lst)
print(a)

