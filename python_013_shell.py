Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple, list, str, range : Sequence type Container
>>> a = (1,2,3,4)
>>> b = [10,20,30,40,50]
>>> c = "abcde"
>>> d = range(5, 10)
>>> a[0]
1
>>> a[3]
4
>>> a[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[4]
IndexError: tuple index out of range
>>> b[-1]
50
>>> b[-3]
30
>>> c[2]
'c'
>>> d[-1]
9
>>> d[0]
5
>>> 