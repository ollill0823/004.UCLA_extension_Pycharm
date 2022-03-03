'''
File Name: module4.py

Agenda
1. Individual Programming 3 (Overview)
2. Encapsulation in Functions
3. Namespaces
4. Classes
5. Overloaded Operators
6. Inheritance
7. Recursion
8. Individual Programming 4
'''



##### Individual Programming 3 #####
'''
## Step 1: Ask the user for a file
badfile = True
while badfile:
    try:
        filename = input("Please enter the file name: ")
        infile = open(filename)
        badfile = False
    except IOError:
        print("Error. File not found. ")


## Step 2: Read and count the number of terms in the file
infile.readline()       ## move the cursor to skip the header line
content = infile.readlines()
print('There are', len(content), 'terms in this vocabulary list.', end = " ")


## Step 3: Put all of the vocabulary in a dictionary
vocabdict = {}          ## the main dictionary that holds all of the terms
for term in content:
    term = term.replace('\n', '')
    pair = term.split('\t')
    tempdict = {pair[0]: pair[1]}
    vocabdict.update(tempdict)          ## updating the main dictionary with each new term


## Step 4: Ask the user if they would like to add more items. If so, how many?
addterms = 'Y'
while addterms == 'Y' or addterms == 'y':
    addterms = input('Would you like to add more terms (Y/N)? ')

    if addterms == 'Y' or addterms == 'y':
        ## Step 4a: How many terms
        badnum = True
        while badnum:
            try:
                addnum = int(input('How many would you like to add? '))
                if addnum >= 0:
                    badnum = False
                else:
                    print('You gave a negative number. Please enter a positive integer. ')
            except:
                print("That's not an integer. Please enter a positive integer.")

        ## Step 4b: Obtain the terms
        for i in range(1, addnum + 1):
            newterm = input('Term #' + str(i) + ': ')

            ## Step 4c: Check if the term exists, and prompt to update
            vocablist = list(vocabdict.keys())
            if newterm in vocablist:
                update = input('Warning! This term is already in the vocabulary list. Update definition (Y/N)? ')
            else:
                update = 'Y'

            ## Step 4d: Add the term to the main dictionary
            if update == 'Y' or update == 'y':
                newdef = input('Definition #' + str(i) + ': ')
                tempdict = {newterm: newdef}
                vocabdict.update(tempdict)


## Step 5: Print the number of vocabulary terms and the term/definition pair
vocablist = list(vocabdict.keys())
print('There are', len(vocablist), 'terms in this vocabulary list.')
for term in vocablist:
    print(term, '-', vocabdict[term])


## Step 6: Ask for a save file and save (in a formatted manner)
savefile = input('What is the save file name? ')
saveto = open(savefile, 'w')
saveto.write('term\tdefinition\n')
for term in vocablist:
    saveto.write(term)
    saveto.write('\t')
    saveto.write(vocabdict[term])
    saveto.write('\n')
'''



##### Encapsulation in Functions #####

"""
x = 4

def squareSum(y):
    x = 5
    return x**2 + y**2          ## 5**2 + 3**2

squareSum(3)

print(x)            ## What will print?
"""

"""
x = 4

def squareSum(y):
    global x
    x = 5
    return x**2 + y**2          ## 5**2 + 3**2

squareSum(3)        ## at this point, we go into squareSum() and modify global x (now x is 5)

print(x)            ## What will print?
"""

"""
x = 7

def fun1():
    x = 5
    def fun2():
        x = 3
    def fun3():
        nonlocal x
        x = 1
    fun3()
    print("fun1 x is: ", x)

fun1()
print("global x is: ", x)
"""

"""
x = 7

def fun1():
    x = 5
    def fun2():
        x = 3
    def fun3():
        nonlocal x
        print("Point a: ", x)
        x = 1
        print("Point b: ", x)
    fun3()
    print("fun1 x is: ", x)

fun1()
print("global x is: ", x)
"""


##### Namespaces #####

"""
import math
print(math.pi)
print(pi)       ## error
"""


"""
from math import pi
print(pi)       ## can use pi without having to say math.pi
"""

"""
from math import *      ## the * will import everything, but be careful, because you might have the same variable/function name across multiple packages
"""

"""
import math as mth
print(mth.pi)
print(math.pi)      ## error
"""

"""
import module4_2

def f():
    print('hello')

f()     ## prints 'hello' as defined above
module4_2.f()
module4_2.g()
print(module4_2.newvar)

g()     ## this will give an error because we did not create a g function in this space
"""

