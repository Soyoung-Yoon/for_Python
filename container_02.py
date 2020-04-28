# '10 20 30 40 50' --> [10, 20, 30, 40, 50]
a = '10 20 30 40 50'
b = list(map(int, a.split()))
print(b)

# 1 ~ 10의 item을 갖는 list 생성
a = list(range(1, 11))
print(a)

# 중복을 제거한 list 생성 - 1
a = [1, 2, 3, 2, 1, 5, 4, 2, 3, 4, 3, 6]
b = list(set(a))
print(b)

# 중복을 제거한 list 생성 - 2
a = [ [1, 2], [1, 2, 3], [1, 2], [1, 2, 3] ]
b = list( map(list, set(map(tuple, a))) )
print(b)

# a를 key, b를 value로 사용하는 dict 객체 생성
a = ['name', 'age', 'gender']
b = ['Julie', 30, 'F']

c = dict(zip(a, b))
print(c)
