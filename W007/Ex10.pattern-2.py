def pattern(n):
    if n>0:
        pattern(n-1)
        print('*'*n)
        pattern(n-1)

pattern(4)













