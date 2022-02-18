'''
File Name: module3.py
Agenda
1. Individual Programming 2 (borderline grades - dropping the lowest individual programming score -- by week)
2. Nested for loops
3. 2D lists
4. While loops
5. break, pass, continue
6. Dictionaries
7. Sets
8. Random module
'''

import random



########## Individual Programming 2 ##########
"""
def intoft(inches):
    inches = int(inches)
    feet = inches//12
    remainder = inches % 12
    return str(feet) + "'" + str(remainder) + '"'

try:
    filename = input("What is the file name? ")
    infile = open(filename)
except IOError:
    filename = input("Invalid file. What is the file name? ")
    infile = open(filename)

infile.readline()       ## skip over the first header line
content = infile.readlines()
infile.close()

## Generating separate lists of person info
firstlist = []
lastlist = []
agelist = []
occlist = []
htlist = []
wtlist = []
sedentarylist =[]
moderatelist = []
activelist =[]

## Storing existing person info in separate lists
for person in content:
    person = person.replace('\n','')
    detail = person.split(',')
    firstlist.append(detail[0])
    lastlist.append(detail[1])
    agelist.append(detail[2])
    occlist.append(detail[3])
    htlist.append(detail[4])
    wtlist.append(detail[5])
    sedentarylist.append(detail[6])
    moderatelist.append(detail[7])
    activelist.append(detail[8])

## Ask for additional person info (if any)
addmore = input('Is there anyone else you would like to add? (Y/N) ')
if addmore == 'Y' or addmore == 'y':
    numadd = int(input('How many? '))
    for i in range(numadd):
        print('----- Person', i+1, '-----')
        first = input('First name: ')
        last = input('Last name: ')
        age = input("Age: ")
        occ = input("Occupation: ")
        ht = input("Height: ")
        wt = input("Weight: ")
        activity = input("Activity level (1-sedentary, 2-moderate, 3-active): ")

        ## Before exiting the loop, we need to save this person's info into our lists
        firstlist.append(first)
        lastlist.append(last)
        agelist.append(age)
        occlist.append(occ)
        htlist.append(ht)
        wtlist.append(wt)

        ## Address different activity levels in lists
        if activity == '1':
            sedentarylist.append('x')
            moderatelist.append('')
            activelist.append('')
        elif activity == '2':
            sedentarylist.append('')
            moderatelist.append('x')
            activelist.append('')
        elif activity == '3':
            sedentarylist.append('')
            moderatelist.append('')
            activelist.append('x')
        else:
            sedentarylist.append('')
            moderatelist.append('')
            activelist.append('')

## obtaining new file name for output file
filename = input('What is the output file? ')
outfile = open(filename, 'w')

## header row
outfile.write('{:12} {:12} {:3} {:12} {:5} {:5} {:10}\n'.format('first', 'last', 'age', 'occupation', 'ht', 'wt', 'activity'))

## write individual info
for i in range(len(firstlist)):
    if sedentarylist[i] == 'x':
        outfile.write('{:12} {:12} {:3} {:12} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'sedentary'))
    elif moderatelist[i] == 'x':
        outfile.write('{:12} {:12} {:3} {:12} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'moderate'))
    elif activelist[i] == 'x':
        outfile.write('{:12} {:12} {:3} {:12} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'active'))
    else:
        outfile.write('{:12} {:12} {:3} {:12} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'N/A'))

outfile.close()

"""


