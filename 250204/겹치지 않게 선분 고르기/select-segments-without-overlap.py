import sys

n = int(sys.stdin.readline().strip())
segments = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 끝점 기준으로 정렬
segments.sort(key=lambda x: x[1])

count = 0
last_end = -float('inf')  # 마지막으로 선택한 선분의 끝점

for x1, x2 in segments:
    if x1 >= last_end:  # 현재 선분이 이전에 선택한 선분과 겹치지 않으면 선택
        count += 1
        last_end = x2  # 현재 선분의 끝점을 업데이트

print(count)
