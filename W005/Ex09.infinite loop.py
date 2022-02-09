def cities():
    lst=[]

    city= input('Enter city: ')

    while city != ' ':
        lst.append(city)
        city= input('Enter city: ')
    return lst


print(cities())
