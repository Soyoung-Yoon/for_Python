# 다음 조건을 만족하는 프로그램을 작성하시오
# 암호를 최대 3회 입력 받는다
# 암호가 “snowbear08#” 이면 ‘success’를 출력하고 종료한다
# 암호가 틀리면 ‘try again’을 출력하고 다시 입력 받는다
# 암호는 3회 모두 틀린 경우
# ‘try again’을 출력하지 않고 ‘fail’을 출력한다

PW = 'snowbear08#'

for x in range(3):
    UPW = input('암호를 입력하세요 : ')
    if PW == UPW :
        print('success')
        break
    else:
        if x < 2 : print('try again')
else:
    print('fail')
