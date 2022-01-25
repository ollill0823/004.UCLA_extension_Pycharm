'''
##### Example 1 #####
Let's create a list of 5 things. Think of a general category.
What category of things should we store? Animals
Animals 1: cat
Animals 2: dog
Animals 3: bird
Animals 4: snake
Animals 5: hamster

Pick a number between 1 and 5: 3
You picked dog!

The sorted list is:
['bird', 'cat', 'dog', 'hamster', 'snake']

Pick a character: a
[False, True, False, True, True]



##### Example 2 #####
Let's create a list of 5 things. Think of a general category.
What category of things should we store? Vegetable
Vegetable 1: peas
Vegetable 2: cauliflower
Vegetable 3: cabbage
Vegetable 4: broccoli
Vegetable 5: carrot

Pick a number between 1 and 5: 2
You picked cabbage!

The sorted list is:
['broccoli', 'cabbage', 'carrot', 'cauliflower', 'peas']

Pick a character: abc         ## If the user enters more than one character, it will search the whole string
[False, False, False, False, False]



##### Example 3 #####
Let's create a list of 5 things. Think of a general category.
What category of things should we store? color
color 1: purple
color 2: blue
color 3: red
color 4: yellow
color 5: green

Pick a number between 1 and 5: 5
You picked yellow!

The sorted list is:
['blue', 'green', 'purple', 'red', 'yellow']

Pick a character: e
[True, True, True, True, True]



##### Example 4 #####
Let's create a list of 5 things. Think of a general category.
What category of things should we store? number
number 1: 123
number 2: 1
number 3: 456
number 4: 3
number 5: 7

Pick a number between 1 and 5: 4
You picked 456!

The sorted list is:
['1', '123', '3', '456', '7']

Pick a character: $
[False, False, False, False, False]
'''
print ( "Let\'s create a list of 5 things. Think of a general category.")
store = input ('What category of things should we store? ' )
var1 = input ( store + ' 1: ')
var2 = input ( store + ' 2: ')
var3 = input ( store + ' 3: ')
var4 = input ( store + ' 4: ')
var5 = input ( store + ' 5: ')
print('')


pick = eval (input ( 'Pick a number between 1 and 5: '))

def list (var1, var2, var3, var4, var5):
      return [ 'var1' +'' + 'var2', +'' + 'var3', +'' + 'var4', +'' + 'var5' ]  #lst = [int(num) for num in input().split()]  print(lst)
var6 = [ var1, var2, var3, var4, var5 ]
var6.sort()   #sorted_list = sorted(list_name)

if pick == 1:
      print ( 'You picked', str(var6[0]) + '!\n' )
elif pick == 2:
      print ( 'You picked', str(var6[1]) + '!\n' )
elif pick == 3:
      print ( 'You picked', str(var6[2]) + '!\n' )
elif pick == 4:
      print ( 'You picked', str(var6[3]) + '!\n' )
else :
      print ( 'You picked', str(var6[4]) + '!\n' )


print ('The sorted list is:' )
print ( var6  )
print ( '' )

character = input ('Pick a character: ')
check1 = character in var6[0]
check2 = character in var6[1]
check3 = character in var6[2]
check4 = character in var6[3]
check5 = character in var6[4]
checklist =[ check1, check2, check3, check4, check5]
print(checklist)