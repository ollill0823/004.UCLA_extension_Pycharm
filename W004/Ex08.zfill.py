weekday='Sunday'
month = 'September'
day=11
year=2022
hour = 8
minute = 3
second = 7

print( str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2) )
print('--------------------------')
datefmt= '{}  {} {} {}  {}:{}:{}'.format(weekday, month, day, year, hour, minute, second)
print('--------------------------')

print(datefmt)

datefmt= '{} {} {} {}  {}:{}:{}'.format(weekday, month, day, year, str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
print(datefmt)
print('--------------------------')
datefmt= '{3}, {2}, {1}, {0} at {4}:{5}:{6}'.format(weekday, month, day, year, str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
print(datefmt)
print('--------------------------')

roster= [ [ 'Anna', 'Barbara', '35', 'nurse' ],
               [ 'Catherine', 'Do', '45', 'physicist' ],
               [ 'Eric', 'Fredrick', '28', 'teacher' ],
               [ 'Gabriel', 'Hernandez', '55', 'surgeon' ],
               [ 'Ivy', 'Joo', '31', 'engineer' ],
               [ 'Kelly', 'Marks', '21', 'student' ]]


for i in roster:
    overall = '{1}, {0} is a {2}-year-old {3}'.format(i[0], i[1], i[2], i[3])
    print(overall)
print('--------------------------')

for person in roster:
    formattestext =  '{:>12} {:>12}{:>3}{:>12}' .format ( person[0], person[1], person[2], person[3])
    print(formattestext)





