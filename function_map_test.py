a = ['Korea', 'Maxico', 'USA', 'Japan', 'China']
b = map(len, a)
for x, y in zip(a, b) :
    print(x, y)

import sys
print(sys.getsizeof(a))
print(sys.getsizeof(map(len,a)))


