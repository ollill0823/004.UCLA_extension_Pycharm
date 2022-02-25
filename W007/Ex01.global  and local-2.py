def h(n):
    print('Start h')
    try:
        print('h(n): 1/n', 1 / n)
    except:
        print('Caught')
    print('h(n): n', n)

def g(n):
    print('Start g')
    h(n-1)
    print('g(n): 1/n', 1/n)
    print('g(n): n', n)

def f(n):
    print('Start f')
    g(n-1)
    print('f(n): 1/n', 1/n)
    print('f(n): n', n)

f(2)
