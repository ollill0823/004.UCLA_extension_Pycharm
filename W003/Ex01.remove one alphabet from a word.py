a=input('Enter word: ')
b=eval(input("Enter n: "))


def f(str,n):
    front = str[:n]
    back = str[n+1:]
    return front + back

z=f(a,b)
print(z)