"""
def intoft(inches):
    inches = int(inches)
    feet = inches//12
    remainder = inches % 12
    return str(feet) + "'" + str(remainder) + '"'

try:
    filename = input("What is the file name? ")
    infile = open(filename)
except IOError:
    filename = input("Invalid file. What is the file name? ")
    infile = open(filename)

infile.readline()       ## skip over the first header line
content = infile.readlines()
infile.close()

## Generating separate lists of person info
firstlist = []
lastlist = []
agelist = []
occlist = []
htlist = []
wtlist = []
sedentarylist =[]
moderatelist = []
activelist =[]

## Storing existing person info in separate lists
for person in content:
    person = person.replace('\n','')
    detail = person.split(',')
    firstlist.append(detail[0])
    lastlist.append(detail[1])
    agelist.append(detail[2])
    occlist.append(detail[3])
    htlist.append(detail[4])
    wtlist.append(detail[5])
    sedentarylist.append(detail[6])
    moderatelist.append(detail[7])
    activelist.append(detail[8])

## Ask for additional person info (if any)
addmore = input('Is there anyone else you would like to add? (Y/N) ')
if addmore == 'Y' or addmore == 'y':
    numadd = int(input('How many? '))
    for i in range(numadd):
        print('----- Person', i+1, '-----')
        first = input('First name: ')
        last = input('Last name: ')
        age = input("Age: ")
        occ = input("Occupation: ")
        ht = input("Height: ")
        wt = input("Weight: ")
        activity = input("Activity level (1-sedentary, 2-moderate, 3-active): ")

        ## Before exiting the loop, we need to save this person's info into our lists
        firstlist.append(first)
        lastlist.append(last)
        agelist.append(age)
        occlist.append(occ)
        htlist.append(ht)
        wtlist.append(wt)

        ## Address different activity levels in lists
        if activity == '1':
            sedentarylist.append('x')
            moderatelist.append('')
            activelist.append('')
        elif activity == '2':
            sedentarylist.append('')
            moderatelist.append('x')
            activelist.append('')
        elif activity == '3':
            sedentarylist.append('')
            moderatelist.append('')
            activelist.append('x')
        else:
            sedentarylist.append('')
            moderatelist.append('')
            activelist.append('')

maxfirstlen = 12
maxlastlen = 12
maxocclen = 12
for i in range(len(firstlist)):
    if len(firstlist[i]) > maxfirstlen:
        maxfirstlen = len(firstlist[i])
    if len(lastlist[i]) > maxlastlen:
        maxlastlen = len(lastlist[i])
    if len(occlist[i]) > maxocclen:
            maxocclen = len(occlist[i])

## obtaining new file name for output file
filename = input('What is the output file? ')
outfile = open(filename, 'w')

## header row
outfile.write('{:{len1}} {:{len2}} {:3} {:{len3}} {:5} {:5} {:10}\n'.format('first', 'last', 'age', 'occupation', 'ht', 'wt', 'activity', len1 = maxfirstlen, len2= maxlastlen, len3 = maxocclen))

## write individual info
for i in range(len(firstlist)):
    if sedentarylist[i] == 'x':
        outfile.write('{:{len1}} {:{len2}} {:3} {:{len3}} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'sedentary', len1 = maxfirstlen, len2= maxlastlen, len3 = maxocclen))
    elif moderatelist[i] == 'x':
        outfile.write('{:{len1}} {:{len2}} {:3} {:{len3}} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'moderate', len1 = maxfirstlen, len2= maxlastlen, len3 = maxocclen))
    elif activelist[i] == 'x':
        outfile.write('{:{len1}} {:{len2}} {:3} {:{len3}} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'active', len1 = maxfirstlen, len2= maxlastlen, len3 = maxocclen))
    else:
        outfile.write('{:{len1}} {:{len2}} {:3} {:{len3}} {:5} {:5} {:10}\n'.format(firstlist[i], lastlist[i], agelist[i], occlist[i], intoft(htlist[i]), wtlist[i], 'N/A', len1 = maxfirstlen, len2= maxlastlen, len3 = maxocclen))

outfile.close()
"""

########## Nested for loops ##########

"""
## Task: write a function that prints the factorial of all numbers up to n

def factorial(factorn):
    '''print factorial of all numbers up to n'''
    for i in range(1, factorn + 1):         # 1         2           3           4
        currentnum = 1                      # 1         1           1           1
        for j in range(2, i + 1):           # never     j = 2       j = 2, 3    j = 2, 3, 4
            currentnum = currentnum * j     #           1 * 2       1 * 2 * 3   1 * 2 * 3 * 4
        print(currentnum)                   # print(1)  print(2)    print(6)    print(24)

factorial(4)

factorial(12)
"""


"""
## Task: write a function that takes two lists of numbers and returns a list
## containing all possible sums of numbers from the two lists

a = [3, 15, 44]
b = [4, 6, 32]
# 3 + 4, 3 + 6, 3 + 32, 15 + 4, 15 + 6, 15 + 32, 44 + 4, 44 + 6, 44 + 32

def listSum(list1, list2):
    'return a list of all possible sums of the two lists'
    sumlist = []
    for i in list1:                     ## i = 3                i = 15             i = 44
        for j in list2:                 ## j = 4    6   32      j = 4   6   32     j = 4    6   32
            sumlist.append(i + j)       ##     7    9   35          19  21  47         48   50  76

    return sumlist

print(listSum(a, b))
"""

##### 2D List #####
## thislist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## print(thislist[1])
## print(thislist[5])
## print(thislist[1][0])
## print(thislist[2][2])

