# var-keyword parameter

def myPrint(**data):
    print(type(data), len(data))
    for x in data.items():
        print(x, *x)

myPrint(a=10, b=20, name='Good')
myPrint(x='king', y='prince')
myPrint()
