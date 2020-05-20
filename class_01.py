
class Mammal :
    # attribute, method
    # special method 
    def __str__(self):
        return f'My name is {self.name}.\nMy age is {self.age}.'
    
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
m1 = Mammal('Happy', 3)
m2 = Mammal('Tom', 2)

print(m1)
print(m2)

print(m1.name, m1.age)  # instance의 attribute
print(m2.name, m2.age)
