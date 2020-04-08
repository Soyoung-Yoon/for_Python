Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #'123' -> 123
>>> # 123  -> '123'
>>> int
<class 'int'>
>>> float
<class 'float'>
>>> str
<class 'str'>
>>> tuple
<class 'tuple'>
>>> a = int(3.5)
>>> a
3
>>> type(a)
<class 'int'>
>>> b = int('1234')
>>> type(b)
<class 'int'>
>>> b
1234
>>> int('123.4')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int('123.4')
ValueError: invalid literal for int() with base 10: '123.4'
>>> int('a123')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int('a123')
ValueError: invalid literal for int() with base 10: 'a123'
>>> b = float(12)
>>> b
12.0
>>> type(b)
<class 'float'>
>>> c = float('123.4')
>>> c
123.4
>>> type(c)
<class 'float'>
>>> a = str(10)
>>> type(a)
<class 'str'>
>>> a
'10'
>>> b = str(3.4)
>>> type(b)
<class 'str'>
>>> b
'3.4'
>>> c = str( (1,2,3,4) )
>>> c
'(1, 2, 3, 4)'
>>> 