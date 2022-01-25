def even(x):
    print('2, 3, ',end='')
    for i in range(4,17):
        if i%2==0:
            print(i, end=', ')
        elif i%3==0:
            print(i, end=', ')


even(17)
