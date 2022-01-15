# Amusement Park height with function
def intocm(inches) :
    return inches * 2.54

def checkheight(inches) :  # 創造這個function的原因主要指是讓inches = hinches
    hcm = intocm(inches)
    if hcm >= 125:
        print('You are tall enough, enjoy your ride ! ')
    elif hcm >= 100:
        response = input('Would you like to sit in the resevered row ?  [Y/N] ')
        if response == 'Y':
            print('Right this way!')
        else:
            print('Sorry, please enjoy a different side. ')
    else:
        print('STOP! You should NOT pass ! ')
        print('You are not tall enough ! ')
hinches = eval(input('Enter your height in inches: '))
checkheight(hinches) #執行 checkheight 之後的 if/elif/else
