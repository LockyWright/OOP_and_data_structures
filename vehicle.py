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
    def __init__(self, colour, speed):
        super().__init__(colour, speed)
        self.num_wheels = 4
    def describe(self):
        print("A", self.colour, "car with", self.num_wheels, "wheels going", self.speed, "mph")

class Bike(Vehicle):
    def __init__(self, colour, speed):
        super().__init__(colour, speed)
        self.num_wheels = 2
    def describe(self):
        print("A", self.colour, "bike with", self.num_wheels, "wheels going", self.speed,"mph")

car1 = Car("red", 0)
bike1 = Bike("green", 0)

car1.accelerate()
car1.describe() #10 mph
bike1.describe() #0 mph