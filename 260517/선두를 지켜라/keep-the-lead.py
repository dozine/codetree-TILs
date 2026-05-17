# MAX_T = 1000000

# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

# # A가 매 초마다 서있는 위치를 기록
# time_a = 1
# for _ in range(n):
#     v, t = tuple(map(int, input().split()))
#     for _ in range(t):
#         pos_a[time_a] = pos_a[time_a - 1] + v
#         time_a += 1

# # B가 매 초마다 서있는 위치를 기록
# time_b = 1
# for _ in range(m):
#     v, t = tuple(map(int, input().split()))
#     for _ in range(t):
#         pos_b[time_b] = pos_b[time_b - 1] + v
#         time_b += 1

# # A와 B 중 더 앞서 있는 경우를 확인합니다.
# # A가 리더면 1, B가 리더면 2로 관리합니다.
# leader, ans = 0, 0
# for i in range(1, time_a):
#     if pos_a[i] > pos_b[i]:
#         # 기존 리더가 B였다면
#         # 답을 갱신합니다.
#         if leader == 2:
#             ans += 1

#         # 리더를 A로 변경합니다.
#         leader = 1
#     elif pos_a[i] < pos_b[i]:
#         # 기존 리더가 A였다면
#         # 답을 갱신합니다.
#         if leader == 1:
#             ans += 1

#         # 리더를 B로 변경합니다.
#         leader = 2
        
# print(ans)



# 최대 시간 설정
MAX_T = 1000000

n, m = tuple(map(int, input().split()))

# 각 '초(time)'별 위치를 저장할 배열
pos_a = [0] * (MAX_T + 1)
pos_b = [0] * (MAX_T + 1)

# A의 이동 경로 기록 (매 초마다의 누적 위치)
time_a = 1
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1

# B의 이동 경로 기록 (매 초마다의 누적 위치)
time_b = 1
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b - 1] + v
        time_b += 1

# 전체 이동 시간 (A와 B의 총 이동 시간은 같습니다)
total_time = time_a

leader = ""
ans = 0

# 1초부터 총 이동 시간까지 매 초마다 비교
for i in range(1, total_time):
    if pos_a[i] > pos_b[i]:
        # 기존 선두가 B였다면 A로 바뀌면서 카운트 증가
        if leader == "B":
            ans += 1
        leader = "A"
    elif pos_b[i] > pos_a[i]:
        # 기존 선두가 A였다면 B로 바뀌면서 카운트 증가
        if leader == "A":
            ans += 1
        leader = "B"
    # 두 위치가 같은 경우는 leader를 바꾸지 않으므로 
    # 문제 조건인 "공동 선두일 때는 선두가 바뀌지 않는다"가 자동으로 만족됩니다.

print(ans)