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

    def describe(self):
        print(self.name, "has", self.get_health(), "health, and", self.attack_power, "attack power.")
    
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=40, attack_power=20)
    def describe(self):
        print("A Mage named", self.name, "with", self.get_health(), "health, and", self.attack_power, "attack power. Mage's are magic and powerful.")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=50, attack_power=10)
    def describe(self):
        print("A Warrior named", self.name, "with", self.get_health(), "health, and", self.attack_power, "attack power. Warrior's are slow to fight.")

class Alien(Character):
    def __init__(self, name):
        super().__init__(name, health=30, attack_power=30)
    def describe(self):
        print("An Alien named", self.name, "with", self.get_health(), "health, and", self.attack_power, "attack power. Alien's are from another planet.")

#testing polymorphism
Mage1 = Mage("Gandalf")
Warrior1 = Warrior("Heavy")
Alien1 = Alien("Martian")

characters = [Mage("Gandalf"), Warrior("Heavy"), Alien("Martian")]
for character in characters:
    character.describe()

#attack system
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