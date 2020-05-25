
class Mammal:
   def __init__(self, age):
      self.age = age
      print("init Mammal")

   def __add__(self, other):
      return self.age + other if type(other) == int else self.age + other.age

   def __str__(self):
      return f'my age is {self.age}'
   
m1 = Mammal(20)
m2 = Mammal(30)
print(m1 + m2)
print(m1 + 10)
print(m1)
