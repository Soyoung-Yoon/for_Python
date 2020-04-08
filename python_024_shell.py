Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> 
=================== RESTART: C:\Users\JulieYoon\Desktop\EduAtoZ\namespace01.py ===================
3000 2020 2020
>>> import pprint as pp
>>> pp.pprint(globals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__file__': 'C:\\Users\\JulieYoon\\Desktop\\EduAtoZ\\namespace01.py',
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'a': 3000,
 'b': 2020,
 'c': 2020,
 'pp': <module 'pprint' from 'C:\\Python37-64\\lib\\pprint.py'>}
>>> import sys
>>> sys.getrefcount(a)
2
>>> sys.getrefcount(b)
3
>>> id(a)
2401964324016
>>> id(b)
2401964323920
>>> id(c)
2401964323920
>>> 