a = input('What is your full name? ')
b = eval(input('What year did you start programming? '))  ##eval 計算值
yrsexp = 2020 - b     ## error, b is not a number (float, int)
print(a, 'has', yrsexp, 'years experience programming.')