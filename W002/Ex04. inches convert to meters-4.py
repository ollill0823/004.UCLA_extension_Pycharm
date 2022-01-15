# elif-if practice
hinches = eval(input('Enter your height in inches: '))
hcm = hinches * 2.54
if hcm >= 125 :
    print('You are tall enough, enjoy your ride ! ')
elif hcm >= 100 :
    response = input ( 'Would you like to sit in the resevered row ?  [Y/N] ')
    if response == 'Y' : # 字元 'Y' 不等於 ' Y ' (中間有空白)
        print ( 'Right this way!' )
    else :
        print('Sorry, please enjoy a different side. ')
else :
    print('STOP! You should NOT pass ! ')
    print('You are not tall enough ! ')