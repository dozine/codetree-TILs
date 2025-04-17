from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
s=SortedSet(arr)
#같거나 큰 최초의 숫자를 계산
for num in queries:
    idx=s.bisect_left(num)
    if idx == len(s):
        print(-1)
    else:
        print(s[idx])