def func1(a, b): pass
def func2(a, /): pass
def func3(*, a): pass
def func4(*a, b): pass
def func5(**a): pass

func1(10, b=10)
func2(10)
func3(a=20)
func4(10, 20, 30, 40, b=20)
func5(x=10, y=20, z=30)
