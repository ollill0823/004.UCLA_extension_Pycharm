'''
File Name: module2.py

Agenda
1. Strings
2. Text Files
3. Time
4. Example of Saving Text with Time Stamp
5. zfill() and format()
6. Writing and Reading formatted txt/csv
7. Errors and Exceptions
'''

"""
##### String and if/else statements #####
veggie = input('State a vegetable: ')
if veggie > 'spinach':
    print('this word starts with t, u, v, w, x, y, or z')
elif veggie > 'carrot':
    print('greater than carrot and less than spinach')
elif veggie > 'broccoli':
    print('greater than broccoli and less than carrot')
else:
    print('not greater than broccoli')
"""


"""
fish1 = 'One fish\nTwo fish\nRed fish\nBlue fish'

## you can also use triple single/double quotes

fish2 = '''One fish
Two fish
Red fish
Blue fish
'''
print(fish1)
print(fish2)
print(fish1 == fish2)       ## False because fish2 has an extra new line

"""


########## Working with text (.txt) files ##########
"""File modes
'r' read    (cannot modify the text file, default)
'w' write   (nothing to read out of the text file, you will overwrite that is there)
'a' append  (add things at the end of the text file, keep what's already there)
'r+' read and write     (dangerous stuff! -- not today)

't' text    (textfile, default)
'b' binary  (binary file, .jpg, .gif -- not today)
"""

"""
frozen = open('letitgo.txt', 'rt')          ## same as open('letitgo.txt') because 'rt' (read, text) is the default

# Table 4.5 in textbook "File methods"
print(frozen.read(1))           ##read and print just the first character
print(frozen.read(3))           ##read and print the next 3 characters
print(frozen.readline())        ##readline() until it sees \n
print(frozen.readlines())

frozen.close()                  ## remember to close your file when you are done

print(frozen.read(1))           ## we will get an error because the file is now closed
"""

"""
frozen = open('letitgo.txt')
content = frozen.read()
frozen.close()

print(content)
print(content.count('it go'))
"""

"""
## Task: Write a function that counts how many characters are in our file
def numChars(filename):
    'return the number of characters in file filename'
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    return len(content)         ## this includes special characters like spaces, \n, \t

n = numChars('letitgo.txt')
print(n)
"""

"""
## Task: Write a function that counts how many lines are in our file
def numLines(filename):
    'return the number of characters in file filename'
    infile = open(filename, 'r')
    contentlist = infile.readlines()
    infile.close()
    print(contentlist)

    return len(contentlist)     ## how many things are in our list?

lines = numLines('letitgo.txt')
print(lines)
"""

"""
##### Writing Files #####
output = open('textfile1.txt', 'w')
output.write('Hello,')
output.write('testing123')
output.write(' Note, you need to manually add spaces')
output.close()

output = open('textfile1.txt', 'w')     ##'w' will create a new file OR overwrite an existing file
output.write('Oh no! Everything is gone!')
output.close()

output = open('textfile1.txt', 'a')     ##'a' will append to an existing file
output.write(' Whew, the last text is still here.')
output.close()
"""

"""
## Task 1: Ask the user how many jokes, and keep prompting for jokes until the quota is met
## Store all jokes and answers in a file with "Q:" for questions and "A:" for answer

numJokes = eval(input('How many jokes do you have? '))
jokefile = open('jokes.txt', 'a')       ## 'a' to keep old jokes
for i in range(numJokes):
    joke = input('Tell me joke #' + str(i+1) + ': ')
    ans = input('I don\'t know. What is the answer? ')          ## same as "I don't know. What is the answer?"
    jokefile.write('Q: ' + joke + '\n')
    jokefile.write('A: ' + ans + '\n')

jokefile.close()
"""

"""
## Task 2: Using the jokes file, print only the questions in a new file 'jokesQ.txt'
jokesfile = open('jokes.txt', 'r')
text = jokesfile.readlines()
jokesfile.close()

qfile = open('jokesQ.txt', 'w')

for line in text:
    if line[:2] == 'Q:':
        qfile.write(line[3:])

qfile.close()
"""

