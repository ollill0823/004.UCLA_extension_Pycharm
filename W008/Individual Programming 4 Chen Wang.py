'''
File Name: Individual Programming 4 Chen Wang.py

Agenda
1. Define class:
    1a : Define Character
    1b : Define MajorCharacter
    1c : Define Boss
    1d : Define Minion
2. follow the order to complete each turn action: Boss --> Players --> Minion
    2a : Boss's action
    2b : Players' action
    2c : Minions' action
3. condition check if need to end game or game over
    3a : finish this turn actions
    3b : Game over : no left players
    3c : End game : Boss's hp ==0

'''

# step 1a : Define class Character: include basic role information
class Character:
    def __init__(self, name, level=1, hp=100, at=10, df=5, exp=0):
        ''' initializes the character's name, level (lvl), health points (hp), attack level (at), defense level (df),
       and experience (exp)'''
        self.name = name
        self.level = level
        self.hp = hp
        self.at = at
        self.df = df
        self.exp = exp
        self.maxhp = hp

    def setlvl(self, level):
        'sets the level'
        self.level = level

    def sethp(self, hp):
        'sets the hp'
        self.hp = hp

    def setat(self, at):
        'set the attack level'
        self.at = at

    def setdf(self, df):
        'set the defense level'
        self.df = df

    def setexp(self, exp):
        'set the exp'
        self.exp = exp

    def getname(self):
        'return the name'
        return self.name

    def getlvl(self):
        'return the level'
        return self.level

    def gethp(self):
        'return the health point'
        return int(self.hp)

    def getat(self):
        'return the attack level'
        return self.at

    def getdf(self):
        'return the defense level'
        return self.df

    def getexp(self):
        'return the exp'
        return self.exp

# step 1b : Define class MajorCharacter: inherit from Character, but include specified skill
class MajorCharacter(Character):
    '''initializes the main character\'s name, level (lvl), health points (hp), attack level (at), defense level (df),
    and experience(exp)'''
    def __init__(self, name, level=1, hp=100, at=10, df=5, exp=0):
        Character.__init__(self, name, level, hp, at, df, exp)
        self.shieldcount = 0
        self.maxshield = 3
        self.charged = False
        self.turnon = False

    def recover(self, recoverhp):
        'recover the hp'
        if self.hp + recoverhp >= self.maxhp:
            self.hp = self.maxhp
        else:
            self.hp += recoverhp
        print('{var1}\'s Hp has been restored to {var3}/{var5}.'.format(var1=self.getname(), var3=self.gethp(),
                                                                        var5=self.maxhp))

    def fullheal(self):
        'recover the hp to maximum hp'
        self.hp += self.maxhp

    def shield(self):
        'turn on the complete defense three times'
        self.shieldcount = 0
        self.turnon = True

    def charge(self):
        'open the critical shot button (next turn action can attack)'
        self.charged = True

    def getcharge(self):
        'return the critical shot status'
        return self.charged

    def attack(self, other):
        'Based on different situation, provide different attacks: 1.normal 2.Critical shot(X2.5) 3. shield defense'
        if other.turnon == False:
            if self.charged == True:
                if other.hp > (self.at * 2.5) - other.df:
                    if (2.5 * self.at) > other.df:
                        other.sethp(other.hp - (2.5 * self.at - other.df))
                        print(
                            '{var1} attacked {var2}. {var1}\'s HP is {var3}/{var5}. {var2}\'s HP is {var4}/{var6}.'.format(
                                var1=self.getname(), var2=other.getname(), var3=self.gethp(), var4=other.gethp(),
                                var5=self.maxhp, var6=other.maxhp))

                    else:
                        print(self.name, 'is too weak.')
                    self.charged = False
                else:
                    other.sethp(0)
                    print(
                        '{var1} attacked {var2}. {var1}\'s HP is {var3}/{var5}. {var2}\'s HP is {var4}/{var6}.'.format(
                            var1=self.getname(), var2=other.getname(), var3=self.gethp(), var4=other.gethp(),
                            var5=self.maxhp, var6=other.maxhp))
                    print('{} has been defeated.'.format(other.name))
            else:
                if other.hp > self.at - other.df:
                    if self.at > other.df:
                        other.sethp(other.hp - (self.at - other.df))
                    else:
                        print(self.name, 'is too weak.')
                    print(
                        '{var1} attacked {var2}. {var1}\'s HP is {var3}/{var5}. {var2}\'s HP is {var4}/{var6}.'.format(
                            var1=self.getname(), var2=other.getname(), var3=self.gethp(), var4=other.gethp(),
                            var5=self.maxhp, var6=other.maxhp))
                else:
                    other.sethp(0)
                    print(
                        '{var1} attacked {var2}. {var1}\'s HP is {var3}/{var5}. {var2}\'s HP is \033[91m\033[1m{var4}\033[0m/{var6}.'.format(
                            var1=self.getname(), var2=other.getname(), var3=self.gethp(), var4=other.gethp(),
                            var5=self.maxhp, var6=other.maxhp))
                    print('{} has been defeated.'.format(other.name))
        elif other.turnon == True:
            print(
                '{var1} attacked {var2}. {var1}\'s HP is {var3}/{var5}. {var2}\'s HP is {var4}/{var6}.'.format(
                    var1=self.getname(), var2=other.getname(), var3=self.gethp(), var4=other.hp,
                    var5=self.maxhp, var6=other.maxhp))
            other.shieldcount +=1
            if other.shieldcount == other.maxshield:
                other.turnon = False

