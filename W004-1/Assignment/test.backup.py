def intoft(inches):
    feet= inches//12
    inch= inches%12
    foot = str(feet) + '\'' + str(inch) + '"'
    return foot

try:
    infile = input('Hello.\nPlease enter a roster file: ')
    openfile = open(infile, 'r')
    openfile.readline()
    checkfile = openfile.readlines()
    openfile.close()

    longestfirst = 0
    longestlast = 0
    longestocc = 10
    for item in checkfile:
        checkrow = item.replace('\n', ' ')
        checksplit = checkrow.split(',')

        if len(checksplit[0]) > longestfirst and len(checksplit[0]) >= 9:
            longestfirst = len(checksplit[0])
        elif len(checksplit[0]) < longestfirst and len(checksplit[0]) >= 9:
            longestfirst = longestfirst
        elif len(checksplit[0]) < longestfirst and len(checksplit[0]) < 9:
            longestfirst = longestfirst
        else:
            longestlast = 9

        if len(checksplit[1]) > longestlast and len(checksplit[1]) >= 9:
            longestlast = len(checksplit[1])
        elif len(checksplit[1]) < longestlast and len(checksplit[1]) >= 9:
            longestlast = longestlast
        elif len(checksplit[1]) < longestlast and len(checksplit[1]) < 9:
            longestlast = longestlast
        else:
            longestlast = 9

        if len(checksplit[3]) > longestocc and len(checksplit[3]) >= 9:
            longestocc = len(checksplit[3])
        elif len(checksplit[3]) < longestocc and len(checksplit[3]) >= 9:
            longestocc = longestocc
        elif len(checksplit[3]) < longestocc and len(checksplit[3]) < 9:
            longestocc = longestocc
        else:
            longestocc = 9

    output = open('test.txt', 'w')
    header = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format('First', 'Last', 'Age', 'Occupation',
                                                                                  'Ht', 'Wt', 'Lifestyle',
                                                                                  var1=longestfirst, var2=longestlast,
                                                                                  var3=longestocc)
    output.write(header)

    for item in checkfile:
        checkrow = item.replace('\n', ' ')
        checksplit = checkrow.split(',')
        lifestyle = ' '
        if checksplit[6] == 'x':
            lifestyle = 'Sedentary'
        elif checksplit[7] == 'x':
            lifestyle = 'Moderate'
        else:
            lifestyle = 'Active'
        a=eval(checksplit[4])
        checkinfo = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format(checksplit[0], checksplit[1],
                                                                                         checksplit[2], checksplit[3],
                                                                                         intoft(a),
                                                                                         checksplit[5], lifestyle,
                                                                                         var1=longestfirst,
                                                                                         var2=longestlast,
                                                                                         var3=longestocc)
        output.write(checkinfo)

    YesorNo = input('There are 13 names in this file. Would you like to enter additional names? (Y/N) ')

    for i in YesorNo:
        if i == 'Y':
            n = eval(input('How many more names? '))
            for a in range(n):
                print('----- Person ' + str(a + 1) + ' -----')
                firstname = input('First name: ')
                lastname = input('Last Name: ')
                age = input('Age: ')
                occupation = input('Occupation: ')
                height = input('Height (in inches): ')
                weight = input('Weight (in pounds): ')
                lifestyle = input('Lifestyle (1-sedentary, 2-moderate, 3-active): ')
                for b in lifestyle:
                    if b == '3':
                        lifestyle = 'Active'
                    elif b == '2':
                        lifestyle = 'Moderate'
                    else:
                        lifestyle = 'Sedentary'
                    a = eval(checksplit[4])
                    additem = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format(firstname, lastname,
                                                                                                   age, occupation, intoft(a), weight, lifestyle, var1=longestfirst, var2=longestlast,
                                                                                  var3=longestocc)
                output.write(additem)

    output.close()
    print('-------------------------')

    reopenfile = open('test.txt', 'r')
    recheckfile = reopenfile.readlines()
    reopenfile.close()

    outfile = input('Save new roster file as: ')
    outcheckfile = open(outfile, 'w')
    for i in recheckfile:
        outcheckfile.write(i)
    print('File saved!')

