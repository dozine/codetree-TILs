n, m = tuple(map(int, input().split()))

MAX_T = 1000000
pos_a = [0] * (MAX_T + 1)
pos_b = [0] * (MAX_T + 1)

time_a = 1 
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1

time_b = 1 
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b - 1] + v
        time_b += 1

total_time = time_a - 1

ans = 0
current_leader = "AB"

for i in range(1, total_time + 1):
    if pos_a[i] > pos_b[i]:
        now_leader = "A"
    elif pos_b[i] > pos_a[i]:
        now_leader = "B"
    else:
        now_leader = "AB"
    
    if current_leader != now_leader:
        ans += 1
        current_leader = now_leader # 현재 조합을 다음 비교를 위해 저장

print(ans)