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