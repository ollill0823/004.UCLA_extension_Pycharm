asknum=True
while asknum:
    try:
        ask=int(input('Enter a positive number: '))
        if ask>0:
            asknum=False
    except ValueError:
        print('Please keyin an int.')
