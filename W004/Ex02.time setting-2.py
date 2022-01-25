first = 'John'
last = 'Doe'
street = 'Main street'
number = 123
city = 'AnyCity'
state = 'AS'
zipcode = '09876'

a='{0} {1}\n{2} {3} \n{4}, {5} {6}'.format( first, last, number, street, city, state, zipcode)
print(a)