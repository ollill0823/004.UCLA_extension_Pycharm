# More if practice
hinches = eval(input('Enter your height in inches: '))
hcm = hinches * 2.54
if hcm >= 125 :
    print('You are tall enough, enjoy your ride ! ')
elif hcm >= 110 :  # elif can be unlimited, but have to follow the order
    print('Row 1 ')
elif hcm >= 100 :
    print('Row 2 ')
elif hcm >= 90 :
    print('Row 3 ')
elif hcm >= 80 :
    print('Row 4 ')
else :
    print('STOP! You should NOT pass ! ')
    print('You are not tall enough ! ')

print ( 'Have a nice day ! ' )