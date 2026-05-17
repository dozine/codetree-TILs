# import sys
# input = sys.stdin.readline

# # 1. 입력 받기
# n, m = map(int, input().split())

# # 배열을 미리 크게 만들지 않고, 0초 위치만 넣어 시작합니다.
# pos_a = [0]
# pos_b = [0]

# # A의 경로 기록 (실제로 움직인 만큼만 append)
# for _ in range(n):
#     t, d = input().split()
#     for _ in range(int(t)):
#         next_pos = pos_a[-1] + (1 if d == 'R' else -1)
#         pos_a.append(next_pos)

# # B의 경로 기록
# for _ in range(m):
#     t, d = input().split()
#     for _ in range(int(t)):
#         next_pos = pos_b[-1] + (1 if d == 'R' else -1)
#         pos_b.append(next_pos)

# # 2. 두 사람의 이동 시간이 다를 경우, 마지막 위치로 채워주기
# # (이 부분이 중요합니다. 한 명이 먼저 멈춰도 그 자리에 계속 서 있으니까요.)
# len_a, len_b = len(pos_a), len(pos_b)

# if len_a < len_b:
#     pos_a += [pos_a[-1]] * (len_b - len_a)
# elif len_b < len_a:
#     pos_b += [pos_b[-1]] * (len_a - len_b)

# # 3. 만나는 횟수 계산 (실제 총 시간만큼만 루프)
# cnt = 0
# for i in range(1, len(pos_a)):
#     # 직전에는 달랐는데 지금 같아진 순간 (새롭게 만남)
#     if pos_a[i] == pos_b[i] and pos_a[i-1] != pos_b[i-1]:
#         cnt += 1

# print(cnt)




n, m = tuple(map(int, input().split()))

# 최대 1000000초까지 고려할 수 있도록 넉넉하게 배열 크기 설정
MAX_T = 1000000
pos_a = [0] * (MAX_T + 1)
pos_b = [0] * (MAX_T + 1)

# A의 이동 기록
time_a = 1
for _ in range(n):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == "L":
            pos_a[time_a] = pos_a[time_a - 1] - 1
        else:
            pos_a[time_a] = pos_a[time_a - 1] + 1
        time_a += 1

# B의 이동 기록 (range(m)으로 수정)
time_b = 1
for _ in range(m):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == "L":
            pos_b[time_b] = pos_b[time_b - 1] - 1
        else:
            pos_b[time_b] = pos_b[time_b - 1] + 1
        time_b += 1

# 두 로봇이 각각 움직인 총 시간
total_time_a = time_a - 1
total_time_b = time_b - 1

# 전체 진행 시간은 둘 중 더 오래 움직인 로봇의 시간입니다.
max_time = max(total_time_a, total_time_b)

# 먼저 멈춘 로봇의 나머지 시간대 위치를 최종 위치로 채워줍니다.
if total_time_a < max_time:
    for i in range(total_time_a + 1, max_time + 1):
        pos_a[i] = pos_a[total_time_a]
        
if total_time_b < max_time:
    for i in range(total_time_b + 1, max_time + 1):
        pos_b[i] = pos_b[total_time_b]

# 다른 위치에 있다가 같은 위치에서 만나게 되는 경우 카운트
ans = 0
for i in range(1, max_time + 1):
    # 직전(i-1)에는 위치가 달랐고, 현재(i)는 위치가 같은 경우
    if pos_a[i-1] != pos_b[i-1] and pos_a[i] == pos_b[i]:
        ans += 1

print(ans)