"""
## Task 3: Task 2, but with numbered questions
jokesfile = open('jokes.txt', 'r')
text = jokesfile.readlines()
jokesfile.close()

qfile = open('jokesQ.txt', 'w')

qnum = 1
for line in text:
    if line[:2] == 'Q:':
        qfile.write(str(qnum) + ': ' + line[3:])
        qnum += 1       ## same as qnum = qnum + 1, incrementing by 1

qfile.close()
"""


########## Time ##########
"""
import time

## This will give you how many seconds it has been since the 'epoch' (beginning of a period in time)
## For most systems in Python, the epoch is January 1, 1970 at midnight in GMT
print(time.time())

print(time.gmtime(0))

print(time.localtime())
"""

"""
## strftime()
'''For basic list of directives, see Table 4.3 (page 107) of textbook
Other directives:
%f microsecond (000000 - 999999)
%j day of year (001-366)
%m month number
%U week number of year (Sunday as first day)
%W week number of year (Monday as first day)
%w weekday number(0 is Sunday, 1 is Monday, ..., 6 is Saturday)
%z UTC offset (-0800 for PST, -0700 for PDT)
'''

import time

datecondensed = time.strftime('%a, %m/%d/%y', time.localtime())
dateexpanded = time.strftime('%A, %B %d, %Y', time.localtime())
time24 = time.strftime('%H:%M:%S %Z', time.localtime())
time12 = time.strftime('%I:%M:%S %p %Z', time.localtime())

print(datecondensed)
print(dateexpanded)
print(time24)
print(time12)
"""

"""
## Task 4: Time-Stamp Joke Entries
import time

numJokes = eval(input('How many jokes do you have? '))
jokefile = open('jokes.txt', 'a')       ## 'a' to keep old jokes
for i in range(numJokes):

    joke = input('Tell me joke #' + str(i+1) + ': ')
    jokets = time.strftime('%m/%d/%y %H:%M:%S', time.localtime())

    ans = input('I don\'t know. What is the answer? ')
    ansts = time.strftime('%m/%d/%y %H:%M:%S', time.localtime())

    jokefile.write('[' + jokets + '] Q: ' + joke + '\n')
    jokefile.write('[' + ansts + '] A: ' + ans + '\n')

jokefile.close()
"""

"""
########## zfill() ##########
## zfill() pads strings on the left with zeroes to fill width
weekday = 'Sunday'
month = 'September'
day = 11
year = 2022
hour = 8
minute = 3
second = 7

print(str(hour))
print(str(hour).zfill(5))

print(str(hour) + ':' + str(minute) + ':' + str(second))

## HH:MM:SS
print(str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2))
"""

"""
########## format() ##########

weekday = 'Sunday'
month = 'September'
day = 11
year = 2022
hour = 8
minute = 3
second = 7

## dow, month day, year, at HH:MM:SS
datefmt = '{}, {} {}, {}, at {}:{}:{}'.format(weekday, month, day, year, hour, minute, second)
print(datefmt)

datefmt = '{}, {} {}, {}, at {}:{}:{}'.format(weekday, month, day, year, str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
print(datefmt)

## By default, blank {} will go in order of the arguments that you gave
## but, if you type in numbers, you will re-order what goes in each  placeholder
datefmt = '{3}, {2} {1}, {0}, at {5}:{5}:{5}'.format(weekday, month, day, year, str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
print(datefmt)
"""

"""
## print the roster in a formatted manner
## {last}, {first} is a {##}-year old {occupation}
roster = [['Anna','Barbara',35,'nurse'],
          ['Catherine','Do',45,'physicist'],
          ['Eric','Frederick',28,'teacher'],
          ['Gabriel','Hernandez',55,'surgeon'],
          ['Ivy','Joo',31,'engineer'],
          ['Kelly','Marks',21,'student']]

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{}, {} is a {}-year old {}'.format(person[1], person[0], person[2], person[3])
    print(formattedtext)
"""

