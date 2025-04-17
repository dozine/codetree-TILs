from sortedcontainers import SortedSet

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
queries = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# treeset에 점들을 넣어줍니다.
s = SortedSet(points)

# 질의마다 조건에 맞는 점을 찾아줍니다.
for target in queries:
    idx = s.bisect_left(target)
    # 그러한 점이 없다면 -1을 출력합니다.
    if idx == len(s):
        print(-1, -1)
    # 존재한다면, 그 지점의 값을 출력합니다.
    else:
        x, y = s[idx]
        print(x, y)