"""
from module4_2 import g
from module4_2 import newvar

def f():
    print('hello')

f()     ## prints 'hello' as defined above
g()     
newvar
module4_2.f()   ## error
module4_2.g()   ## error
"""

"""
def f():
    print('hello')
    
from module4_2 import *     ## now we replaced the hello f() function with f() from module4_2

f()     ## prints 'hello'
g()
newvar
"""

##### Classes #####

"""
class Product:
    ''' represent an item in a grocery store '''
    def __init__(self, name, price, taxable):       ## you can change 'self' to a different term
        self.name = name
        self.price = price
        self.tax = taxable          ## common to have the same variable name, but not necessary
                                    ## taxable is a temporary variable
                                    ## tax is the variable attached to the Product itself

apple = Product('green apple', 0.99, False)

print(apple.name)
print(apple.price)
print(apple.tax)
print(apple.taxable)        ## error
"""


"""
## example using 'thing' in place of 'self' -- NOTE, THIS IS NOT COMMON PRACTICE
class Product:
    ''' represent an item in a grocery store '''
    def __init__(thing, name, price, taxable):       ## you can change 'self' to a different term
        thing.name = name
        thing.price = price
        thing.tax = taxable          ## common to have the same variable name, but not necessary
                                    ## taxable is a temporary variable
                                    ## tax is the variable attached to the Product itself

apple = Product('green apple', 0.99, False)

print(apple.name)
print(apple.price)
print(apple.tax)

"""

"""
class Product:
    ''' represent an item in a grocery store '''
    def __init__(self, name, price, tax):       ## you can change 'self' to a different term
        self.name = name
        self.price = price
        self.tax = tax

    def setPrice(self, price):          ## price does not have to have the same name as self.price
        '''set the price of the product'''
        if price >= 0:
            self.price = price

    def getPrice(self):                 ## no additional arguments here
        '''return the price of the product'''
        return self.price

apple = Product('green apple', 0.99, False)
print(apple.price)
print(apple.getPrice())     ## For now, this function does the same thing as apple.price
apple.setPrice(1.49)        ## setPrice(__) requires 1 argument -- price (what you want to set the price to)
print(apple.price)
print(apple.getPrice())     ## getPrice() does not require any argument

apple.price = 2.99          ## you can manually change the variable by accessing the variable directly
print(apple.getPrice())     ## but it's not recommended because there might be important code that you're overriding
                            ## compare apple.price = -2.99      versus      apple.setPrice(-2.99)
"""

##### Overloaded Operators and Optional Arguments #####
"""
class Product:
    '''represents items in a grocery store'''
    def __init__(self, name, price = 0, tax = True, ounce = 0):     ## by default, price is 0, tax is True, ounce is 0
        self.name = name
        self.price = price
        self.tax = tax
        self.ounce = ounce

    def setPrice(self, price):
        '''set the price of the product'''
        if price >= 0:
            self.price = price
        else:
            self.price = 0

    def getPrice(self):
        '''return the price of the product'''
        return self.price

    def setName(self, name):
        '''set the name of product'''
        self.name = name

    def getName(self):
        ''' return the name of the product '''
        return self.name

    def setTax(self, tax):
        '''set the tax of product'''
        self.tax = tax

    def getTax(self):
        ''' return the tax of the product '''
        return self.tax

    def setOunce(self, ounce):
        '''set the ounce of the product'''
        self.ounce = ounce

    def getOunce(self):
        '''return the ounce of the product'''
        return self.ounce

    def __eq__(self, other):            ## == operator
        ''' return True if the products have the same price '''
        return self.getPrice() == other.getPrice()          ## you can use self.price instead of self.getPrice()

dishsoap1 = Product('Dawn', 1.99, True)     ## by default ounce = 0
dishsoap2 = Product('Ajax', 1.79, True)
print(dishsoap1 == dishsoap2)
    ##dishsoap1 is the self, dishsoap2 is the other

dishsoap1.setPrice(1.79)
print(dishsoap1 == dishsoap2)


apple = Product('apple', 0.99, False)
ziplock = Product('Ziplock sandwich bags', 3.49)
print('Ziplock tax status:', ziplock.tax)
coupon = Product('coupon flyer', tax = False)       ## didn't need to enter a price for coupon flyer, and skip over to tax
"""

