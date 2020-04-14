Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 1 + 3.14
>>> type(a)
<class 'float'>
>>> a
4.140000000000001
>>> b = '%d' % 10
>>> type(b)
<class 'str'>
>>> b
'10'
>>> # tuple, list, set, dict display
>>> a = (1, 2, 3)
>>> b = [1,2,3]
>>> c = {1, 2, 3}
>>> d = { 'A': 65, 'B':66}
>>> type(a)
<class 'tuple'>
>>> type(b)
<class 'list'>
>>> type(c)
<class 'set'>
>>> type(d)
<class 'dict'>
>>> e = [ x for x in range(4) ]
>>> type(e)
<class 'list'>
>>> e
[0, 1, 2, 3]
>>> a = ()
>>> type(a)
<class 'tuple'>
>>> b = (1,)
>>> type(b)
<class 'tuple'>
>>> c = (1)
>>> type(c)
<class 'int'>
>>> a = 1,
>>> type(a)
<class 'tuple'>
>>> b = 1, 2, 3
>>> type(b)
<class 'tuple'>
>>> c = 1
>>> type(c)
<class 'int'>
>>> 