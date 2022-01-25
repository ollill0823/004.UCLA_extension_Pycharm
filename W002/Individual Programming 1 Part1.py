'''  Individual Programming 1-assignment
example is as below
Person 1 Height: 64
Person 2 Height: 61
64 - 61 = 3
Person 1 is 3 inches taller than Person 2.
Person 1 is 5'4"
Person 2 is 5'1"

Person 1 Height: 65
Person 2 Height: 65
65 - 65 = 0
Person 1 is 0 inches taller than Person 2.
Person 1 is 5'5"
Person 2 is 5'5"

Person 1 Height: 68
Person 2 Height: 70
68 - 70 = -2
Person 1 is -2 inches taller than Person 2.
Person 1 is 5'8"
Person 2 is 5'10"
'''
def intoft(inches):
    foot = inches // 12
    inch = inches % 12
    ftin =  str(foot) + "'" + str(inch) + '"'
    return ftin    # input inches and convert to inches

var1= eval (input ( 'Person 1 Height: ')) # input person 1 height to int
var2= eval (input ( 'Person 2 Height: ')) #input person 2 height to int
var3 = var1 - var2   # calculate person 1 and person 2's gap

print ( var1, '-', var2, '=', var3 )
print ( 'Person 1 is', var3, 'inches taller than Person 2.' )
var1ftin = intoft(var1)
var2ftin = intoft(var2)

print ( 'Person 1 is', var1ftin )
print ( 'Person 2 is', var2ftin )