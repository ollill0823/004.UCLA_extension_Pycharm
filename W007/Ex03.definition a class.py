class Point:

    def setx(self, xcoord):
        self.x=xcoord

    def sety(self, ycoord):
        self.y = ycoord

    def move(self,dx,dy):
        self.x +=dx
        self.y += dy

    def get(self):
        return (self.x, self.y)

    def getx(self):
        return (self.x)


b=Point()
b.setx(5)
b.sety(2)
print(b.get())

a=Point()
a.setx(3)
a.sety(4)
print(a.get())