def complete(abbreviation):
       day={'Mo': 'Monday', 'We': 'Wednesday', 'Th': 'Thursday', 'Sa': 'Saturday', 'Fr': 'Friday'}
       return day[abbreviation]



a=complete('Th')
print(a)
