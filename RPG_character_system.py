class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.__health = health
        self.attack_power = attack_power
    
    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        self.__health = new_health
    
    def attack(self, target):
        target.set_health(target.get_health() - self.attack_power)
    
    def check_health(self):
        if self.__health <= 0:
            print(self.name, "has been KO'd!")
        else:
            print(self.name, "has", self.__health, "health remaining")
    
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=40, attack_power=20)
        self.weapon = "staff"
    def describe(self):
        print("A Mage named", self.name, "with", self.get_health(), "health, and", self.attack_power, "attack power.", self.name, "wields a", self.weapon, ".")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=50, attack_power=10)
        self.weapon = "club"
    def describe(self):
        print("A Warrior named", self.name, "with", self.get_health(), "health, and", self.attack_power, "attack power.", self.name, "wields a", self.weapon, ".")

Mage1 = Mage("Gandalf")
Warrior1 = Warrior("Heavy")

Mage1.describe()
Warrior1.describe()


Mage1.attack(Warrior1)
Warrior1.attack(Mage1)
Mage1.check_health()
Warrior1.check_health()

Mage1.attack(Warrior1)
Warrior1.attack(Mage1)
Mage1.check_health()
Warrior1.check_health()

Mage1.attack(Warrior1)
Mage1.attack(Warrior1)
Mage1.check_health()
Warrior1.check_health()