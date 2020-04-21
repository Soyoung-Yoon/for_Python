# return object

def func1(): # None  (return 문이 없는 경우) 
    print('hi')
    
def func2(a):
    return a

def func3(a, b):
    return (a, b)  # a, b를 item으로 하는 tuple

x = func1()
print(x)

x = func2(100)
print(x)

x = func3(100, 200)
print(type(x), x)

x, y = func3(10, 20)
print(x, y)
