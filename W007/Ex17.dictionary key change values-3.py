def reverse(item):
    lst_v= list(item.values())
    lst_k= list(item.keys())
    str={}
    for i in range(len(phonebook)):
        str[lst_v[i]]=lst_k[i]
    return str



phonebook = {'Smith, Jane': '123-45-67', 'Doe John': '987-65-43', 'Baker David': '567-89-01'}
reverse(phonebook)
print(reverse(phonebook))