"""
## 12 character spaces for first name   (left aligned because string)
## 12 character spaces for last name    (left aligned because string)
## 3 character spaces for age           (right aligned because int)
## 12 character spaces for occupation   (left aligned because string)
roster = [['Anna','Barbara',35,'nurse'],
          ['Catherine','Do',45,'physicist'],
          ['Eric','Frederick',28,'teacher'],
          ['Gabriel','Hernandez',55,'surgeon'],
          ['Ivy','Joo',31,'engineer'],
          ['Kelly','Marks',21,'student']]

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{:12}{:12}{:3}{:12}'.format(person[0], person[1], person[2], person[3])
    print(formattedtext)
"""


########## Alignment ##########
## {:>12}       12 spaces, right aligned (by default, numbers are right aligned)
## {:<10}       10 spaces, left aligned (by default, strings are left aligned)
## {:^11}       11 spaces, center aligned (extra space, if odd number, will go to the right)
## {:_<9}       9 spaces, right aligned with '_' to show spaces

"""
## Formatted roster output with everything left-aligned
roster = [['Anna','Barbara',35,'nurse'],
          ['Catherine','Do',45,'physicist'],
          ['Eric','Frederick',28,'teacher'],
          ['Gabriel','Hernandez',55,'surgeon'],
          ['Ivy','Joo',31,'engineer'],
          ['Kelly','Marks',21,'student']]

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{:<12}{:<12}{:<3}{:<12}'.format(person[0], person[1], person[2], person[3])
    print(formattedtext)
"""

"""
## Formatted roster output with everything left-aligned (with character fill-ins)
roster = [['Anna','Barbara',35,'nurse'],
          ['Catherine','Do',45,'physicist'],
          ['Eric','Frederick',28,'teacher'],
          ['Gabriel','Hernandez',55,'surgeon'],
          ['Ivy','Joo',31,'engineer'],
          ['Kelly','Marks',21,'student']]

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{:-<12}{:*<12}{:.<3}{:~<12}'.format(person[0], person[1], person[2], person[3])
    print(formattedtext)
"""

"""
## What if your text is longer than how many spaces you allotted
## Answer: the text will bleed over
roster = [['Anna','Barbara',35,'nurse'],
          ['Catherine','Do',45,'physicist'],
          ['Eric','Frederick',28,'teacher'],
          ['Gabriel','Hernandez',55,'surgeon'],
          ['Ivy','Joo',31,'engineer'],
          ['Kelly','Marks',21,'student']]

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{:-<6}{:*<12}{:.<3}{:~<12}'.format(person[0], person[1], person[2], person[3])
    print(formattedtext)
"""

"""
## How do you make the text length (allocated spaces) a variable?
roster = [['Anna','Barbara',35,'nurse'],
          ['Catherine','Do',45,'physicist'],
          ['Eric','Frederick',28,'teacher'],
          ['Gabriel','Hernandez',55,'surgeon'],
          ['Ivy','Joo',31,'engineer'],
          ['Kelly','Marks',21,'student']]
longestfirstname = 9
longestlastname = 9
longestoccupation = 9

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{:<{lenfirst}}{:<{lenlast}}{:<3}{:<{lenocc}}'.format(person[0], person[1], person[2], person[3],
                                                                          lenfirst = longestfirstname + 1, lenlast = longestlastname + 1, lenocc = longestoccupation + 1)
    print(formattedtext)
"""

"""
## Numbers in front of the color will re-order the placeholders
roster = [['Anna','Barbara',35,'nurse'],
          ['Catherine','Do',45,'physicist'],
          ['Eric','Frederick',28,'teacher'],
          ['Gabriel','Hernandez',55,'surgeon'],
          ['Ivy','Joo',31,'engineer'],
          ['Kelly','Marks',21,'student']]
longestfirstname = 9
longestlastname = 9
longestoccupation = 9

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{1:<{lenlast}}{0:<{lenfirst}}{2:<3}{3:<{lenocc}}'.format(person[0], person[1], person[2], person[3],
                                                                          lenfirst = longestfirstname + 1, lenlast = longestlastname + 1, lenocc = longestoccupation + 1)
    print(formattedtext)
"""

