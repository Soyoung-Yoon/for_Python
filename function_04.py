
def func1(a, b=20): pass
def func2(*, a=10, b): pass
def func3(*a, b, c=30): pass

func1(10)
func2(b=20)
func2(a=30, b=20)
func3(b=20)
func3(b=20, c=40)
