# 1. 1개의 행에 임의 개수의 정수를 입력 받는다
# 2. 각 정수의 일의 자리를 0으로 하는 숫자로 변경한다
# 3. 2번 처리된 결과를 list로 작성하여 출력한다 
# 예)
# 25 89 112
# [20, 80, 110]
# map, lambda, input, int, str.split 을 사용하여 작성한다

# I - P - O
a = list(map(lambda x : int(x)//10*10, input().split()))
print(a)

