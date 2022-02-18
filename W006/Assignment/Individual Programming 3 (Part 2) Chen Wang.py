# Open defined file
filename = input ('Please enter a file name: ')
openfile = open (filename)

# Get rid of the first column
title = openfile.readline()  # # get rid of the first column
content = openfile.readlines()  # read all the information and use it to modify
openfile.close() # close unused file to save memory

#  list  --> str --> dictionary
dict= {}
for item in content:
    for detail in item:
        contentsplit = item.replace ('\t','-')
        #  replace \t to - (use - instead of ',' because information has already had ',' if we use ',', information will be error)
        contentsplit = contentsplit.replace ('\n','') # remove \n
        detail = contentsplit.split ('-') # str -->list
        # list-->dictionary
        for i in detail:
            dict[detail[0]] = detail[1]
    dict.update (dict)

print ('There are 10 terms in this vocabulary list.')

# Ask user if need to keyin more term
YesorNoCheck=True
while YesorNoCheck:  # check if the user wants to keyin data
    YesorNo = input('Would you like to add more terms (Y/N)? ')
    if YesorNo == 'Y' or YesorNo == 'y': # the user wants to keyin data
        badnum = True
        # Check until the user enter qualified answer
        while badnum:
            try:
                numadd = int(input('How many would you like to add? '))
                if numadd > 0:
                    badnum = False
                elif numadd == 0:
                    break
                else:
                    print('Error. Please enter a positive number.')
            except ValueError:
                print('Error. Please enter an integer.')

        # Double check the item the user keyin (if the user repudicates the term)
        # Enter the new item into the existed dictionary
        for i in range(numadd):  # keyin information
            keyinfo = input('Term #{}: '.format(i + 1))  # keyin keys
            for item in dict:
                if keyinfo == item:  # check if user keyin the repeated key, ask user to double check)
                    checkifno = input('Warning! This term is already in the vocabulary list. Update definition (Y/N)? ')
                    if checkifno == 'Y' or checkifno == 'y':
                        pass
                    else:
                        break
                valuesadd = input('Definition #{}: '.format(i + 1))  # keyin values
                ArrangeToDict = {keyinfo: valuesadd}  # change to dictionary type
                dict.update(ArrangeToDict)
                break
    elif YesorNo == 'N' or YesorNo == 'n':  # the user does not want to keyin data
        print('OK. Let\'us save the data to the file.')
        break
    else:  # the user does not keyin Y/N, request the user to keyin again
        print('Type error. Please enter Y/N again: ')


count = len(dict)
print ('There are {} terms in the new vocabulary list.'.format(count))

# Print the overall information on the bullentin board
print('')
for j in dict:
    print ('{} - {}'.format(j,dict[j]))

# Created a defined file
print ('')
filename = input ('What would you like to save the file as? ')
outfile = open (filename, 'w')

# Alignment key and save information into file
key=dict.keys()
keycount=0  # spaces in term row
print(key)

# calculate how many spaces should the term row have
for i in key:
    if len(i)>keycount:
        keycount=len(i)

outfile.write ('{:<{var1}}  {}\n'.format( 'term', 'definition', var1 = keycount))

# Print all the inforamtion in the dictionary to the file
for k in dict:
    outfile.write ('{:<{var1}}  {}\n'.format( k, dict[k], var1 = keycount))