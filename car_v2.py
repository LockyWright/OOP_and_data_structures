class Car:
    def __init__(self, colour, speed):
        self.colour = colour
        self.speed = speed
    def accelerate(self):
        self.speed +=10
    def brake(self):
        self.speed -=10
    def describe(self):
        print("A", self.colour, "car going", self.speed,"mph")

car1 = Car("blue", 20)
print(car1.speed) #should print 20

car1.accelerate()
print(car1.speed) #should print 30

car1.brake()
print(car1.speed) #should print 20

car1.describe() #should print "A blue car going 20mph"