"""
## Task: Write a function that multiplies the nth x mth element of thisList to nth x mth element of thatList
## returns the multiplied 2D list
##  list1:      1, 2, 3     2, 4, 6     2, 8, 18
##  list2:      4, 5, 6     3, 5, 7     9, 5, 42
##  result:     4, 10, 18    6, 20, 42   18, 40, 756

def elementTimes(list1, list2):
    'multiply the nth x mth element of list1 to nth x mth element of list2'
    list3 = list1.copy()
    for i in range(len(list1)):             ## i is the inner list
        for j in range(len(list1[i])):      ## j is the element in the inner list
            list3[i][j] = list1[i][j] * list2[i][j]
    return list3

thisList = [[1, 2, 3], [2, 4, 6], [2, 8, 18]]
thatList = [[4, 5, 6], [3, 5, 7], [9, 5, 42]]

print(elementTimes(thisList, thatList))

"""

"""
def timesTab(timesn):
    'print a times table up to n'
    myTable = []
    for i in range(timesn):
        myTable.append([])      ##appended an empty list to represent a new row to start
        for j in range(timesn):
            myTable[i].append((i+1)*(j+1))
    return myTable

a = timesTab(5)
print(a)


b = timesTab(12)
for i in range(len(b)):
    row = ''
    for j in range(len(b[i])):
        row = row + '{:4}'.format(b[i][j])
    print(row)
"""


########## While Loops ##########
## while loops are similar to for loops, except you don't know how many times you'd like to go through the loop
## You DO know your stopping condition (when you'd like to stop)
## The while loop starts like an if statement (if <<condition>>:)
## >> while <<condition>>:

"""
## Simple example
booli = True
while booli:
    print(booli)
    booli = False
"""

"""
## Print powers of 2 up to 100
x = 2
while x < 100:
    print(x)
    x *= 2      ## same as x = x * 2

print('Done')
print('Outside x is now:', x)           ## Pay attention to the order of your code! Is this what you expected?

"""

"""
## While Loop - Decay Function
## Every year, 3% of the population of Boringville move out of the town.
## No one wants to move in to Boringville. In the year 2019, the mayor
## of Boringville realized that the town would crumble if the population reached
## below 10,000 people. He wants to restructure the town to attract more
## residents. How many years does the mayor have to rebuild the town
## assuming there's currently 11,000 people in Boringville?

pop = 11000
year = 0
while pop >= 10000:
    pop *= 0.97
    year += 1

print(year)
"""

"""
## Asking the user for a positive integer (HINT FOR IP3)
badnum = True
while badnum:
    try:
        num = int(input("Please enter a positive integer: "))
        if num > 0:
            badnum = False
            print('positive number')        ## use print to help you keep track of what's going on in your programs!
    except:
        badnum = True
        print('non-integer')
"""

"""
## Asking the user for a good file

badfile = True
while badfile:
    try:
        filename = input('File Name: ')
        openfile = open(filename)
        badfile = False
    except:
        badfile = True
"""

########## break, continue, pass ##########

"""
## Asking the user for a positive integer (HINT FOR IP3)
badnum = True
while badnum:
    try:
        num = int(input("Please enter a positive integer: "))
        if num > 0:
            badnum = False
    except:
        pass        ## pass does nothing. It's used as a placeholder.

"""

"""
## Asking the user for a good file
badfile = True
while badfile:
    try:
        filename = input('File Name: ')
        openfile = open(filename)
        badfile = False
    except:
        pass
"""


"""
## break -- stops the entire loop once it is encountered (innermost loop that is still running)
def guessname():
    name = input('Guess my name: ')
    while name != 'Python':
        if name == 'Quit':
            break
        name = input('Guess again: ')
    if name == 'Python':
        print('You got it!')
    else:
        print('Awww.')

guessname()
"""



"""
## You can use "return" as a break to the function -- stop the function where it encounters the return
def guessname():
    name = input('Guess my name: ')
    while name != 'Python':
        if name == 'Quit':
            return                      ## return will stop the function entirely
        name = input('Guess again: ')
    if name == 'Python':
        print('You got it!')
    else:
        print('Awww.')

guessname()
print('We are done with the function.')
"""


"""
## Learning Quiz 17, Problem 5
def myfun(word):
    while True:
        return 'done'       ## the return stops the function before we can ever print anything
        print(word)

userin = input('Enter name: ')
myfun(userin)
"""

"""
def beforeneg(numlist):
    'print values in the list until it comes across a negative number'
    for i in numlist:
        if i < 0:
            break
        print(i, end = ' ')
    print('We are done with the for-loop')

beforeneg([1,2,3,4,5,-5,4,-3,-2,1,2,3])
"""

"""
## continue - stops the current iteration of the loop once it's encounter, but it will continue with the next iteration
def beforeneg(numlist):
    'print values in the list until it comes across a negative number'
    for i in numlist:
        if i < 0:
            continue
        print(i, end = ' ')
    print('We are done with the for-loop')

beforeneg([1,2,3,4,5,-5,4,-3,-2,1,2,3])
"""

