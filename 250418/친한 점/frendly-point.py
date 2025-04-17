from sortedcontainers import SortedSet
n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

s=SortedSet(points)

for target in queries:
    idx = s.bisect_left(target)
    if idx == len(s):
        print(-1,-1)
    else:
        x,y = s[idx]
        print(x,y)