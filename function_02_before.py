//  아래의 코드를 사용하여 함수를 작성해 보세요

a = input('Input a character : ')
msg = 'YES' if 'f' <= a <= 'o' else 'NO'
print(msg) 


num = int(input('Input a number : '))
if not num % 2 : result = 2
elif not num % 3 : result = 3
elif not num % 5 : result = 5
else : result = 0
print(result)

score = int(input('Input a score : '))
if score < 0 or score > 100 : grade = 'Error'
elif score >= 90 : grade = 'A'
elif score >= 80 : grade = 'B'
elif score >= 70 : grade = 'C'
elif score >= 60 : grade = 'D'
else : grade = 'F'
print(grade)
