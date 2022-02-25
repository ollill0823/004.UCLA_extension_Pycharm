def output(n):
    for i in range(n,-1,-1):
        print(i, end=' ')
    print()
    if n>0:
        output(n - 1)


output(5)






