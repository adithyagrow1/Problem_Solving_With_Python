class Vehicle:
    def __init__(self,name):
        self.name = name

    def breaking_system(self):
        pass

class BMW(Vehicle):
    def breaking_system(self):
        return f"{self.name}has ABS"

class Maruthi(Vehicle):
    def breaking_system(self):
        return f"{self.name}has NBS"

car1 = BMW ("X5")
car2 = Maruthi ("Alto")
print(car1.breaking_system())
print(car2.breaking_system())