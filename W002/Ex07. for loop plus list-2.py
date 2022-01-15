## Combination range, but also looping through a list ####
mylist = ['milk', 'egg' , 'bananas', 'ham']
print ( 'I need the following items from the store : ' )
for i in range(len(mylist)) :  ##range(5) so 0, 1,2,3,4
    print( i + 1 , ' : ' , mylist[i], sep= ' ' )    # or print (str(i+1) + ' : ' + mylist[i])
                                               # sep = '' tells python that you don't want the default space  given at commas
