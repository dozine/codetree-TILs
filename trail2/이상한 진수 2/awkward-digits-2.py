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