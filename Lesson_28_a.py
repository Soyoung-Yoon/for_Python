class MyList:
    def __init__(self, a):
        self.data = list(a)

    def __str__(self):
        return '[ ' + ' '.join(map(str,self.data)) + ' ]'

    def __add__(self, other):
        return MyList(self.data + other.data)
    
n1 = MyList( (1, 2, 3, 4, 5) )
n2 = MyList( range(10) )
print(n1)
print(n2)
print(n1 + n2)
