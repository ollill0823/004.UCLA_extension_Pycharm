class Rectangle:
    'class that represents rectangle'
    def setSize(self,width, length):
        'define width and length'
        self.w = width
        self.l = length

    def perimeter(self):
        'define the perimeter'
        return 2*(self.w + self.l)

    def area(self):
        'calculate the area of the defined width and the length'
        return self.w*self.l

x=eval(input('Give a width: '))
y=eval(input('Give a length: '))

rect=Rectangle()
rect.setSize(x,y)
print(rect.perimeter())
print(rect.area())
print(dir(rect))
print(help(rect))