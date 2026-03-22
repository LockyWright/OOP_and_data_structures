class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.__health = health
        self.attack_power = attack_power

    def get_health(self):
        return self.__health
    
    def set_health(self, new_health):
        self.__health = new_health

    def health_check(self):
        if self.__health <= 0:
            print(self.name, "has been KO'd")
        else:
            print(self.name, "has", self.__health, "health remaining")
        
    def attack(self, target):
        target.set_health(target.get_health() - self.attack_power)
    
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=50, attack_power=10)
        self.weapon = "Club"
    def describe(self):
        print(self.name, "has", self.get_health(), "health, and uses a", self.weapon, "to inflict", self.attack_power, "attack power")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=40, attack_power=20)
        self.weapon = "Staff"
    def describe(self):
        print(self.name, "has", self.get_health(), "health, and uses a", self.weapon, "to inflict", self.attack_power, "attack power")

Warrior1 = Warrior("Brute")
Mage1 = Mage("Wizard")

Warrior1.describe()
Mage1.describe()

Warrior1.attack(Mage1)
Mage1.health_check()

Mage1.attack(Warrior1)
Warrior1.health_check()

Mage1.attack(Warrior1)
Warrior1.health_check()

Mage1.attack(Warrior1)
Warrior1.health_check()