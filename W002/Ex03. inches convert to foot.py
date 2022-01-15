### Task: Ask the user for a height in inches and convert to ft-in
# 12 inches to 1 foot

def foot(inches):
   return inches//12
def inch(inches):
    return inches%12

inches = eval(input ('How tall are you ? (Enter inches) '))
f=foot(inches)
i=inch(inches)
print ('You are',f,"'",i,'" tall')   # 若要打出文字' ,需用"'". 若要打出文字", 需用'"'
print('----------------------------------')
