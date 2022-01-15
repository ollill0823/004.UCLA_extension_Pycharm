# reserved from the highest level
hinches = eval(input('Enter your height in inches: '))
hcm = hinches * 2.54
if hcm >= 125 :
    print('You are tall enough, enjoy your ride ! ')
elif hcm >= 110 : # 若只有if hcm >=110 會變成 確認完>125 以後,繼續確認這個
    print('Would you like to sit in reserved row ? ')
else :
    print('STOP! You should NOT pass ! ')
    print('You are not tall enough ! ')

print ( 'Have a nice day ! ' )
