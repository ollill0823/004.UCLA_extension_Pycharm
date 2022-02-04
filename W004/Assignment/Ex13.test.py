def file(filename):
    output = open(filename, 'r')
    output.read()


infile = input('Hello.\nPlease enter a roster file: ')
YesorNo=input('There are 13 names in this file. Would you like to enter additional names? (Y/N)')

for i in YesorNo:
    if i == 'Y':
        n=eval(input('How many more names? '))

for a in range(n):
    print('----- Person '+ str(a+1) + ' -----')
    firstname=input('First name: ')
    lastname=input('Last Name: ')
    age=input('Age: ')
    occupation= input('Occupation: ')
    height= input('Height (in inches): ')
    weight = input('Height (in pounds): ')
    lifestyle = eval(input ('Lifestyle (1-sedentary, 2-moderate, 3-active): '))
    sedentary=' '
    moderate= ' '
    active= ' '
    for b in lifestyle:
        if b ==3:
            active='x'
        elif b==2:
            moderate='x'
        else:
            sedentary='x'

file(infile)