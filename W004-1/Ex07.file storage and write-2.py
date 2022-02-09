
import time

number= eval(input('How many joke do you have? '))

output= open('gogopower.txt', 'w')

for i in range (number):
    joke= input ('Telle me your ' + str(i+1) +' joke: ')
    joket= time.strftime('%a. %m/%d/%y %H:%M:%S %Z', time.localtime())
    ans= input ('I don\' know. What is the answer? ')
    anst = time.strftime('%a. %m/%d/%y %H:%M:%S %Z', time.localtime())
    output.write('[' + joket+ '] Q: '+ joke + '\n')
    output.write('[' + anst+ '] A: ' + ans + '\n')

output.close()