"""
class Product:
    '''represents items in a grocery store'''
    def __init__(self, name, price = 0, tax = True, ounce = 0):     ## by default, price is 0, tax is True, ounce is 0
        self.name = name
        self.price = price
        self.tax = tax
        self.ounce = ounce

    def setPrice(self, price):
        '''set the price of the product'''
        if price >= 0:
            self.price = price
        else:
            self.price = 0

    def getPrice(self):
        '''return the price of the product'''
        return self.price

    def setName(self, name):
        '''set the name of product'''
        self.name = name

    def getName(self):
        ''' return the name of the product '''
        return self.name

    def setTax(self, tax):
        '''set the tax of product'''
        self.tax = tax

    def getTax(self):
        ''' return the tax of the product '''
        return self.tax

    def setOunce(self, ounce):
        '''set the ounce of the product'''
        self.ounce = ounce

    def getOunce(self):
        '''return the ounce of the product'''
        return self.ounce

    def __eq__(self, other):            ## == operator
        ''' return True if the products have the same name, price, tax, and ounces '''
        if self.getPrice() != other.getPrice():
            return False
        if self.getName() != other.getName():
            return False
        if self.getTax() != other.getTax():
            return False
        if self.getOunce() != other.getOunce():
            return False
        return True

    def __ge__(self, other):        ## operator >=
        ''' return True if the price per count is greater than or equal to the other price per ounce '''
        return self.getPrice() / self.getOunce() >= other.getPrice() / other.getOunce()


dishsoap1 = Product('Dawn', 1.99, True, ounce = 10)
dishsoap2 = Product('Ajax', 1.79, True, ounce = 8)
dishsoap3 = Product('Ajax', 1.79, True, ounce = 8)
print(dishsoap1 == dishsoap2)
print(dishsoap3 == dishsoap2)
print(dishsoap1 >= dishsoap2)
print(dishsoap1 <= dishsoap2)       ## Although we didn't create a __le__ operator, this is automatically generated from __ge__

"""

##### Inheritance #####
## subcategories, e.g. a Fruit is a Product


"""
class Product:
    '''represents items in a grocery store'''
    def __init__(self, name, price = 0, tax = True, ounce = 0):     ## by default, price is 0, tax is True, ounce is 0
        self.name = name
        self.price = price
        self.tax = tax
        self.ounce = ounce

    def setPrice(self, price):
        '''set the price of the product'''
        if price >= 0:
            self.price = price
        else:
            self.price = 0

    def getPrice(self):
        '''return the price of the product'''
        return self.price

    def setName(self, name):
        '''set the name of product'''
        self.name = name

    def getName(self):
        ''' return the name of the product '''
        return self.name

    def setTax(self, tax):
        '''set the tax of product'''
        self.tax = tax

    def getTax(self):
        ''' return the tax of the product '''
        return self.tax

    def setOunce(self, ounce):
        '''set the ounce of the product'''
        self.ounce = ounce

    def getOunce(self):
        '''return the ounce of the product'''
        return self.ounce

    def __eq__(self, other):            ## == operator
        ''' return True if the products have the same name, price, tax, and ounces '''
        if self.getPrice() != other.getPrice():
            return False
        if self.getName() != other.getName():
            return False
        if self.getTax() != other.getTax():
            return False
        if self.getOunce() != other.getOunce():
            return False
        return True

    def __ge__(self, other):        ## operator >=
        ''' return True if the price per count is greater than or equal to the other price per ounce '''
        return self.getPrice() / self.getOunce() >= other.getPrice() / other.getOunce()


## A fruit is a product, but it is a special kind of product
class Fruit(Product):       ## by inheriting Product, we borrow all of the Product's functions AND we can add more properties/functions/variables
    def __init__(self, name, price=0, tax=False, lbs=0):
        Product.__init__(self, name, price, tax)        ## still need to initialise name, price, tax, ...
        self.lbs = lbs

    def setLbs(self, lbs = 0):
        ''' get the lbs of the fruit '''
        self.lbs = lbs

    def getLbs(self):
        ''' return the lbs of the fruit '''
        return self.lbs

orange = Fruit('Orange', 1.59, lbs = 2)
print(orange.getPrice())            ## Fruit is a Product, so Fruit will be able to use anything that Product has
print(orange.getLbs())
orange.setLbs(2.1)
print(orange.getLbs())

dishsoap = Product('Dawn')
dishsoap.getLbs()           ##Error, because dishsoap is a Product, which is not necessarily a Fruit (getLbs() belongs only to Fruit)
"""