# step 1c : Define class Boss: inherit from MajorCharacter, storage Boss's information and spawn skill(unique)
class Boss(MajorCharacter):
    " initialize Boss's life status"
    def __init__(self, name='Boss', hp=20):
        Character.__init__(self, name, hp)
        self.hp = number*hp
        self.at = 25
        self.df = 0
        self.exp = 0
        self.maxhp=number * hp
        self.turnon = False

    def spawn(self):
        ' spawn a new baby that attack players'
        master_blood = int(round(self.maxhp * 0.25, 0))
        newminion = Minion('Minion', master_blood)
        print('Boss spawned Minion (HP {}, AT {}, DF {})'.format(master_blood, newminion.at, newminion.df))
        return newminion

# step 1d : Define class Minion: inherit from Boss, storage Minions' information only
class Minion(Boss):
    " initialize master's life status"
    def __init__(self, name = 'Minion', hp=5):
        Boss.__init__(self, name, hp)
        self.hp = hp
        self.maxhp = hp
        self.shieldcount = 0
        self.maxshield = 3


# step 2 : input players information
number = int(input ('How many players? '))
players = []
for i in range(number):
    askname = input ('Player {} Name: '.format(i+1))
    newplayer = MajorCharacter(askname)
    players.append(newplayer)

# step 2a: Boss's action
##  input Boss and invader's  information
Putin= Boss()
##  create list to storage invaders
Xi_group=[]
while Putin.gethp() >0 :
    ## step 2a: Boss's skill
    BLR=Putin.spawn()
    Xi_group.append(BLR)

    # step 2b players's fight detail
    ### fight detail: player's turn action
    for UKR in players:
        ### step 2b.1 check Boss's Hp, if 0 then game over(win)
        if Putin.gethp() == 0:
            break
        else:
            YesorNoCheck = True
            while YesorNoCheck:
                try:
                    ### step 2b.2 : give options (Attack/Charge/Shield) for players to choose an action
                    print('\033[94m\033[1m1. Attack\n2. Charge\n3. Shield\033[0m')
                    action = int(input('{}, what would you like to do? '.format(UKR.getname())))
                    ### step 2b.3 : based on the choose the players choose to develop the detail
                    #### 1.Attack: normal attack, but can choose anyone to attack(except boss)
                    if action == 1:
                        YesorNoCheck = False
                        if len(Xi_group) >= 1:
                            AttackCheck = True
                            ItemCheck = []
                            while AttackCheck:
                                try:
                                    for item in range(len(Xi_group)):
                                        print('{}. Minion (HP {})'.format(item + 1, Xi_group[item].gethp()))
                                        ItemCheck.append(item + 1)
                                    option = int(input('{}, who would you like to attack? '.format(UKR.getname())))
                                    if option in ItemCheck:
                                        AttackCheck = False
                                    else:
                                        print('Invalid input.')
                                except ValueError:
                                    print("Invalid input. Please enter again.")
                            for attacker in range(len(Xi_group)):
                                if (option - 1) == attacker:
                                    UKR.attack(Xi_group[attacker])
                            for people in Xi_group:
                                if people.hp == 0:
                                    Xi_group.remove(people)
                        else:
                            print('1. Boss (HP {})'.format(Putin.gethp()))
                            UKR.attack(Putin)
                    ### step 2b.3 :
                    #### 2.charge: the next turn actions players will give a crtitical shot to specified invaders
                    #### (this turn action will do nothing)
                    elif action == 2:
                        YesorNoCheck = False
                        UKR.charge()
                        print('{} charged.'.format(UKR.getname()))
                    ### step 2b.3 :
                    #### 3.shield: allow to be attacked free from invaders for three times
                    elif action == 3:
                        YesorNoCheck = False
                        UKR.shield()
                        print('{} is safe from the next 3 attacks.'.format(UKR.getname()))
                    ### step 2b.3 :
                    #### mistake Proofing 1: if players provides with not 1 or 2 or 3 (number), give players to re-choose again)
                    else:
                        print('\033[91m\033[1mInvalid input.\033[0m')
                ### step 2b.3 :
                #### mistake Proofing 2: if players provides with not 1 or 2 or 3 (non number), give players to re-choose again)
                except ValueError:
                    print("\033[91m\033[1mThat's not an integer 1 or 2 or 3. Please enter again.\033[0m")

    ## step 2c : fight detail: invader and Boss's turn action
    for invaders in Xi_group:
        invaders.charged = False
        ### invaders attack players from the reverse order
        for defender in range(len(players) - 1, -1, -1):
            invaders.attack(players[defender])
            if players[defender].hp == 0:
                players.remove(players[defender])
            break

    ## step 3 : final check status
    ## step 3a : no find Minion --> return no minions was found
    if Putin.hp > 0 and len(Xi_group) == 0:
        print('There are no Minions to attack.')

    ## step 3b : no find players --> game over
    if len(players) == 0:
        print('\033[91m\033[1mYou lose.\033[0m')
        break

    ## step 3c : no find Boss --> end game
    if Putin.hp ==0:
        print('You win!')
