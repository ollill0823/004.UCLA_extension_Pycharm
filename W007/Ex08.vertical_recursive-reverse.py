def vertical(n):
    if n<10:
        print(n)
    else:
        print(n % 10)
        vertical(n//10)


vertical(3124)















