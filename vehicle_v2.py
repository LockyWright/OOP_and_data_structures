class Vehicle:
    def __init__(self, colour, speed):
        self.colour = colour
        self.__speed = speed
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, new_speed):
        if new_speed < 0:
            print("New speed cannot be negative")
        else:
            self.__speed = new_speed
        
    def accelerate(self):
        self.__speed += 10
    
    def brake(self):
        if self.__speed - 10 < 0:
            print("Cannot brake below zero")
        else:
            self.__speed -= 10
    
    def describe(self):
        print("A", self.colour, "vehicle going", self.__speed, "mph")

#Test scenarios below
car1 = Vehicle("red", 0)
car1.set_speed(50)
print(car1.get_speed()) #should print 50

car1.set_speed(-10)
print(car1.get_speed()) #should print "New speed cannot be negative", then revert back to 50

car1.brake()
car1.brake()
car1.brake()
car1.brake()
car1.brake()
print(car1.get_speed()) #should print 0