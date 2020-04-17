# 2차원 tuple을 주어진 형식에 맞게 바꾸어 출력하라
# str.format(), f-string 등을 사용해 출력 형식을
# 작성할 수 있다

mydata = ( ('Apple', 'Red', 600),
           ('Kiwi', 'Brown', 300),
           ('Banana', 'Yellow', 200) )

# Apple : price is 600, color is Red
# Kiwi : price is 300, color is Brown
# Banana : price is 200, color is Yellow

for x in mydata :
    name, color, price = x
    print(f'{name} : price is {price}, color is {color}')
    
if 0:
    for x in mydata :
        print('{0} : price is {2}, color is {1}'.format(*x))
    
if 0:
    for x in mydata :
        print(*x, sep=', ')
