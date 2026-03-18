class Vehicle:
    def __init__(self, colour, speed):
        self.colour = colour
        self.speed = speed
    def accelerate(self):
        self.speed +=10
    def brake(self):
        self.speed -=10
    def describe(self):
        print("A", self.colour, "vehicle going", self.speed,"mph")

class Car(Vehicle):
    def describe(self):
        print("A", self.colour, "car going", self.speed,"mph")

class Bike(Vehicle):
    def describe(self):
        print("A", self.colour, "bike going", self.speed,"mph")

v1 = Vehicle("white", 0)
car1 = Car("red", 30)
bike1 = Bike("green", 10)

car1.accelerate()
bike1.accelerate()
bike1.accelerate()

v1.describe() #0 mph
car1.describe() #40 mph
bike1.describe() #30 mph < a fast bike!