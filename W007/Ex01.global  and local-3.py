def h(n):
    print('Start h')
    print('h(n): 1/n', 1/n)
    print('h(n): n', n)

def g(n):
    print('Start g')
    try:
        h(n - 1)
        print('g(n): 1/n', 1 / n)
        print('g(n): n', n)
    except:
        print('Caught')

def f(n):
    print('Start f')
    g(n-1)
    print('f(n): 1/n', 1/n)
    print('f(n): n', n)

f(2)

