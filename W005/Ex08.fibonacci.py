import math

# fiabonacci number = 1/0! + 1/1! + 1/2! + 1/3! + ......+ 1/n!

def approxE(error):
    x=1   # fiabonacci first number e0= 1/0!
    y=2  # fiabonacci first number e1= 1/0! + 1/1!
    i=2 # start from i=2
    while y-x>error:
        x=y
        y=x+ 1/math.factorial(i)
        i +=1
    return y

a=approxE(0.000000001)
print(a)