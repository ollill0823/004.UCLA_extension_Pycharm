#### Execution control , if statements  #####
## One way if: Height requirement
## Scenior: amusement park with 125 cm minimum height requirement to ride
hinches = eval(input('Enter your height in inches: '))
hcm = hinches * 2.54
if hcm < 125 :
    'the tider is shorter than 125'
    print ( 'STOP! You should NOT pass ! ')
    print ( 'You are not tall enough ! ' )
## Once you stop indenting, you are no longer in the if-statement
print ( 'Have a nice day ! ' )