"""
## pass is just a placeholder. It does nothing for your loop
def beforeneg(numlist):
    'print values in the list until it comes across a negative number'
    for i in numlist:
        if i < 0:
            pass
        print(i, end = ' ')
    print('We are done with the for-loop')

beforeneg([1,2,3,4,5,-5,4,-3,-2,1,2,3])
"""



########## Dictionaries ##########
## Suppose we want to associate students with their ID numbers rather than index numbers
## We should use a dictionary
## mylist = ['Person1', 'Person2', 'Person3']
## studentlist = {id1: 'Person1', id2: 'Person2', id3: 'Person3'}

## dictionaryformat = {key: value, key: value, key: value}

"""
student = {'123456': ['Anna', 'Barbara'], '345678': ['Joe', 'Bruin'], '567890': ['Josephine', 'Bruin']}
print(student['123456'])
print(student.get('123456'))
## print(student[0])       ## DOES NOT WORK

print(student.items())      ## Note, the data type is not something we can work with yet
print(student.keys())
print(student.values())

print(list(student.items()))        ## change the data type to a list
print(list(student.keys()))
print(list(student.values()))

student.pop('123456')       ## this removed ['Anna', 'Barbara'] from our dictionary
print(student)
"""

"""
student = {'123456': ['Anna', 'Barbara'], '345678': ['Joe', 'Bruin'], '567890': ['Josephine', 'Bruin']}
student2 = {'234567': ['April', 'Summer'], '456789': ['May', 'Spring'], '135790': ['June', 'Winters']}
student.update(student2)        ##updating student with the students in student2
print(student)

student3 = {'246801': ['A', 'B']}
student.update(student3)

student3 = {'123456': ['Annabelle', 'Barbara']}
student.update(student3)        ## if there's someone with the same key, then it will replace the old info
print(student)
"""

'''
Other dictionary methods
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''

"""
## Strings, integers, floats, and tuples can be keys. Lists cannot be keys.
## You can have ANY value.
dictionary1 = {3903213: 'apple', 8943829: 'orange', 8493024: 'grapes'}
dictionary2 = {83921.2: [1, 2], 28291.3: [3, 4], 32902.3: [5, 6]}
dictionary3 = {(3,4): 'Point A', (6, 7): 'Point B', (101, 102): 'Point C'}
dictionary4 = {'break': 'ends the loops', 'continue': 'skip the rest of the iteration', 'pass': 'does nothing'}

## multiple keys can have the same value
dictionary5 = {3903213: 'apple', 8943829: 'apple', 8493024: 'apple'}
print(dictionary5)

## but multiple values cannot have the same key (Python will look only at the latest one)
dictionary6 = {3903213: 'apple', 3903213: 'orange', 3903213: 'grapes'}
print(dictionary6)
"""



########## SETS ##########
## no order
## cannot have multiple of the same thing
"""
popnames2050 = {'Spongebob', 'Patrick', 'Squidward', 'Spongebob'}
print(popnames2050)
"""

"""
popnames2050 = {'Spongebob', 'Patrick', 'Squidward', 'Spongebob'}
popnames2060 = {'Joey', 'Phoebe', 'Ross', 'Monica', 'Patrick'}
namesinter = popnames2050 & popnames2060        ## intersection (&), what is in both sets
namesunion = popnames2050 | popnames2060        ## union (|), combination of both sets
namesdiff = popnames2050 - popnames2060         ## what is in 2050 but not 2060
namesdifftw = popnames2050 ^ popnames2060       ## what is in one and only one of the sets
print(namesinter)
print(namesunion)
print(namesdiff)
print(namesdifftw)
"""

"""
## Some methods
popnames2050 = {'Spongebob', 'Patrick', 'Squidward', 'Spongebob'}
popnames2050.add('Mr.Krabs')
popnames2050.remove('Spongebob')
popnames2050.clear()


emptydict = {}
emptyset = set()
"""


########## the random module ##########
## import random        ## remember to import at the very beginning!

random.seed(113)        ## setting the seed is used for testing. It makes sure you get the SAME random numbers (so it won't be "random")
                        ## make sure that if you use random in a program, remove seed() so the numbers 'appear' truly random
i = random.randrange(5, 10)     ## random numbers 5, 6, 7, 8, 9 (but not 10)
print(i)

j = random.uniform(0,1)         ## random number between 0 and 1
print(j)

mylist = ['apple', 'orange', 'grape', 'strawberry', 'banana']
random.shuffle(mylist)          ## shuffle the list
print(mylist)

k = random.choice(mylist)       ## randomly pick 1 from the list
print(k)

m = random.sample(mylist, 3)    ## randomly pick 3 (without replacement) from the list
print(m)
