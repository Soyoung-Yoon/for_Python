Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input()
soyoung
'soyoung'
>>> name = input()
soyoung
>>> print(name)
soyoung
>>> age = input()
20
>>> print(age)
20
>>> type(name)
<class 'str'>
>>> type(age)
<class 'str'>
>>> age + 10
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    age + 10
TypeError: can only concatenate str (not "int") to str
>>> age + '10'
'2010'
>>> int(age) + 10
30
>>> age = int(input())
20
>>> type(age)
<class 'int'>
>>> a = int('1234-234')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a = int('1234-234')
ValueError: invalid literal for int() with base 10: '1234-234'
>>> a = int('12.34')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a = int('12.34')
ValueError: invalid literal for int() with base 10: '12.34'
>>> a = int('12386')
>>> type(a)
<class 'int'>
>>> a
12386
>>> b = float(input())
3.14
>>> type(b)
<class 'float'>
>>> b
3.14
>>> age = int(input('Input your age : '))
Input your age : 20
>>> type(age)
<class 'int'>
>>> age
20
>>> age = input()
123 456 789
>>> a
12386
>>> b = float(input())
3.14
>>> type(b)
<class 'float'>
>>> b
3.14
>>> age = int(input('Input your age : '))
Input your age : 20
>>> type(age)
<class 'int'>
>>> age
20
>>> 