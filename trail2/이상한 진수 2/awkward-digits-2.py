import sys

INT_MIN = -sys.maxsize

def decimal(arr):
    num = 0
    for x in arr:
        num = num * 2 + x
    return num

a = list(map(int, input()))
n = len(a)

ans = INT_MIN

for i in range(n):
    a[i] = 1 - a[i]
    ans = max(ans, decimal(a))
    a[i] = 1 - a[i]

print(ans)


# 각 자리의 비트를 하나씩 뒤집어 최댓값 탐색
# 0/1 반전: 1 - x
# 이진수 변환: 이전 결과 * 2 + 현재 비트