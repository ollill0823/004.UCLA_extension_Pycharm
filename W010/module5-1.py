'''
File Name: module5.py
Agenda
1. Individual Programming 4
2. String Pattern Matching
3. HTML Parser
4. Beautiful Soup
'''

"""
class Character:
    def __init__(self, name, lvl=1, hp=100, at=25, df=1, exp=1):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.at = at
        self.df = df
        self.exp = exp
        self.maxhp = hp

    def rename(self, name):
        '''rename characters'''
        self.name = name

    def setlvl(self, lvl):
        '''set character level to lvl'''
        self.lvl = lvl

    def sethp(self, hp):                    ## Between char1.sethp() and char1.hp, sethp() checks to make sure we don't have negative hp.
        '''set character hp to hp, checking for int'''
        if hp <= 0:
            self.hp = 0
        else:
            try:
                self.hp = int(hp)           ## HP = 15.0 will become HP = 15
            except:
                self.hp = hp                ## HP = 15.5 will remain HP = 15.5

    def setat(self, at):
        '''set character attack to at'''
        self.at = at

    def setdf(self, df):
        '''set character defense to df'''
        self.df = df

    def setexp(self, exp):
        '''set character experience to exp'''
        self.exp = exp

    def getname(self):
        '''return the name'''
        return self.name

    def getlvl(self):
        '''return the level'''
        return self.lvl

    def getat(self):
        '''return the attack point'''
        return self.at

    def getdf(self):
       '''return the defense point'''
       return self.df

    def gethp(self):
        '''return the HP'''
        return self.hp

    def getexp(self):
        '''return the experience point'''
        return self.exp

    def attack(self, other):
        ''' decrements other's HP and prints statements '''
        other.sethp(other.gethp() - self.getat() - other.getdf())
        print(self.getname(), " attacked ", other.getname(), ". ", self.getname(), "'s HP is ", self.gethp(), "/", self.maxhp,
              ". ", other.getname(), "'s HP is ", other.gethp(), "/", other.maxhp, ". ", sep = "")
        if other.gethp() == 0:
            print(other.getname(), "has been defeated.")



class MajorCharacter(Character):
    def __init__(self, name, lvl=1, hp=100, at=10, df=1, exp = 1):
        Character.__init__(self, name, lvl, hp, at, df)
        self.charged = False
        self.shielded = 0

    def sethp(self, hp):
        '''set character hp to hp, checking for int'''

        ##if the character is shielded, then don't do anything to the hp, instead decrease the shield by 1
        if self.shielded > 0:
            self.shielded -= 1
        else:
            if hp <= 0:
                self.hp = 0
            else:
                try:
                    self.hp = int(hp)
                except:
                    self.hp = hp

    def recover(self, points):
        '''recover the current character's HP by points'''
        if (self.hp + points) >= self.maxhp:
            self.sethp(self.maxhp)
        else:
            self.sethp(self.hp + points)
        print(self.name, "'s HP has been fully restored to", self.hp, "/", self.maxhp, sep="")

    def fullheal(self):
        '''recovers the current character's HP to the max HP'''
        self.sethp(self.maxhp)
        print(self.name, "'s HP has been fully restored (", self.hp, "/", self.maxhp, ")", sep = "")

    def shield(self):
        '''reset the number of protects back to three'''
        self.shielded = 3
        print(self.getname(), "is safe from the next 3 attacks.")

    def charge(self):
        self.charged = True
        print(self.getname(), "charged.")

    def attack(self, other):
        ''' not considering defense, subtract the other's HP by my AT '''
        if self.charged:
            other.sethp(other.hp - self.at*2.5 + other.df)      ## attack considering charged status
            self.charged = False                                ## reset charged back to False
        else:
            other.sethp(other.hp - self.at + other.df)          ## otherwise, attack as usual
        print(self.getname(), " attacked ", other.getname(), ". ", self.getname(), "'s HP is ", self.hp, "/", self.maxhp,
              ". ", other.getname(), "'s HP is ", other.hp, "/", other.maxhp, ". ", sep = "")
        if other.gethp() == 0:
            print(other.getname(), "has been defeated.")



class Minion(Character):
    def __init__(self, name, lvl=1, hp=100, at=25, df=1, exp=1):
        Character.__init__(self, name, lvl, hp, at, df)

class Boss(Character):
    def __init__(self, name, lvl=1, hp=100, at=25, df=1, exp=1):
        Character.__init__(self, name, lvl, hp, at, df)

    def spawn(self, name = "Minion"):
        '''spawns minion with attack equal to 1/4 of the Boss's max. Same level, but no exp and no def'''
        newminion = Minion(name, lvl = self.lvl, hp = self.maxhp//4, at = self.at//4, df = 0, exp = 0)
        print("Boss spawned ", name, " (HP ", newminion.gethp(), ", AT ", newminion.getat(), ", DF ", newminion.getdf(), ")", sep = "")
        return newminion


##### Gameplay #####

playerlist = []
minionlist = []


## Get a number of players
invalidNum = True
while invalidNum:
    try:
        numplayers = int(input("How many players? "))
        if numplayers > 0:
            invalidNum = False
    except:
        pass

## Obtain player names and create the players (MajorCharacter)
for i in range(numplayers):
    playername = input("Player " + str(i+1) + " Name: ")
    playerlist.append(MajorCharacter(playername, lvl = 1, hp = 100, at = 10, df = 5, exp = 0))

## Create a Boss
boss = Boss('Boss', lvl = 1, hp = numplayers * 20, at = 100, df = 0, exp = 0)


ingame = True
## while loop for the game
while ingame:
    ## Boss spawns minion
    minionlist.append(boss.spawn())

    ## Players' turn (for loop)
    for player in playerlist:
        print('1. Attack\n2. Charge\n3. Shield')
        selection = '0'
        while selection != '1' and selection != '2' and selection != '3':
            selection = input(player.getname() + ', what would you like to do?')

        ## 1. Attack
        if selection == '1':
            ## Minions are alive, so player can only attack minions
            if len(minionlist) > 0:
                ## print out minion list
                for j in range(len(minionlist)):
                    print(str(j+1) + ". " + minionlist[j].getname() + " (HP " , minionlist[j].gethp() , ")", sep = "")
                attmin = int(input(player.getname() + ', who would you like to attack?'))
                ## check to make sure the player is only attacking a valid numbered minion

                player.attack(minionlist[attmin - 1])

                ## check attacked minion's status (still alive?)
                if minionlist[attmin - 1].gethp() <= 0:
                    minionlist.remove(minionlist[attmin - 1])


            ## Minions are all gone, so player can attack the boss
            else:
                player.attack(boss)

                ## Check if Boss is dead (end game -- win)
                if boss.gethp() <= 0:
                    ingame = False
                    print('You win!')

        ## 2. Charge
        elif selection == '2':
            player.charge()

        ## 3. Shield
        elif selection == '3':
            player.shield()

    ## Minions' turn (for loop)
    for minion in minionlist:
        minion.attack(playerlist[0])
        if playerlist[0].gethp() <= 0:
            playerlist.remove(playerlist[0])
        ## Check if players are gone (end game -- lose)
        if len(playerlist) == 0:
            ingame = False
            print('You lose!')
            break
            
"""

