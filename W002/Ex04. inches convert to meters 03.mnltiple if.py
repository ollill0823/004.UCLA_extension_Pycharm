## More if: Height requirement
## Scenior: amusement park with 125 cm minimum height requirement to ride
##               reserved seat if they are between 110 and 125
# Stop the rider if they are not tall enough
# Offer a reserved seat if they are between 110 and 125
# Allow the rider on otherwise
hinches = eval(input('Enter your height in inches: '))
hcm = hinches * 2.54
if hcm < 110 :
    # the tider is shorter than 125'
    print ( 'STOP! You should NOT pass ! ')
    print ( 'You are not tall enough ! ' )
elif  hcm < 125 : # elif is used at the second condition, but not include the first condition (ex.: hcm>110;)
    print ( 'Would you like to sit in reserved row ? ' )
else :   # if heigh(cm) higher than 125 cm
    print ( 'You are tall enough, enjoy your ride ! ' )