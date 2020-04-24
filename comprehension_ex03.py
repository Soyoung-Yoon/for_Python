# 동작 결과 생성되는 item의 개수는?
# Hint) set은 중복 item을 허용하지 않음 
a = [ x*y for x in range(2, 10)
             for y in range(1, 10) ]
b = { x*y for x in range(2, 10) for y in range(1, 10) }
print(a)
print(b)
print('length of a : ', len(a))
print('length of b : ', len(b))

# name을 key, score를 value로 하는 dict 를 생성하라
# 단, score의 경우 반올림하여 정수로 처리한다
# score가 80.0 이상인 것에 대해서만 대상으로 한다 
# 결과 : { 'Sam' : 91, 'Merry' : 96, 'Tom' : 85 }
name  = ['Sam', 'John', 'Merry', 'Tom']
score = [90.5, 75.2, 95.8, 85.3]

r = { k:int(v+0.5)
      for k, v in zip(name, score)
      if v >= 80.0 }
print(r)

# () [] {}
