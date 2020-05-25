
class Mammal:
    def __init__(self, age):
        self.age = age
        print("init Mammal")

    def printAge(self):
        print(f'my age is {self.age}')

m = Mammal(20)
print(m.age)
m.printAge()  # m instance namespace에서 - Mammal namespace
print(Mammal.__dict__)
print(m.__dict__)
