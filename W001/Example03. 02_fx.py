def myfun(x):
    solution = x**2 + 3*x + 2
    return solution
    solution = 2*solution  ##  this line is ignored because the last return solution
    return solution  ##  this line is ignored because the last return solution

print(myfun(5))  ## will finish the first return solution, Ans = 42

def myfun(x):
    solution = x**2 + 3*x + 2
    solution = 2*solution
    return solution

print(myfun(5))  ##  Ans = 84