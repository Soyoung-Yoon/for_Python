## 사칙연산 함수 작성
# 함수의 형태 
# function은 두 개의 positional or keyword parameter 사용
# 두 parameter의 add, sub, mul, floordiv를 반환
# 두 개의 정수를 입력 받는다
# 두 개의 정수를 argument로 사용한다
# 화면에 반환 받은 4개의 값을 예시와 같이 출력한다
# 17
# 4
# 21 13 68 4
def calculation(n1, n2):
    return n1+n2, n1-n2, n1*n2, n1//n2

a = int(input())
b = int(input())
x = calculation(a, b)
print(*x)

print(*calculation(int(input()), int(input())))
