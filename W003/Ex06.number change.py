number= eval(input('give a number: '))


def f(n):
  hundred= n//100
  tendigit=(n-hundred*100)//10
  singledigit=n-hundred*100-tendigit*10
  return singledigit*100+tendigit*10+hundred

print(f(number))
