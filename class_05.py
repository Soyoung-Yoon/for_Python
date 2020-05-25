
class myInt(int):
   def increase(self, step):
      if type(step) != int :
         raise TypeError
      return self.real + step

a = myInt(5)
b = myInt(10)
print(a+b, a-b, a*b, a/b) 

c = a.increase(3)
print(c)
