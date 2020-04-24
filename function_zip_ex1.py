
a = (82, 52, 1)      
b = ('Korea', 'Maxico', 'USA')
c = zip(a, b)
print(type(c))

print(next(c))
for x in c:
    print(x, type(x))

c = zip(a, b)
for x in c:
    print(type(x), x)

    
