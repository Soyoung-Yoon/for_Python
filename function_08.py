# var-positional parameter

def getSum(*data):
    print(type(data), len(data))
    return sum(data)

r = getSum(1,2,3,4,5,6,7,8,9,10)
print(r)

r = getSum(10, 20, 30)
print(r)

r = getSum()
print(r)
