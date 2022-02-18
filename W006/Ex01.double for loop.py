def factorial(n):
    for i in range(1,n+1):
        currentum=1
        for j in range(2, i+1):
            currentum=currentum*j
        print(currentum)

factorial(4)