Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # object : value, type, identity
>>> type(100)
<class 'int'>
>>> id(100)
140737278016880
>>> hex(id(100))
'0x7ffff3767d70'
>>> type(id(100))
<class 'int'>
>>> type(hex(id(100)))
<class 'str'>
>>> # oct (0o), bin(0b)
>>> type((1, 2, 3))
<class 'tuple'>
>>> id((1, 2, 3))
1638208183496
>>> (1, 2, 3)[0]
1
>>> (1, 2, 3)[0] = 10
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    (1, 2, 3)[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> [1, 2, 3][0]
1
>>> [1, 2, 3][0] = 10
>>> a = [1,2,3]
>>> a[0] = 10
>>> a
[10, 2, 3]
>>> 