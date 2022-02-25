def different(t):

    output=set()
    for i in t:
        for j in i:
            output.add(j)
    return len(output)

t=[[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
a=different(t)
print(a)





