Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 2020
>>> b = a
>>> import pprint as pp
>>> pp.pprint(globals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'a': 2020,
 'b': 2020,
 'pp': <module 'pprint' from 'C:\\Python37-64\\lib\\pprint.py'>}
>>> id(a)
1611606193232
>>> id(b)
1611606193232
>>> import sys
>>> sys.getrefcount(a)
3
>>> del a
>>> pp.pprint(globals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'b': 2020,
 'pp': <module 'pprint' from 'C:\\Python37-64\\lib\\pprint.py'>,
 'sys': <module 'sys' (built-in)>}
>>> sys.getrefcount(b)
2
>>> del b
>>> # Garbage Collector  - ref_cnt : 0