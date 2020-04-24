# 함수를 argument로 갖는 함수 작성

data = (10, 21, 32, 43)

def myMap(function, iterable):
    r = []
    for x in iterable:
        r.append(function(x))  # int('10')
    return r

a = myMap(lambda x : x*2, data)
print(a)

data = ['10', '20', '30', '40']
a = myMap(int, data)
print(a)
