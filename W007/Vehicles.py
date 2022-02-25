class Seat:
    def __init__(self):
        'initializes the seat and seat variables'
        self.status = "vacant"

    def occupy(self):
        'makes the seat status occupied'
        self.status = "occupied"

    def vacate(self):
        'makes the seat status to vacant'
        self.status = "vacant"

    def getstatus(self):
        'returns whether the seat is occupied or vacant'
        return self.status


class Vehicle:
    'Represents a drive-able vehicle'

    def __init__(self, color, make, model, wheels=4, year=2000, seats=5):
        'initializes the vehicle and vehicle variables'
        self.color = color
        self.wheels = wheels
        self.make = make
        self.model = model
        self.year = year
        self.fuel = 0
        self.driverseat = Seat()
        self.seats = []
        for i in range(seats - 1):
            self.seats.append(Seat())


    def getseat(self, num):
        'returns the status of the seat'
        return self.seats[num].getstatus()


hisCar = Vehicle('green', 'Honda', 'Accord')
print(hisCar.getseat(2))


















