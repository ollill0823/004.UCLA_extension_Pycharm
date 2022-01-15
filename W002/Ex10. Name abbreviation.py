## Scenario : write a function that takes in 2 or 3 times (last , first, middle)
## Your function should return a string with the first name and last name printed in order
## if there is a middle name, print just the initial followed with a period
## ex. C. Wang
def firstmlast (first, last, middle = None):
    if middle == None :
        return first + ' ' +  last
    else :
        return first +' ' + middle[0] + '.' +  last
    
print (firstmlast('Chen','Wang'))
print (firstmlast('Meng','Chieh','Chan'))
print (firstmlast(last ='Bing', middle = 'Muriel', first = 'Chandler' ))
print('Green','Blue','Yellow','Red')