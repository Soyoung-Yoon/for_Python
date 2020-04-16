# 정수 두 개(a, b)를 입력 받아
# a 부터 b까지 더하는 프로그램을 작성하라
# 더한 결과를 result에 저장하여 출력한다

# I - P - O
a = int(input('Input the first num : '))
b = int(input('Input the second num : '))

# 1 + 2 + 3 + 4 + 5
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
result = a # 초기화 
for x in range(a+1, b+1):
    result = result + x  # 누적
    
print(result)
