def koch(n):
    if n==0:
        return 'F'
    else:
        tmp= koch(n-1)
        return tmp+'L' + tmp + 'R' + tmp + 'L' + tmp


from turtle import *
def draw(n):

    s=Screen()
    directions = koch(n)

    color("red", "cyan")
    begin_fill()
    for j in range(3):
        for i in directions:
            if i == 'F':
                forward(300 / 3 ** n)
            elif i == 'L':
                lt(60)
            elif i == 'R':
                rt(120)
        rt(120)
    end_fill()
    done()


draw(2)












