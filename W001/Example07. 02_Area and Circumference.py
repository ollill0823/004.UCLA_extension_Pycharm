## Task: Calculate the circumstance and area of a circle.
## import math
import math

def circumference (radius):
    circumference = 2 * math.pi * radius
    return circumference

def area (radius) :
    return math.pi * radius ** 2

def printdetails ( radius ) :
    c = circumference( radius )
    a = area( radius )

    print (' ------------------------ ')
    print(' Radius = ', radius)
    print (' Circumference ', c )
    print (' Area = ', a )


printdetails (10)
printdetails (12)
printdetails (2.5)