"""
## decimal numbers, 8 spaces and 5 digits
print('{:8.5}'.format(1000/3))
## decimal numbers, 10 spaces and 6 digits
print('{:10.6}'.format(1000/3))

## string, 8 spaces and only 5 letters
print('{:8.5}'.format('phalange'))
## string, 10 spaces and 6 letters
print('{:-<10.6}'.format('phalange'))

## decimal numbers, 11 spaces and 5 digits AFTER THE DECIMAL (5 decimal places)
print('{:11.5f}'.format(1000/3))

## scientific notation
print('{:e}'.format(1000/3))

## decimal numbers, 11 spaces and 5 digits AFTER THE DECIMAL (5 decimal places) with leading 0's
print('{:011.5f}'.format(1000/3))
"""

"""
n = 10
'{:b}'.format(n)    ## binary
'{:c}'.format(n)    ## unicode
'{:d}'.format(n)    ## decimal notation, default
'{:o}'.format(n)    ## octal numeral, base 8: 01234567
'{:x}'.format(n)    ## hexadecimal, base 16: 0123456789abcdef

print('{:b}'.format(n))    ## binary
print('{:c}'.format(n))     ## unicode (10 means '\n')
print('{:d}'.format(n))    ## decimal notation, default
print('{:o}'.format(n))    ## octal numeral, base 8: 01234567
print('{:x}'.format(n))   ## hexadecimal, base 16: 0123456789abcdef
"""


"""
Number  Octal   Binary
0       00       0000
1       01       0001
2       02       0010
3       03       0011
4       04       0100
5       05       0101
6       06       0110
7       07       0111
8       10       1000
9       11       1001
10      12       1010
"""

##### Reading and Writing Formatted txt/csv


"""
def intoft(inches):
    'returns a string value of the height in feet\'inches"'
    ft = inches//12       ## 12 inches to 1 foot
    inch = inches%12
    return str(ft) + "'" + str(inch) + '"'

def kgtolb(kg):
    'take weight in kg and return weight in pounds'
    return round(kg * 2.20462, 1)

## first name
## last name
## age
## height in inches  -- convert this to ft inches
## weight in kg  -- convert this to pounds
roster = [['Anna','Barbara', 35, 60, 58.5],
           ['Catherine','Do', 45, 65, 61.5],
           ['Eric','Frederick', 28, 65, 63.5],
           ['Gabriel','Hernandez', 55, 70, 68],
           ['Ivy','Joo', 31, 55, 57],
           ['Kelly','Marks', 21, 75, 60]]

output = open('roster1.txt', 'w')
header = '{:<15} {:<15} {:<3} {:<5} {:<5}\n'.format('First', 'Last', 'Age', 'Ht', 'Wt')
output.write(header)

for person in roster:
    ## first name:      person[0]
    ## last name:       person[1]
    ## age:             person[2]
    ## height:          intoft(person[3])
    ## weight:          kgtolb(person[4])
    personfmt = '{:<15} {:<15} {:<3} {:<5} {:<5}\n'.format(person[0], person[1], person[2], intoft(person[3]), kgtolb(person[4]))
    output.write(personfmt)

output.close()


roster2 = [['Nancy','Owens', 36, 65, 59],
           ['Patty','Queens', 48, 63, 66],
           ['Roderick','Stevenson', 57, 62, 65],
           ['Timothy','Umeda', 52, 77, 69],
           ['Veronica','Winters', 33, 63, 59],
           ['Xiaoya','Zhu', 24, 71, 61]]

output = open('roster1.txt', 'a')           ## MAKE SURE YOU APPEND TO NOT OVERWRITE THE ORIGINAL FILE

for person in roster2:
    ## first name:      person[0]
    ## last name:       person[1]
    ## age:             person[2]
    ## height:          intoft(person[3])
    ## weight:          kgtolb(person[4])
    personfmt = '{:<15} {:<15} {:<3} {:<5} {:<5}\n'.format(person[0], person[1], person[2], intoft(person[3]), kgtolb(person[4]))
    output.write(personfmt)

output.close()
"""

