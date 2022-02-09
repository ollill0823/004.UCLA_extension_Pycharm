def intoft(inches):
    feet= inches//12
    inch= inches%12
    foot = str(feet) + '\'' + str(inch) + '"'
    return foot

def kgtopound(kg):
    kground= round(2.204*kg,1)
    return kground

try:
    infile = input('Hello.\nPlease enter a roster file: ')
    openfile = open(infile, 'r')
except FileNotFoundError:
    infile = input('ERROR, FILE DOES NOT EXIST. Please enter a roster file: ')
    openfile = open(infile, 'r')

# read all the original CSV file
checkfile = openfile.readlines()
openfile.close()

# print this file to a new but editable file
secondopen=open('test.csv','w')
for b in checkfile:
    secondopen.write(b)


YesorNo = input('There are 13 names in this file. Would you like to enter additional names? (Y/N) ')


# judge from if requiring to enter new data
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
            sedentary=''
            moderate=''
            active=''
            for b in lifestyle:
                if b == '3':
                     active= 'x'
                elif b == '2':
                    moderate= 'x'
                elif b == '1':
                    sedentary = 'x'
                else:
                    infile = input('    Sorry, you can only key in 1, 2,3 only. Please enter lifestyle again: ')
            additem = firstname + ',' + lastname + ',' + age + ',' + occupation + ',' + height + ',' + weight + ',' + sedentary + ',' + moderate + ',' + active + '\n'
                # storage input data into defined a storage file
            secondopen.write(additem)
        secondopen.close()

         # open storage file then arrange the data and then storage the final file
        thirdopen = open('test.csv', 'rt')
        thirdopen.readline()
        thirdcheck = thirdopen.readlines()
        thirdopen.close()

        # Stoage the file to the defined file
        print('-------------------------')
        outfile = input('Save new roster file as: ')
        finaloutput = open(outfile, 'w')
        print('File saved!')

        # judge first, last, occupation column to check how many bllanks they need
        longestfirst = 0
        longestlast = 0
        longestocc = 0
        for item in thirdcheck:
            replace = item.replace('\n', ' ')
            checksplit = replace.split(',')

             # define how many blank firs, last, occupation need
            if len(checksplit[0]) > longestfirst and len(checksplit[0]) >= 9:
                longestfirst = len(checksplit[0])
            elif len(checksplit[0]) < longestfirst and len(checksplit[0]) >= 9:
                longestfirst = longestfirst
            elif len(checksplit[0]) < longestfirst and len(checksplit[0]) < 9:
                longestfirst = longestfirst
            else:
                longestfirst = 9

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

        header = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>5} {:>9} \n'.format('First', 'Last', 'Age',
                                                                                      'Occupation',
                                                                                      'Ht', 'Wt',
                                                                                      'lifestyle',
                                                                                      var1=longestfirst,
                                                                                      var2=longestlast,
                                                                                      var3=longestocc)
        finaloutput.write(header)

        lifestyle = ' '
        for item in thirdcheck:
            checkrowagain = item.replace('\n', ' ')
            checksplitagain = checkrowagain.split(',')
            if checksplitagain[6] == 'x':
                lifestyle = 'Sedentary'
            elif checksplitagain[7] == 'x':
                lifestyle = 'Moderate'
            else:
                lifestyle = 'Active'

            a = eval(checksplitagain[4])
            b = eval(checksplitagain[5])
            checkinfo = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>5} {:>9} \n'.format(checksplitagain[0],
                                                                                                 checksplitagain[1],
                                                                                                 checksplitagain[2],
                                                                                                 checksplitagain[3],
                                                                                                 intoft(a),
                                                                                                 kgtopound(b),
                                                                                                 lifestyle,
                                                                                                 var1=longestfirst,
                                                                                                 var2=longestlast,
                                                                                                 var3=longestocc)
            thirdopen.close()
            finaloutput.write(checkinfo)

    elif i == 'N':
        secondopen.close()
        fourthopen = open('test.csv', 'rt')
        fourthopen.readline()
        fourthcheck = fourthopen.readlines()
        fourthopen.close()

        print('-------------------------')
        outfile = input('Save new roster file as: ')
        finaloutput = open(outfile, 'w')
        print('File saved!')

        seclongestfirst = 0
        seclongestlast = 0
        seclongestocc = 0
        for item in fourthcheck:
            replace = item.replace('\n', ' ')
            checksplit = replace.split(',')

            if len(checksplit[0]) > seclongestfirst and len(checksplit[0]) >= 9:
                seclongestfirst = len(checksplit[0])
            elif len(checksplit[0]) < seclongestfirst and len(checksplit[0]) >= 9:
                seclongestfirst = seclongestfirst
            elif len(checksplit[0]) < seclongestfirst and len(checksplit[0]) < 9:
                seclongestfirst = seclongestfirst
            else:
                seclongestfirst = 9

            if len(checksplit[1]) > seclongestlast and len(checksplit[1]) >= 9:
                seclongestlast = len(checksplit[1])
            elif len(checksplit[1]) < seclongestlast and len(checksplit[1]) >= 9:
                seclongestlast = seclongestlast
            elif len(checksplit[1]) < seclongestlast and len(checksplit[1]) < 9:
                seclongestlast = seclongestlast
            else:
                seclongestlast = 9

            if len(checksplit[3]) > seclongestocc and len(checksplit[3]) >= 9:
                seclongestocc = len(checksplit[3])
            elif len(checksplit[3]) < seclongestocc and len(checksplit[3]) >= 9:
                seclongestocc = seclongestocc
            elif len(checksplit[3]) < seclongestocc and len(checksplit[3]) < 9:
                seclongestocc = seclongestocc
            else:
                seclongestocc = 9

        header = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>5} {:>9} \n'.format('First', 'Last', 'Age',
                                                                                      'Occupation',
                                                                                      'Ht', 'Wt',
                                                                                      'lifestyle',
                                                                                      var1=seclongestfirst,
                                                                                      var2=seclongestlast,
                                                                                      var3=seclongestocc)
        finaloutput.write(header)

        lifestyle = ' '

        for item in fourthcheck:
            checkrowagain = item.replace('\n', ' ')
            checksplitagain = checkrowagain.split(',')
            if checksplitagain[6] == 'x':
                lifestyle = 'Sedentary'
            elif checksplitagain[7] == 'x':
                lifestyle = 'Moderate'
            else:
                lifestyle = 'Active'

            a = eval(checksplitagain[4])
            b = eval(checksplitagain[5])
            checkinfo = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>5} {:>9} \n'.format(checksplitagain[0],
                                                                                             checksplitagain[1],
                                                                                             checksplitagain[2],
                                                                                             checksplitagain[3],
                                                                                             intoft(a),
                                                                                             kgtopound(b),
                                                                                             lifestyle,
                                                                                             var1=seclongestfirst,
                                                                                             var2=seclongestlast,
                                                                                             var3=seclongestocc)
            finaloutput.write(checkinfo)
    else:
        infile = input('Sorry, you should keyin Y/N.. Please enter only Y/N again: ')
