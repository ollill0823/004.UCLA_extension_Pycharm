def even(x):
    print('2, 3, ',end='')
    for i in range(4,x+1):
        if i%2==0 or i%3==0:
            print(i, end=', ')
    print('\b\b')


even(17)