"""
## TASK: Formatted data file with the length of the longest first name (as opposed to the arbitrary picked number)

def intoft(inches):
    'returns a string value of the height in feet\'inches"'
    ft = inches//12       ## 12 inches to 1 foot
    inch = inches%12
    return str(ft) + "'" + str(inch) + '"'

def kgtolb(kg):
    'take weight in kg and return weight in pounds'
    return round(kg * 2.20462, 1)

## first name
## last name
## age
## height in inches  -- convert this to ft inches
## weight in kg  -- convert this to pounds
roster = [['Anna','Barbara', 35, 60, 58.5],
           ['Catherine','Do', 45, 65, 61.5],
           ['Eric','Frederick', 28, 65, 63.5],
           ['Gabriel','Hernandez', 55, 70, 68],
           ['Ivy','Joo', 31, 55, 57],
           ['Kelly','Marks', 21, 75, 60]]


longestfirst = 5        ## need 5 spaces minimum for first name
longestlast = 5         ## need 5 spaces minimum for last name

for person in roster:

    ## First Name: if name is longer than longestfirst, then I need to update longestfirst
    if len(person[0]) > longestfirst:
        longestfirst = len(person[0])

    ## Last Name: if name is longer than longestlast, then I need to update longestlast
    if len(person[1]) > longestlast:
        longestlast = len(person[1])



output = open('roster1.txt', 'w')
header = '{:<{var1}} {:<{var2}} {:<3} {:<5} {:<5}\n'.format('First', 'Last', 'Age', 'Ht', 'Wt', var1 = longestfirst, var2 = longestlast)
output.write(header)

for person in roster:
    ## first name:      person[0]
    ## last name:       person[1]
    ## age:             person[2]
    ## height:          intoft(person[3])
    ## weight:          kgtolb(person[4])
    personfmt = '{:<{var1}} {:<{var2}} {:<3} {:<5} {:<5}\n'.format(person[0], person[1], person[2], intoft(person[3]), kgtolb(person[4]), var1 = longestfirst, var2 = longestlast)
    output.write(personfmt)

output.close()
"""

"""
## Convert CSV data format to spaced data format
## Note: CSV is also a text file

input = open('roster_small.csv', 'r')
input.readline()        ## skipping over the first line (get rid of header)
roster = input.readlines()
input.close()


output = open('roster2.txt', 'w')
header = '{:<15} {:<15} {:<3} {:<15}\n'.format('First', 'Last', 'Age', 'Occupation')
output.write(header)

for person in roster:
    currentrow = person.replace('\n', '')
    personinfo = currentrow.split(',')
    personfmt = '{:<15} {:<15} {:<3} {:<15}\n'.format(personinfo[0], personinfo[1], personinfo[2], personinfo[3])
    output.write(personfmt)

output.close()
"""


##### Errors and Exceptions #####
## infile = open('roster5.csv')
## Program will crash if file does not exist

"""
## Basic try/except pair
try:
    userinput = input('File Name: ')
    infile = open(userinput)
    print('Open success!')
    infile.close()
except:
    print('Error!')
"""

"""
## If you know what type of error you're looking for, you can specify what you want to happen given the particular error
try:
    userinput = input('File Name: ')
    userint = int(input('Give me an integer: '))
    infile = open(userinput)
    print('Open success!')
    infile.close()
except IOError:
    print('File not found!')
except ValueError:
    print('That is not an integer.')
except:
    print('Other error.')
"""

## ORDER MATTERS!
try:
    userinput = input('File Name: ')
    infile = open(userinput)                ## Notice line swap
    userint = int(input('Give me an integer: '))
    print('Open success!')
    infile.close()
except IOError:
    print('File not found!')
except ValueError:
    print('That is not an integer.')
except:
    print('Other error.')