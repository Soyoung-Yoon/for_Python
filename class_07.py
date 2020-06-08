
class Mammal:
   def __init__(self, age):
      self.age = age
      print("init 1:", self.__class__.__name__)

   def printAge(self):
      print(f"my age is {self.age}")


class Dog(Mammal):
   def __init__(self, name, age):
      super().__init__(age)
      self.name = name
      print("init 2:", self.__class__.__name__)
      
      #Mammal.__init__(self)
   def printName(self):
      print(f"my name is {self.name}")
   
d = Dog('Happy', 100)
d.printAge()
d.printName()
print(Dog.__dict__)
print(d.__dict__)
