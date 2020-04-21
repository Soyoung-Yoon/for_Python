# positional or keyword parameter

def func1(a, b):
    print(a, b)

func1(10, 20)
func1(a=10, b=20)
func1(b=20, a=10)
func1(10, b=20)
#func1(a=10, 20)

def func2(a=0, b=0):
    print(a, b)

func2()
func2(a=10)
func2(b=20)
func2(a=10, b=20)
func2(b=20, a=10)
func2(10, 20)
func2(10, b=20)

def func3(a, b=10):
    print(a, b)

func3(5)
func3(a=5, b=20)
func3(b=20, a=5)
func3(5, 20)

# Error
#def func4(a=10, b):
#    print(a, b)



    

    
