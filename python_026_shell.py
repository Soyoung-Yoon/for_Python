Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = 10, 20, 30
>>> type(data)
<class 'tuple'>
>>> a, b, c = True, 25, 'good'
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'int'>
>>> type(c)
<class 'str'>
>>> print(a, b, c)
True 25 good
>>> a, b, c = [4, 5, 6]
>>> print(a, b, c)
4 5 6
>>> 