Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 'Hello'
>>> b = 'Good Morning \
Good afternoon \
      Good evening'
>>> print(b)
Good Morning Good afternoon       Good evening
>>> c = 'Good Morning \ # 아침인사
SyntaxError: EOL while scanning string literal
>>> c = ( 'Good morning',
      'Good afternoon',
      'Good evening')
>>> print(c)
('Good morning', 'Good afternoon', 'Good evening')
>>> d = (1,      2,        3)
>>> print(d)
(1, 2, 3)
>>> e = (1, # number one
              2,  # number two
     3, # number three
     4)
>>> print(e)
(1, 2, 3, 4)
>>> 