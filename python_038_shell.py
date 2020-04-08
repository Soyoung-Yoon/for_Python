Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input('data : ')
data : soyoung
>>> print(a)
soyoung
>>> b = input()
100
>>> print(type(b))
<class 'str'>
>>> b + 10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b + 10
TypeError: can only concatenate str (not "int") to str
>>> b = int(b)
>>> type(b)
<class 'int'>
>>> c = int(input())
123
>>> type(c)
<class 'int'>
>>> c
123
>>> c + 10
133
>>> 