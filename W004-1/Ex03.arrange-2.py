<<<<<<< HEAD
students=[]
students.append(['DeMoines','Jim', 'Sophomore',3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River','Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])


def roster(students):
    print ('   Last       First           Class      Average Grade')
    for i in students:
        print('{:10}{:10}{:10}{:8.2f}'.format(i[0], i[1], i[2], i[3]))

roster(students)
=======
def growthrates(n):
    print(' i     i**2   i**3   2**i')
    formatStr= '{0:2d} {1:6d} {2:6d} {3:6d}'
    for i in range (2, n+1):
        print(formatStr.format(i,  i**2,  i**3,  2**i))

a=growthrates(12)
>>>>>>> origin/main
