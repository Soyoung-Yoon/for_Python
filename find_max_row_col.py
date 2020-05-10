# 배열에서 합이 가장 큰 행과 열의 번호를 각각 인쇄하라
# N * N 배열의 각 요소에 정수가 들어 있다
# 5
# 3 -5 12 3 -21
# -2 11 2 -7 -11
# 21 -21 -34 -93 -11
# 9 14 39 -98 -1
# -2 -2 -2 -2 -2

N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]
brr = [ sum(x) for x in arr ]
rowmax = max(brr)
print(brr.index(rowmax))
crr = [ sum(x) for x in zip(*arr)]
colmax = max(crr)
print(crr.index(colmax))
