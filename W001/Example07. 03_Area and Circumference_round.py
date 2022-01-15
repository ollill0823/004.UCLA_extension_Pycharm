## Task: Calculate the circumstance and area of a circle.
## import math
import math

def circumference (radius):
    circumference = 2 * math.pi * radius
    return circumference

def area (radius) :
    return math.pi * radius ** 2

def printdetails ( radius ) :
    c =  round (circumference( radius ), ndigits = 2) ## round(number, ndigits=None) number = 要印出的值, ndigits=小數點後幾位
    a = round ( area( radius ), ndigits =2)

    print (' ------------------------ ')
    print(' Radius = ', radius)
    print (' Circumference ', c )
    print (' Area = ', a )


printdetails (10)
printdetails (12)
printdetails (2.5)

