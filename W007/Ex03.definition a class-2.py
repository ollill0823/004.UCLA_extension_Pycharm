class Point:

    def __init__(self, x, y):
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
check.setx(6)
print(check.get())
check.move(5, 8)
print(check.get())

print(check.getx())

print(dir(check))