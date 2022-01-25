x1 = eval(input('x1: '))
y1 = eval(input('y1: '))
r1 = eval(input('r1: '))
x2 =eval( input('x2: '))
y2 = eval(input('y2: '))
r2 =eval( input('r2: '))

def f(a,b,c,d,e,f):
  distance=((a-d)**2+(b-e)**2)**0.5
  rgap=c+f
  if distance<rgap:
    return True
  else:
    return False
z=f(x1,y1,r1,x2,y2,r2)
print(z)

