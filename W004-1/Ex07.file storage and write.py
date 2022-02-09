
import time

number= eval(input('How many joke do you have? '))

output= open('gogopower.txt', 'w')

for i in range (number):
    joke= input ('Telle me your ' + str(i+1) +' joke: ')
    ans= input ('I don\' know. What is the answer? ')
    output.write('Q: '+ joke + '\n')
    output.write('Q: ' + ans + '\n')

output.close()

gogopoweread=open('gogopower.txt', 'r')
infile=gogopoweread.readlines()
gogopoweread.close()




qfile=open('gogopower2.txt', 'w')

number=1
for i in infile:
    if i[:2] =='Q:':
       qfile.write(str(number) +':' + i[3:])
    elif i[:2]  =='A:':
        qfile.write(str(number) +':' + i[3:])
        number=number+1

qfile.close()


