
def add(a, b):    
    c = a + b
    print(locals())
    return c

r = add(10,20)
print(r)
print(globals())

import dis

print(add.__code__.co_varnames)
dis.dis(add)

