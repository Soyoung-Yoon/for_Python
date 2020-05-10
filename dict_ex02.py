# 다음 nums에 포함된 숫자 0 ~ 9 의 개수를 출력하라
# 0개인 것은 포함하지 않으며, 발생 순서로 출력되도록 한다.
# 1 - 2
# 2 - 6
# 3 - 9
# 7 - 5
# ...
# 0 - 1

nums='1237894673683038478236749192738623234234'

cnt = {}

for x in nums :
    cnt.setdefault(x, 0)
    cnt[x] += 1
    
print('\n'.join(f'{key} - {value}' for key, value in cnt.items()))


# 빈도가 큰 것이 먼저 출력되도록 정렬하도록 한다.
# 빈도가 같은 경우 작은 숫자 -> 큰 숫자 순서로 출력되도록 한다.
# 예)
# 3 - 9
# 2 - 6
# 4 - 5
# 7 - 5
# 8 - 5
# ...
# 0 - 1

a = sorted(cnt.items(), key = lambda x : (-x[1], x[0]))
print(a)


## 참고하세요 
print('\n'.join( f'{key} - {value}' for key, value in a ) )
