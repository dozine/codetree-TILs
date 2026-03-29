import sys

n, m = map(int, sys.stdin.readline().split())

pos_a = []
pos_b = []

curr_a = 0
for _ in range(n):
    dist, direction = sys.stdin.readline().split()
    dist = int(dist)
    for _ in range(dist):
        if direction == 'R':
            curr_a += 1
        else:
            curr_a -= 1
        pos_a.append(curr_a)

# B의 이동 경로 기록 (1초 단위)
curr_b = 0
for _ in range(m):
    dist, direction = sys.stdin.readline().split()
    dist = int(dist)
    for _ in range(dist):
        if direction == 'R':
            curr_b += 1
        else:
            curr_b -= 1
        pos_b.append(curr_b)

# 2. 최초로 만나는 시간 찾기
# 두 사람이 움직인 총 시간 중 더 짧은 시간만큼만 비교 가능 (동시에 움직이는 동안만)
min_time = min(len(pos_a), len(pos_b))
ans = -1 # 만약 만나지 못하면 -1 출력 (문제 조건에 따라 다름)

for t in range(min_time):
    # t는 인덱스이므로, 실제 시간은 t + 1초입니다.
    if pos_a[t] == pos_b[t]:
        ans = t + 1
        break

print(ans)