fruit = ['apple', 'mango', 'kiwi', 'orange']
test  = ['A', 'z', 'a', 'Z', 'c'] 

if 0 :
    fruit.sort()
    print(fruit)
    fruit.sort(reverse=True)
    print(fruit)

if 0:
    r1 = sorted(test)
    print(id(test), id(r1))
    print(f'r1 = {r1}\ntest = {test}')

if 1:
    #str.lower(test[0])  str.lower(test[1]) ...
    # [ 'a', 'a', 'c', 'z', 'z']
    #test.sort(key=str.lower)
    test.sort(key= lambda x : (str.lower(x), x))
    print(f'test = {test}')
