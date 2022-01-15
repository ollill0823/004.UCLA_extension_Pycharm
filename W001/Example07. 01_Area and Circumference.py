## Task: Calculate the circumstance and area of a circle.
## import math
import math

def circumference (radius):
    circumference = 2 * math.pi * radius
    return circumference

def area (radius) :
    return math.pi * radius ** 2

r = 10
c = circumference ( r ) ##當他定義函數的時後,他就會套值進去
## Because line 13  c = circumference ( r ) & line 5 circumference (radius) looks similar, python will define r=radius
a = area ( r )
## Because line 15  a = area ( r ) & line 9 area (radius) looks similar, python will define r=radius

print ('radius = ', r )
print ('circumference = ', c )
print (' area = ', a )

