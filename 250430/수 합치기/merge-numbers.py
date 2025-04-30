from collections import deque

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

from bisect import insort

ans = 0
arr = deque(arr)

while len(arr) > 1:
    a = arr.popleft()
    b = arr.popleft()
    cost = a + b
    ans += cost
    # 삽입 위치를 정렬 유지하며 넣기
    insort(arr, cost)

print(ans)
