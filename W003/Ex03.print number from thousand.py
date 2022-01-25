num=eval(input('Enter a number: '))


for i in range (3,-1,-1):
  r = num // (10 ** i)
  print(r)
  num = num % (10 ** i)