input=open('roster_small.csv','r')
input.readline()  #skip the title
roster=input.readlines()
input.close()

output = open('roster2.txt', 'w')
header = '{:<12} {:<12} {:^3} {:^5}\n'.format('First', 'Last', 'Age', 'Occupation')
output.write(header)


for person in roster:
    currentrow=person.replace('\n', ' ')
    personinfo=currentrow.split( ',' )
    personfmt = '{:<12} {:<12} {:^3} {:<5}\n'.format(personinfo[0], personinfo[1], personinfo[2], personinfo[3])
    output.write(personfmt)
output.close()