except FileNotFoundError:
    infile = input('ERROR, FILE DOES NOT EXIST. Please enter a roster file: ')
    openfile = open(infile, 'r')
    openfile.readline()
    checkfile = openfile.readlines()
    openfile.close()

    longestfirst = 0
    longestlast = 0
    longestocc = 10
    for item in checkfile:
        checkrow = item.replace('\n', ' ')
        checksplit = checkrow.split(',')

        if len(checksplit[0]) > longestfirst and len(checksplit[0]) >= 9:
            longestfirst = len(checksplit[0])
        elif len(checksplit[0]) < longestfirst and len(checksplit[0]) >= 9:
            longestfirst = longestfirst
        elif len(checksplit[0]) < longestfirst and len(checksplit[0]) < 9:
            longestfirst = longestfirst
        else:
            longestlast = 9

        if len(checksplit[1]) > longestlast and len(checksplit[1]) >= 9:
            longestlast = len(checksplit[1])
        elif len(checksplit[1]) < longestlast and len(checksplit[1]) >= 9:
            longestlast = longestlast
        elif len(checksplit[1]) < longestlast and len(checksplit[1]) < 9:
            longestlast = longestlast
        else:
            longestlast = 9

        if len(checksplit[3]) > longestocc and len(checksplit[3]) >= 9:
            longestocc = len(checksplit[3])
        elif len(checksplit[3]) < longestocc and len(checksplit[3]) >= 9:
            longestocc = longestocc
        elif len(checksplit[3]) < longestocc and len(checksplit[3]) < 9:
            longestocc = longestocc
        else:
            longestocc = 9

    output = open('test.txt', 'w')
    header = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format('First', 'Last', 'Age', 'Occupation',
                                                                                  'Height', 'Weight', 'lifestyle', var1=longestfirst, var2=longestlast,
                                                                                  var3=longestocc)
    output.write(header)

    for item in checkfile:
        checkrow = item.replace('\n', ' ')
        checksplit = checkrow.split(',')
        lifestyle = ' '
        if checksplit[6] == 'x':
            lifestyle = 'Sedentary'
        elif checksplit[7] == 'x':
            lifestyle = 'Moderate'
        else:
            lifestyle = 'Active'
        a = eval(checksplit[4])
        checkinfo = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format(checksplit[0], checksplit[1],
                                                                                         checksplit[2], checksplit[3], intoft(a),
                                                                                         checksplit[5], lifestyle, var1=longestfirst, var2=longestlast,
                                                                                  var3=longestocc)
        output.write(checkinfo)

    YesorNo = input('There are 13 names in this file. Would you like to enter additional names? (Y/N) ')

    for i in YesorNo:
        if i == 'Y':
            n = eval(input('How many more names? '))
            for a in range(n):
                print('----- Person ' + str(a + 1) + ' -----')
                firstname = input('First name: ')
                lastname = input('Last Name: ')
                age = input('Age: ')
                occupation = input('Occupation: ')
                height = input('Height (in inches): ')
                weight = input('Weight (in pounds): ')
                lifestyle = input('Lifestyle (1-sedentary, 2-moderate, 3-active): ')
                for b in lifestyle:
                    if b == '3':
                        lifestyle = 'Sedentary'
                    elif b == '2':
                        lifestyle = 'Moderate'
                    else:
                        lifestyle = 'Active'
                    a = eval(checksplit[4])
                    additem = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format(firstname, lastname,
                                                                                                   age, occupation, intoft(a), weight, lifestyle, var1=longestfirst, var2=longestlast,
                                                                                  var3=longestocc)
                output.write(additem)

    output.close()
    print('-------------------------')

    reopenfile = open('test.txt', 'r')
    recheckfile = reopenfile.readlines()
    reopenfile.close()

    outfile = input('Save new roster file as: ')
    outcheckfile = open(outfile, 'w')
    for i in recheckfile:
        outcheckfile.write(i)
    print('File saved!')
