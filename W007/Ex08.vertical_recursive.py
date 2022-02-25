def vertical(n):
    if n<10:
        print(n)
    else:
        vertical(n//10)
        print(n%10)

vertical(3124)















