def getYesNo(a) :
    return 'YES' if 'f' <= a <= 'o' else 'NO'

def getTimes(num):
    if not num % 2 : result = 2
    elif not num % 3 : result = 3
    elif not num % 5 : result = 5
    else : result = 0
    return result

def getTimes2(num):
    if not num % 2 : return 2
    if not num % 3 : return 3
    if not num % 5 : return 5
    return 0

def getTimes3(num):
    return 2 if not num % 2 else \
           3 if not num % 3 else \
           5 if not num % 5 else 0

import dis
dis.dis(getTimes3)
print(getYesNo(input('Input a character : '))) 
print(getTimes3(int(input('Input a number : '))))
