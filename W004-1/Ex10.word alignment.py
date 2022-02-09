def intofeet(inches):
    feet= inches//12
    inch= inches%12
    return str(feet) + '\'' + str(inch) + '"'

def kgtopound(kg):
    pound=round ( kg*2.24062,1)
    return str(pound)


roster= [ [ 'Anna', 'Barbara', 35, 60, 58.5 ],
               [ 'Catherine', 'Do', 45, 65, 61.5 ],
               [ 'Eric', 'Fredrick', 28, 65, 63.5 ],
               [ 'Gabriel', 'Hernandez', 55, 70, 68 ],
               [ 'Ivy', 'Joo', 31, 55, 57 ],
               [ 'Kelly', 'Marks', 21, 75, 60]]

longestfirst= 5 ## 隨便數字都可以
longestlast= 5 ## 隨便數字都可以

for i in roster:
    if len(i[0])>longestfirst:
        longestfirst=len(i[0])
    if len(i[1])>longestlast:
        longestlast=len(i[1])


output=open('roster1.txt', 'w')
header = '{:<{var1}} {:<{var2}} {:^3} {:^5} {:^5}\n'. format ('First', 'Last', 'Age', 'Mt', 'Wt', var1= longestfirst, var2 = longestlast)
output.write(header)


for i in roster:
    personfmt = '{:<{var1}} {:<{var2}} {:<3} {:<5} {:<5}\n'. format (i[0], i[1], i[2], intofeet(i[3]), kgtopound(i[4]), var1= longestfirst, var2 = longestlast)
    output.write(personfmt)
output.close()