##### String Pattern Matching #####
"""
from re import findall

## find exactly the work 'clack' in a lengthy string
print(findall('clack', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## find any word with one character (except a new line character) between cl and ck
print(findall('cl.ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## find any word with two characters (except a new line character) between cl and ck
print(findall('cl..ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck cleack'))


## find any string with 0 or more repetitions of the previous character
print(findall('cla*ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## find any string with 1 or more repetitions of the previous character
print(findall('cla+ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## find any string with 0 or 1 of the previous character
print(findall('cla?ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))


## either i or a between cl_ck
print(findall('cl[ia]ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## letter g through z between cl_ck
print(findall('cl[g-z]ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## letter (a through e or s through z) between cl_ck
print(findall('cl[a-es-z]ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## combining concepts
print(findall('cl[a-es-z]*ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck cluuck'))
print(findall('cl[a-es-z]+ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck cluuck'))


## anything EXCEPT i or a between cl_ck
print(findall('cl[^ia]ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))

## ^ EXCEPT
print(findall('cl[^g-z]ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))
print(findall('cl[^a-es-z]ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))



## | or
print(findall('clack|quack', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))
print(findall('a+|0+|z+', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))
print(findall('cl+|qu+', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))
print(findall('cl+|qu[ia]ck', 'click clack cluck claack claaack croak cr0000ak cricket quack cl ck clck'))      ## looking for cl, cll, clll, ..., quick, or quack

"""


##### urllib.request #####

"""
from re import findall
from urllib.request import urlopen

response = urlopen('https://en.wikipedia.org/wiki/Los_Angeles')

html = response.read()
##print(type(html))
##print(html)

html = html.decode()
##print(type(html))
##print(html)

print(html.count('Angels') + html.count('angels'))

print(findall('Wiki[A-z]edia', html))
"""

