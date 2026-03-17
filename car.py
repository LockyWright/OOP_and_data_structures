class Car:
    def __init__(self, colour, speed):
        self.colour = colour
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

car1 = Car("red", 0)
car2 = Car("blue", 30)

car1.accelerate()
print(car1.speed) #should print 10

car2.brake()
print(car2.speed) #should print 20