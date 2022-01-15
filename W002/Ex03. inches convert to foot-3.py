def intoft(inches):
    ft = inches //12
    inch = inches % 12
    ftinch = str(ft) + "'" + str(inch) + '"'
    return ftinch

inches = eval (input ('How tall are you ? (Enter inches) '))
print ('You are',intoft(inches),'tall')
print(inches,'inches is',intoft(inches),'foot')