a = ['Korea', 'Maxico', 'USA', 'Japan', 'China']

b = map(len, a)
#print(b)
#iterator
#len('Korea') => 5
#len('Maxico') => 6
for x in b :
    print(x)

import sys
print(sys.getsizeof(a))
print(sys.getsizeof(b))
