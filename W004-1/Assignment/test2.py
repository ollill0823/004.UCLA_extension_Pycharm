def intoft(inches):
    feet= inches//12
    inch= inches%12
    foot = str(feet) + '\'' + str(inch) + '"'
    return foot

try:
    infile = input('Hello.\nPlease enter a roster file: ')
    openfile = open(infile, 'r')
except FileNotFoundError:
    infile = input('ERROR, FILE DOES NOT EXIST. Please enter a roster file: ')
    openfile = open(infile, 'r')


checkfile = openfile.readlines()
openfile.close()

secondopen=open('test.csv','w')
for b in checkfile:
    secondopen.write(b)
secondopen.close()

YesorNo = input('There are 13 names in this file. Would you like to enter additional names? (Y/N) ')

for i in YesorNo:

    if i == 'N':
        fourthopen = open('test.csv', 'rt')
        fourthopen.readline()
        fourthcheck = fourthopen.readlines()
        fourthopen.close()
        print(fourthcheck)

        print('-------------------------')
        outfile = input('Save new roster file as: ')
        outcheckfile = open(outfile, 'w')
        print('File saved!')

        seclongestfirst = 0
        seclongestlast = 0
        seclongestocc = 0
        for item in fourthcheck:
            checkrow = item.replace('\n', ' ')
            checksplit = checkrow.split(',')

            if len(checksplit[0]) > seclongestfirst and len(checksplit[0]) >= 9:
                seclongestfirst = len(checksplit[0])
            elif len(checksplit[0]) < seclongestfirst and len(checksplit[0]) >= 9:
                seclongestfirst = seclongestfirst
            elif len(checksplit[0]) < seclongestfirst and len(checksplit[0]) < 9:
                seclongestfirst = seclongestfirst
            else:
                seclongestlast = 9

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

        header = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format('First', 'Last', 'Age',
                                                                                      'Occupation',
                                                                                      'Ht', 'Wt',
                                                                                      'lifestyle',
                                                                                      var1=seclongestfirst,
                                                                                      var2=seclongestlast,
                                                                                      var3=seclongestocc)
        outcheckfile.write(header)

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
            checkinfo = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>5} {:>3} {:>9} \n'.format(checksplitagain[0],
                                                                                             checksplitagain[1],
                                                                                             checksplitagain[2],
                                                                                             checksplitagain[3],
                                                                                             intoft(a),
                                                                                             checksplitagain[5],
                                                                                             lifestyle,
                                                                                             var1=seclongestfirst,
                                                                                             var2=seclongestlast,
                                                                                             var3=seclongestocc)
            outcheckfile.write(checkinfo)