"""
class Product:
    '''represents items in a grocery store'''
    def __init__(self, name, price = 0, tax = True, ounce = 0):     ## by default, price is 0, tax is True, ounce is 0
        self.name = name
        self.price = price
        self.tax = tax
        self.ounce = ounce

    def setPrice(self, price):
        '''set the price of the product'''
        if price >= 0:
            self.price = price
        else:
            self.price = 0

    def getPrice(self):
        '''return the price of the product'''
        return self.price

    def setName(self, name):
        '''set the name of product'''
        self.name = name

    def getName(self):
        ''' return the name of the product '''
        return self.name

    def setTax(self, tax):
        '''set the tax of product'''
        self.tax = tax

    def getTax(self):
        ''' return the tax of the product '''
        return self.tax

    def setOunce(self, ounce):
        '''set the ounce of the product'''
        self.ounce = ounce

    def getOunce(self):
        '''return the ounce of the product'''
        return self.ounce

    def __eq__(self, other):            ## == operator
        ''' return True if the products have the same name, price, tax, and ounces '''
        if self.getPrice() != other.getPrice():
            return False
        if self.getName() != other.getName():
            return False
        if self.getTax() != other.getTax():
            return False
        if self.getOunce() != other.getOunce():
            return False
        return True

    def __ge__(self, other):        ## operator >=
        ''' return True if the price per count is greater than or equal to the other price per ounce '''
        return self.getPrice() / self.getOunce() >= other.getPrice() / other.getOunce()


## A fruit is a product, but it is a special kind of product
class Fruit(Product):       ## by inheriting Product, we borrow all of the Product's functions AND we can add more properties/functions/variables
    def __init__(self, name, price=0, tax=False, lbs=0):
        Product.__init__(self, name, price, tax)        ## still need to initialise name, price, tax, ...
        self.lbs = lbs

    def setLbs(self, lbs = 0):
        ''' get the lbs of the fruit '''
        self.lbs = lbs

    def getLbs(self):
        ''' return the lbs of the fruit '''
        return self.lbs

    def getOunce(self):             ## Product already has a getOunce(); here, we're overwriting it
        ''' do not return anything '''
        return None

    def getTotal(self):
        ''' total price of the fruit '''
        return self.price * self.lbs

orange = Fruit('Orange', 1.59, lbs = 2)
print(orange.getPrice())            ## Fruit is a Product, so Fruit will be able to use anything that Product has
print(orange.getLbs())
orange.setLbs(2.1)
print(orange.getLbs())
print(orange.getOunce())
print(orange.getTotal())

dishsoap = Product('Dawn')
print(dishsoap.getOunce())
"""

##### Recursion #####
## function that calls itself
"""
def recurf(n):
    print(n)
    if n > 0:
        recurf(n-1)
    print('end', n)

recurf(4)
"""

## Recursion may take fewer lines of code (lower human labor cost)
## Example of how recursion could take fewer lines of code: Tower Hanoi

"""
## WARNING! Recursion needs a "base case" -- otherwise you can be stuck in an unexpected loop
def recurf(n):
    print(n)
    if n > 0:       ## the function doesn't have a valid stopping condition
        recurf(n+1)
    print('end', n)

recurf(4)
"""

"""
## Recursion is computationally expensive
import time

def count1(n):
    ''' count down using loops '''
    for i in range(n, 0, -1):
        print(i)

def count2(n):
    ''' recursively count down '''
    print(n)
    if n > 1:
        count2(n - 1)

start1 = time.time()
count1(990)
count1(990)
count1(990)
count1(990)
count1(990)
count1(990)
count1(990)
count1(990)
count1(990)
count1(990)
stop1 = time.time()

start2 = time.time()
count2(990)
count2(990)
count2(990)
count2(990)
count2(990)
count2(990)
count2(990)
count2(990)
count2(990)
count2(990)
stop2 = time.time()

print("Loop time: ", stop1 - start1)
print("Recursion time: ", stop2 - start2)

"""

##### Individual Programming 4 #####

""" 
rename(), renames the character
setlvl()
sethp()
setat()
setdf()
setexp()
getname()
getlvl()
gethp()
getat()
getdf()
getexp()
attack(), details below


The attack() method should take in one argument (another Character), whose hp you will be depleting by the attacking Character's attack points minus the defending Character's defense points. That is if Alpha (below) attacks Beta, Beta will lose 8 HP (10 Alpha_attack - 2 Beta_defense). At the end of each attack, print out who attacked who and current HP stats of the two characters. Note, HP cannot be more than the max HP or less than 0. In the attack method, you must also print "__ defeated __" if any one character's HP reaches 0.

"""


