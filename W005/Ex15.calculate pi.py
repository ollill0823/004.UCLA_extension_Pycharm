import random

def approxPi(n):
    num=0

    for i in range(n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        r=(x**2+y**2)**0.5

        if r<=1:
            num +=1
    return num*4/n

input=eval(input('Enter a number: '))
a=approxPi(input)
print(a)
