
class Mammal:
    ''' This is Mammal class '''
    def __new__(cls, *args, **kwargs):
        print('__new__', cls.__name__)
        print(args, kwargs, sep='\n')
        return super().__new__(cls)
        
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('__init__', self.__class__)

m = Mammal('Happy', age=3)


