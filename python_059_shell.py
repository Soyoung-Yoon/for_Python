Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = (1, 2, 3)
>>> for x in a : print(x)

1
2
3
>>> for x in a :
	print(x)

	
1
2
3
>>> for x in a :
	if x % 2 : print(x)

	
1
3
>>> for x in range(3) : print(x)

0
1
2
>>> for x in range(1, 4) : print(x)

1
2
3
>>> for x in range(1, 10, 2) : print(x)

1
3
5
7
9
>>> for x in a :
	if not x % 2 : break
	print(x)
else:
	print("done1")

	
1
>>> for x in a :
	if not x % 2 : continue
	print(x)
else:
	print("done2")

	
1
3
done2
>>> 