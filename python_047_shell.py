Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #is, is not
>>> a = 200
>>> b = 200
>>> a is b
True
>>> id(a)
140732435171824
>>> id(b)
140732435171824
>>> a = 2020
>>> b = 2020
>>> a is b
False
>>> id (a)
2299290844816
>>> id(b)
2299290845104
>>> a is not b
True
>>> # in, not in
>>> 10 in [ 1, 4, 8, 10, 20, 25 ]
True
>>> 10 in [ 1, 4, 8 20, 25 ]
SyntaxError: invalid syntax
>>> 10 in [ 1, 4, 8, 20, 25 ]
False
>>> 10 not in [ 1, 4, 8, 20, 25 ]
True
>>> a = 2020
>>> b = 2020
>>> a is b
False
>>> a == b
True
>>> [1, 2, 3, 4] == [1, 2, 3, 4]
True
>>> [1, 2, 3, 4] == [1, 3, 2, 4]
False
>>> {1, 2, 3, 4} == {1, 3, 2, 4}
True
>>> 2020 != 2030
True
>>> 2020 != 2020
False
>>> a = 10
>>> b = 20
>>> c = 30
>>> a < b < c
True
>>> a < c < b
False
>>> 1 and 2
2
>>> 0 and 2
0
>>> 1 and 0
0
>>> 