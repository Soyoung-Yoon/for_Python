Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 123
123
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> 1234
1234
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> 123 + 456
579
>>> dis(123+456)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dis(123+456)
NameError: name 'dis' is not defined
>>> import dis
>>> dis(123+456)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dis(123+456)
TypeError: 'module' object is not callable
>>> dis.dis(123+456)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dis.dis(123+456)
  File "C:\Python37-64\lib\dis.py", line 77, in dis
    type(x).__name__)
TypeError: don't know how to disassemble int objects
>>> dis.dis(complie(123+456))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dis.dis(complie(123+456))
NameError: name 'complie' is not defined
>>> __builtins__
<module 'builtins' (built-in)>
>>> print(__builtins__)
<module 'builtins' (built-in)>
>>> import builtins
>>> print(builtins)
<module 'builtins' (built-in)>
>>> builtins.compile(123+456)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    builtins.compile(123+456)
TypeError: compile() missing required argument 'filename' (pos 2)
>>> def func():
	return 123+456

>>> dis.dis(func)
  2           0 LOAD_CONST               1 (579)
              2 RETURN_VALUE
>>> def func2():
	a = 123
	b = 456
	return a + b

>>> dis.dis(func2)
  2           0 LOAD_CONST               1 (123)
              2 STORE_FAST               0 (a)

  3           4 LOAD_CONST               2 (456)
              6 STORE_FAST               1 (b)

  4           8 LOAD_FAST                0 (a)
             10 LOAD_FAST                1 (b)
             12 BINARY_ADD
             14 RETURN_VALUE
>>> def func3():
	a = 123
	return a + 456

>>> did.dis(func3)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    did.dis(func3)
NameError: name 'did' is not defined
>>> dis.dis(func3)
  2           0 LOAD_CONST               1 (123)
              2 STORE_FAST               0 (a)

  3           4 LOAD_FAST                0 (a)
              6 LOAD_CONST               2 (456)
              8 BINARY_ADD
             10 RETURN_VALUE
>>> def func4():
	a = 123 + 456
	return a

>>> dis.dis(func4)
  2           0 LOAD_CONST               1 (579)
              2 STORE_FAST               0 (a)

  3           4 LOAD_FAST                0 (a)
              6 RETURN_VALUE
>>> def func5():
	b = (10) + (20)
	return b

>>> dis.dis(func5)
  2           0 LOAD_CONST               1 (30)
              2 STORE_FAST               0 (b)

  3           4 LOAD_FAST                0 (b)
              6 RETURN_VALUE
>>> def func5():
	b = (100).__add__(200)
	return b

>>> dis.dis(func5)
  2           0 LOAD_CONST               1 (100)
              2 LOAD_METHOD              0 (__add__)
              4 LOAD_CONST               2 (200)
              6 CALL_METHOD              1
              8 STORE_FAST               0 (b)

  3          10 LOAD_FAST                0 (b)
             12 RETURN_VALUE
>>> def func6():
	a = 100
	b = 200
	return a.__add__(b)

>>> dis.dis(func6)
  2           0 LOAD_CONST               1 (100)
              2 STORE_FAST               0 (a)

  3           4 LOAD_CONST               2 (200)
              6 STORE_FAST               1 (b)

  4           8 LOAD_FAST                0 (a)
             10 LOAD_METHOD              0 (__add__)
             12 LOAD_FAST                1 (b)
             14 CALL_METHOD              1
             16 RETURN_VALUE
>>> b = dis.Bytecode(func)
>>> print(b)
Bytecode(<function func at 0x000001F0FDE671F8>)
>>> for x in b:
	print(x.opname)

	
LOAD_CONST
RETURN_VALUE
>>> def func6():
	b = 'abc' + 'def'
	c = 'aaa'
	return a + b

>>> dis.dis(func6)
  2           0 LOAD_CONST               1 ('abcdef')
              2 STORE_FAST               0 (b)

  3           4 LOAD_CONST               2 ('aaa')
              6 STORE_FAST               1 (c)

  4           8 LOAD_GLOBAL              0 (a)
             10 LOAD_FAST                0 (b)
             12 BINARY_ADD
             14 RETURN_VALUE
