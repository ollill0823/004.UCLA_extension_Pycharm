def reverse(item):
    str={}
    for i, j  in item.items():
        str.update({j:i})
    return str



phonebook = {'Smith, Jane': '123-45-67', 'Doe John': '987-65-43', 'Baker David': '567-89-01'}
reverse(phonebook)
print(reverse(phonebook))






