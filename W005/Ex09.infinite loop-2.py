def hello2():
    name = input('What is your name? ')
    while name != 'ppwang':
        name=input('What is your name? ')
        print('Hello {}'.format(name))

hello2()