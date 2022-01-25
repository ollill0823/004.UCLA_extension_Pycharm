money = eval(input('Your hourly salary: '))
hour = eval(input('How many hours do you weekly work: '))

def f(x,y):
  if y<40:
    return x*y
  else:
    return 40*x+ 1.5*(y-40)*x
print(f(money,hour))