>>> def func7():
	a = [1, 2, 3, 4]
	return a + 5

>>> dis.dis(func7)
  2           0 LOAD_CONST               1 (1)
              2 LOAD_CONST               2 (2)
              4 LOAD_CONST               3 (3)
              6 LOAD_CONST               4 (4)
              8 BUILD_LIST               4
             10 STORE_FAST               0 (a)

  3          12 LOAD_FAST                0 (a)
             14 LOAD_CONST               5 (5)
             16 BINARY_ADD
             18 RETURN_VALUE
>>> def func8():
	a = (1, 2, 3, 4)
	return a + 5

>>> dis.dis(func8)
  2           0 LOAD_CONST               1 ((1, 2, 3, 4))
              2 STORE_FAST               0 (a)

  3           4 LOAD_FAST                0 (a)
              6 LOAD_CONST               2 (5)
              8 BINARY_ADD
             10 RETURN_VALUE
>>> def func9():
	return {1,2,3,4}

>>> dis.dis(func9)
  2           0 LOAD_CONST               1 (1)
              2 LOAD_CONST               2 (2)
              4 LOAD_CONST               3 (3)
              6 LOAD_CONST               4 (4)
              8 BUILD_SET                4
             10 RETURN_VALUE
>>> def func10():
	return {'a':10, 'b':20}

>>> dis.dis(func10)
  2           0 LOAD_CONST               1 (10)
              2 LOAD_CONST               2 (20)
              4 LOAD_CONST               3 (('a', 'b'))
              6 BUILD_CONST_KEY_MAP      2
              8 RETURN_VALUE
>>> def func11():
	return {1,2,3,4}

>>> dis.dis(func11)
  2           0 LOAD_CONST               1 (1)
              2 LOAD_CONST               2 (2)
              4 LOAD_CONST               3 (3)
              6 LOAD_CONST               4 (4)
              8 BUILD_SET                4
             10 RETURN_VALUE
>>> [1, 2, 3][2] = 10
>>> (1, 2, 3)[1] = 20
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    (1, 2, 3)[1] = 20
TypeError: 'tuple' object does not support item assignment
>>> a = 2020
>>> b = a
>>> c = a
>>> print(a, b, c)
2020 2020 2020
>>> a = 3000
>>> print(a, b, c)
3000 2020 2020
>>> import sys
>>> sys.getrefcount(a)
2
>>> sys.getrefcount(b)
3
>>> sys.getrefcount(sys)
103
>>> type(sys)
<class 'module'>
>>> isinstance(sys, type)
False
>>> isinstance(int, type)
True
>>> type(sys.getrefcount)
<class 'builtin_function_or_method'>
>>> sys.getrefcount
<built-in function getrefcount>
>>> 
================== RESTART: C:/Python37-64/MyModules/name1.py ==================
30
300
>>> 
================================ RESTART: Shell ================================
>>> a = 2020
>>> b = 2020
>>> import sys
>>> sys.getrefcount(a)
2
>>> sys.getrefcount(b)
2
>>> c = a
>>> sys.getrefcount(c)
3
>>> del a
>>> del b
>>> del c
>>> a = 2020
>>> b = a
>>> import sys
>>> sys.getrefcount(a)
3
>>> del a
>>> sys.getrefcount(b)
2
>>> del b
>>> a = 123
>>> b = 123
>>> import sys
>>> sys.getrefcount(b)
6
>>> a = 256
>>> sys.getrefcount(a)
71
>>> a = 2020
>>> b = a
>>> import sys
>>> sys.getrefcount(b)
3
>>> del a
>>> sys.getrefcount(a)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    sys.getrefcount(a)
NameError: name 'a' is not defined
>>> del b
>>> a = 2020
>>> b = a
>>> import sys
>>> sys.getrefcount(b)
3
>>> del a
>>> sys.getrefcount(b)
2
>>> 