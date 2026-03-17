class Car:
    def __init__(self, colour, speed):
        self.colour = colour
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10