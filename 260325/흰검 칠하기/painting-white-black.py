import sys

# 1. 설정 및 입력
n = int(sys.stdin.readline())
MAX_V = 200000  # 명령이 1000개, x가 100이므로 최대 10만 이동 가능
OFFSET = 100000
cur = OFFSET

# 각 칸별 흰색/검은색 칠해진 횟수 저장
white_cnt = [0] * MAX_V
black_cnt = [0] * MAX_V
# 각 칸의 최종 색깔 (0: 없음, 1: 흰색, 2: 검은색, 3: 회색)
color = [0] * MAX_V

for _ in range(n):
    line = sys.stdin.readline().split()
    if not line: break
    x, d = int(line[0]), line[1]
    
    if d == 'R':
        # 오른쪽으로 이동: 현재 위치 포함 x칸 (cur ~ cur + x - 1)
        for i in range(cur, cur + x):
            black_cnt[i] += 1
            # 이미 회색이 아니라면 검은색으로 칠함
            if color[i] != 3:
                color[i] = 2
            # 조건 체크: 흰색 2번 이상 & 검은색 2번 이상 -> 회색(3)
            if white_cnt[i] >= 2 and black_cnt[i] >= 2:
                color[i] = 3
        # 마지막으로 칠한 타일 위치로 이동
        cur = cur + x - 1
    else:
        # 왼쪽으로 이동: 현재 위치 포함 x칸 (cur - x + 1 ~ cur)
        for i in range(cur - x + 1, cur + 1):
            white_cnt[i] += 1
            # 이미 회색이 아니라면 흰색으로 칠함
            if color[i] != 3:
                color[i] = 1
            # 조건 체크
            if white_cnt[i] >= 2 and black_cnt[i] >= 2:
                color[i] = 3
        # 마지막으로 칠한 타일 위치로 이동
        cur = cur - x + 1

# 2. 결과 집계
w_final = color.count(1)
b_final = color.count(2)
g_final = color.count(3)

print(w_final, b_final, g_final)