"""
from urllib.request import urlopen

response = urlopen('https://www.classicshorts.com/stories/aos.html')
html = response.read()
html = html.decode()            ## one line version: html = response.read().decode()
print(html.count('<div class="StoryPara">'))
"""


"""
from urllib.request import urlopen

def countInstances(url, keyword):
    ''' access a given url and count how many times a keyword shows up in the HTML '''
    response = urlopen(url)
    html = response.read().decode()
    return html.count(keyword)

print(countInstances('https://www.classicshorts.com/stories/aos.html', '<div class="StoryPara">'))
print(countInstances('https://en.wikipedia.org/wiki/Los_Angeles', 'Angels'))
"""


"""
from html.parser import HTMLParser
from urllib.request import urlopen

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        ' print value of href attribute if any '        ## the link behind href
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

response = urlopen('https://www.classicshorts.com/stories/aos.html')
html = response.read().decode()
parser = LinkParser()
parser.feed(html)
"""



"""
from html.parser import HTMLParser
from urllib.request import urlopen

class StoryParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        ' print value of href attribute if any '        ## the link behind href
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])
    def handle_data(self, data):
        ' create a story file to save data'
        storyfile = open('aos.txt', 'a')            ## Every time we come across new data, we don't want to overwrite existing data
        storyfile.write(data + '\n')
        storyfile.close()


response = urlopen('https://www.classicshorts.com/stories/aos.html')
html = response.read().decode()
parser = StoryParser()
parser.feed(html)
"""

"""
from html.parser import HTMLParser
from urllib.request import urlopen

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        ' print value of href attribute if any '        ## the link behind href
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    term = attr[1].replace('https://www.coolkidfacts.com/', '')
                    term = term.replace('facts-for-kids','')
                    term = term.replace('facts', '')
                    term = term.replace('for-kids','')
                    term = term.replace('facts', '')
                    term = term.replace('-/', '')
                    term = term.replace('/', '')
                    term = term.replace('-', ' ')
                    animals = open('animal.txt', 'a')
                    animals.write(term + '\n')
                    animals.close()

response = urlopen('https://www.coolkidfacts.com/animals/')
html = response.read().decode()
parser = LinkParser()
parser.feed(html)

animals = open('animal.txt', 'r')
animaltext = animals.readlines()
animals.close()

print(animaltext[70:90])
"""


########## Beautiful Soup ##########
## For those looking to do more web-scraping, I highly recommend Beautiful Soup
## You will need to install it
## Option 1: File >> Settings >> Project >> Project Interpreter >> "+" on the right side >> look for beautifulsoup4 >> install package
## Option 2: type       pip install beautifulsoup4          in the terminal (on bottom of screen)


"""
## Print out a short story


from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.classicshorts.com/stories/aos.html')
soup = BeautifulSoup(response, 'html.parser')

## Example 1 <div class = "StoryPara">
story = soup.findAll('div', attrs = {'class': 'StoryPara'})         ##findAll() is part of BeautifulSoup (we're not using the re findall from earlier)
print(type(story))
for para in story:
    print(para.text)

## Example 2 <div> with any attr
story2 = soup.findAll('div')
for para in story2:
    print(para.text)
"""

"""
## Write short story into a file

from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.classicshorts.com/stories/aos.html')
soup = BeautifulSoup(response, 'html.parser')

story = soup.findAll('div', attrs = {'class': 'StoryPara'})         ##findAll() is part of BeautifulSoup (we're not using the re findall from earlier)
storyfile = open('newstory.txt', 'w')
for para in story:
    storyfile.write(para.text)
    storyfile.write('\n')
storyfile.close()
"""

"""
## Example using the a tag

from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.coolkidfacts.com/animals/')
soup = BeautifulSoup(response, 'html.parser')

atag = soup.findAll('a')
for tag in atag:
    print(tag.text)         ## text associated with tag a
"""

"""
## Example using the a tag

from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.coolkidfacts.com/animals/')
soup = BeautifulSoup(response, 'html.parser')

atag = soup.findAll('a')
for tag in atag:
    print(tag.get('href'))
"""


"""

## FINAL ASSIGNMENT HINT!
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.classicshorts.com/stories/aos.html')
soup = BeautifulSoup(response, 'html.parser')

atag = soup.findAll('a')
for tag in atag:
    print(tag.text)
"""

## FINAL ASSIGNMENT HINT!
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.classicshorts.com/stories/aos.html')
soup = BeautifulSoup(response, 'html.parser')

atag = soup.findAll('a')
for tag in atag:
    if "dictionary" in tag.get('href'):
        print(tag.get('href'))
    ##print(tag.get('href').replace("http://dictionary.reference.com/browse/", ""))     ## give me vocab list only