"""
class Character:
    def __init__(self, name, lvl = 1, hp = 100, at = 10, df = 1, exp = 1):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.at = at
        self.df = df
        self.maxhp = hp

    def sethp(self, hp):
        ''' sets the character's hp '''
        self.hp = hp

    def attack(self, other):
        print(other.name, "'s HP was ", other.hp, sep = "")
        print(self.name, "'s AT is ", self.at, sep = "")
        print(other.name, "'s DF is ", other.df, sep="")
        print(self.name, " attacked ", other.name, ".", sep = "")
        other.sethp(other.hp - (self.at - other.df))                ## make sure there's no healing
        print(other.name, "'s HP is now ", other.hp, sep="")

mario = Character('Mario')
luigi = Character('Luigi', df = 1)          ## if Luigi's df = 100, we end up getting healing Luigi

for i in range(20):
    mario.attack(luigi)
    
"""

"""
class Character:
    def __init__(self, name, lvl = 1, hp = 100, at = 10, df = 1, exp = 1):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.at = at
        self.df = df
        self.maxhp = hp

    def sethp(self, hp):
        ''' sets the character's hp to a new value or 0 (if hp is below 0)'''
        if hp <= 0:
            self.hp = 0
        else:
            self.hp = hp

    def attack(self, other):
        print(other.name, "'s HP was ", other.hp, sep = "")
        print(self.name, "'s AT is ", self.at, sep = "")
        print(other.name, "'s DF is ", other.df, sep="")
        print(self.name, " attacked ", other.name, ".", sep = "")
        if self.at > other.df:
            other.sethp(other.hp - (self.at - other.df))
        else:
            print(self.name, 'is too weak.')
        print(other.name, "'s HP is now ", other.hp, sep="")

mario = Character('Mario')
luigi = Character('Luigi', df = 1)

for i in range(20):
    mario.attack(luigi)
"""



class Character:
    def __init__(self, name, lvl = 1, hp = 100, at = 10, df = 1, exp = 1):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.at = at
        self.df = df
        self.maxhp = hp

    def sethp(self, hp):
        ''' sets the character's hp to a new value or 0 (if hp is below 0)'''
        if hp <= 0:
            self.hp = 0
        else:
            try:
                self.hp = int(hp)
            except:
                self.hp = hp

    def attack(self, other):
        print(other.name, "'s HP was ", other.hp, sep = "")
        print(self.name, "'s AT is ", self.at, sep = "")
        print(other.name, "'s DF is ", other.df, sep="")
        print(self.name, " attacked ", other.name, ".", sep = "")
        if self.at > other.df:
            other.sethp(other.hp - (self.at - other.df))
        else:
            print(self.name, 'is too weak.')
        print(other.name, "'s HP is now ", other.hp, sep="")



class MajorCharacter(Character):
    def __init__(self, name, lvl=1, hp=100, at=10, df=1, exp=1):
        Character.__init__(self, name, lvl, hp, at, df, exp)
        self.charged = False        ## we'll change this to True when the character charges
        self.shields = 0            ## if the character protect himself/herself, we'll change this number (this number decreases each time the character is attacked)


    def recover(self, recoverypts):
        ''' recover the current character's HP by recoverypts UP TO the max'''
        self.hp += recoverypts
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def fullheal(self):
        self.hp = self.maxhp

    def shield(self):
        self.shields = 3        ## Note, a variable and a function CANNOT have the same name

    def decr_shield(self):
        self.shields -= 1

    def charge(self):
        self.charged = True



    def attack(self, other):
        print(other.name, "'s HP was ", other.hp, sep = "")
        print(self.name, "'s AT is ", self.at, sep = "")
        print(other.name, "'s DF is ", other.df, sep="")
        print(self.name, " attacked ", other.name, ".", sep = "")
        if self.charged:
            if (2.5 * self.at) > other.df:
                other.sethp(other.hp - (2.5 * self.at - other.df))
            else:
                print(self.name, 'is too weak.')
            self.charged = False
        else:
            if self.at > other.df:
                other.sethp(other.hp - (self.at - other.df))
            else:
                print(self.name, 'is too weak.')
        print(other.name, "'s HP is now ", other.hp, sep="")



mario = MajorCharacter('Mario')
luigi = MajorCharacter('Luigi', df = 1)

mario.attack(luigi)
mario.charge()
mario.attack(luigi)
mario.attack(luigi)