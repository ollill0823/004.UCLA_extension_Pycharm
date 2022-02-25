def koch(n):
    if n==0:
        return 'F'
    else:
        tmp= koch(n-1)
        return tmp+'L' + tmp + 'R' + tmp + 'L' + tmp

from turtle import Screen, Turtle
def draw(n):

    s=Screen()
    t=Turtle()
    directions = koch(n)

    for i in directions:
        if i =='F':
            t.forward(300/3**n)
        elif i =='L':
            t.lt(60)
        elif i =='R':
            t.rt(120)
    s.bye()

draw(3)












