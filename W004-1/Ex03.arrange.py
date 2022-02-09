<<<<<<< HEAD
def growthrates(n):
    print(' i     i**2   i**3   2**i')
    formatStr= '{0:2d} {1:6d} {2:6d} {3:6d}'
    for i in range (2, n+1):
        print(formatStr.format(i,  i**2,  i**3,  2**i))

a=growthrates(12)
=======
print ('  i   i**2   i**3   2**i')
for i in range(1,13):
    print('{0:2}   {1:4}  {2:7}  {3:7}'.format(i, i**2, i**3, 2**i, sep='            '))
>>>>>>> origin/main
