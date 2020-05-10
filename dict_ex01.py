# 다음 nums에 포함된 숫자 0 ~ 9 의 개수를 출력하라
# 0개인 것도 포함하도록 한다
# 0 - 1
# 1 - 2
# 2 - 6
# 3 - 9
# ...
# 9 - 3

nums='1237894673683038478236749192738623234234'

cnt = dict.fromkeys("0123456789", 0)
for x in nums:
    cnt[x] += 1

#for key, value in cnt.items():
#    print(f'{key} - {value}')

print('\n'.join(f'{key} - {value}' for key, value in cnt.items()))
