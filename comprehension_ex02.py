# 2차원 list의 입력
# 예)
# 1 2 3
# 4 5 6
# 7 8 9

#r = [ list(map(int, input().split())) for _ in range(3)]
#print(r)

# 2차원 list를 1차원 list로 변경
# 처리 전) [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# 처리 후) [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

for row in a:
    for col in row:
        print(col, end=' ')
print()

r = [ col for row in a for col in row ]
print(r)



