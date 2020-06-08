
class MyRange:

    def __init__(self, start, stop):
        self.curr = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        curr = self.curr
        if curr < self.stop :
            self.curr += 1
        else :
            raise StopIteration
        return curr

from collections.abc import Iterator
print(isinstance(MyRange(1, 4), Iterator))
print(isinstance(range(1, 4), Iterator))

for i in MyRange(1, 5):
    print(i, end=' ')
print()

print(list(MyRange(0, 10)))
        
