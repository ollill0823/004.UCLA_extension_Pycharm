class Point:

    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord

    def __repr__(self):
        return ('({}, {})'.format(self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def setx(self, xcoord):
        self.x=xcoord

    def sety(self, ycoord):
        self.y=ycoord

    def get(self):
        return (self.x,self.y)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def move(self, dx, dy):
        self.x +=dx
        self.y +=dy



a=Point(3,5)
print(a.x)