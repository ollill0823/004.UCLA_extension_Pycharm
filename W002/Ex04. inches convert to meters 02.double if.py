## Two-way if: Height requirement
## Scenior: amusement park with 125 cm minimum height requirement to ride
# Stop the rider if they are not tall enough
# Allow the rider on otherwise
hinches = eval(input('Enter your height in inches: '))
hcm = hinches * 2.54
if hcm < 125 :
    # the tider is shorter than 125'
    print ( 'STOP! You should NOT pass ! ')
    print ( 'You are not tall enough ! ' )
else :   # if heigh(cm) higher than 125 cm
    print ( 'You are tall enough, enjoy your ride ! ' )
print ( 'Have a nice day ! ' )