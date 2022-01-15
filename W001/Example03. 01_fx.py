'''
Week1 Python Notes
Name: PPwang
Description: Examples of functions in Python
'''
def myfun(x):
    'Calculate the function f(x) = x^2 + 3x + 2'
    solution = x**2 + 3*x + 2
    return solution  ## use return when you expect the function to give a value back in return

print("f(x) = x^2 + 3x + 2")
print(myfun(5))      ## print 只會做對齊最左邊的, 沒對齊最左邊的print 需要強迫他跑他才會跑

def urfun(x):
    'Calculate the function f(x) = x^2 - 3x + 2'
    solution = x ** 2 - 3 * x + 2
    return solution
print("f(x) = x^2 - 3x + 2")
print(urfun(5)) ## print 可以放在最後也可以放在以定義的函數之後

def theirfun(x):
    solution = x ** 2 + 3 * x - 2
    return solution
print("f(x) = x^2 + 3x - 2")
print(theirfun(5))

var1 = myfun(5)
print('The function value is', var1)

help(myfun)