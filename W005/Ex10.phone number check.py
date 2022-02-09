rphonebook={
        '(123)456-78-90':['Anna', 'Karenina'],
        '(901)234-56-78':['Yu', 'Tsun'],
        '(321)908-76-54':['Hans','Castorp']
    }

def rlookup(phonebook):
    while True:
        number = input('Enter phone number in the format (xxx)xxx-xx-xx: ')
        if number in phonebook:
            print(phonebook[number])
        else:
            print('The number you entered is not in use.')

a=rlookup(rphonebook)
print(a)