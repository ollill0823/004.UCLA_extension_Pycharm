x1= eval(input('give x1: '))
y1= eval(input('give y1: '))
x2= eval(input('give x2: '))
y2= eval(input('give y2: '))

def f(w,x,y,z):
  if abs(w-y)==0:
    distance = ((w - y) ** 2 + (x - z) ** 2) ** 0.5
    print('The slope is infinity and the distance is ', distance)
  else:
    slope= (z-x)/((y-w))
    distance = ((w - y) ** 2 + (x - z) ** 2) ** 0.5
    print('The slope is ', slope, ' and the distance is ', distance)

a= f(x1,y1,x2,y2)





