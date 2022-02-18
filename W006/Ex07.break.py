def guessname():
    name= input('Guess a programming language: ')
    while name !='python':
        if name == 'Quit':
            break
        name=input('Error. Guess a programming language again: ')
    if name =='python':
        print('you got it!')
    else:
        print('So great')

guessname()