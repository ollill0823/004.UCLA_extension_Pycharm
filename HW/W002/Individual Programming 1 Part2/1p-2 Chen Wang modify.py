###
# name = Chen Wang
# date = 2022/01/15
#  assignment title = ip1 part2 modify.py
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
category = input ('What category of things should we store? ' ) # define a category
var1 = input ( category + ' 1: ')  # list 5 item is related to category
var2 = input ( category + ' 2: ')
var3 = input ( category + ' 3: ')
var4 = input ( category + ' 4: ')
var5 = input ( category + ' 5: ')
print('')


pick = eval (input ( 'Pick a number between 1 and 5: '))

def list (var1, var2, var3, var4, var5):
      return [ 'var1' +'' + 'var2', +'' + 'var3', +'' + 'var4', +'' + 'var5' ]
varlist = [ var1, var2, var3, var4, var5 ]
sorted_list = sorted (varlist)    # re-defined new item sorted_list; did not replace varlist
# pick a number and based on the number to choose the right order of item
if pick == 1:
      print ( 'You picked', str(sorted_list[0]) + '!\n' )
elif pick == 2:
      print ( 'You picked', str(sorted_list[1]) + '!\n' )
elif pick == 3:
      print ( 'You picked', str(sorted_list[2]) + '!\n' )
elif pick == 4:
      print ( 'You picked', str(sorted_list[3]) + '!\n' )
else :
      print ( 'You picked', str(sorted_list[4]) + '!\n' )


print ('The sorted list is:' )
print ( sorted_list  )
print ( '' )

character = input ('Pick a character: ')
incheck1 = character in sorted_list[0]
incheck2 = character in sorted_list[1]
incheck3 = character in sorted_list[2]
incheck4 = character in sorted_list[3]
incheck5 = character in sorted_list[4]
checklist =[ incheck1, incheck2, incheck3, incheck4, incheck5]
print(checklist)

