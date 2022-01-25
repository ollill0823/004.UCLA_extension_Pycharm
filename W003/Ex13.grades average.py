grade=eval(input('give grades: '))

def f(x):
    sum = 0
    for i in range(0,len(x)):
        sum=sum+x[i]
    return sum/len(x)

z=f(grade)
print(z)
