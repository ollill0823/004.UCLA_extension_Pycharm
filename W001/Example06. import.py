############ import ############
import math

a = math.sqrt(25)  ## 開根號25
b = math.ceil(4.3)  ## number rounded up 無條件進位

print ( a, ' ' , b )
print(math.pi)

import math as m
a = m.sqrt(64)  ## 開根號25
b = m.ceil(8.8)  ## number rounded up 無條件進位

print ( a, ' ' , b )
print(m.pi)

import fractions   ##分數
num1 = fractions.Fraction( 3, 4 )
print( num1)
print( num1 == 0.75)
print( num1 > 1 )
print( type ( num1 ))
print( math.floor( num1 ))   ## number rounded down
print( 3 // 4 ) ## division rounded down

## changing or checking working directory
import os   ## please don't change directory in your programming assignments.
os.chdir (_______________)
os.getcwd ()


## help(math)