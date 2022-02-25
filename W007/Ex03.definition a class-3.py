class Point:

    def __init__(self, x=0, y=0):
        # define x=0, y=0 to avoid entering empty number
        self.x = x
        self.y = y

    def setx(self, xcoord):
        self.x=xcoord

    def setx(self, ycoord):
        self.y = ycoord

    def move(self,dx,dy):
        self.x +=dx
        self.y += dy

    def get(self):
        return (self.x, self.y)

    def getx(self):
        return (self.x)


check=Point(3, 2)
print(check.get())
check=Point()
print(check.get())
check=Point(2)
print(check.get())
