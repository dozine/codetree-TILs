# 1. N과 T 입력
n, t = map(int, input().split())

# 2. 명령어가 먼저 들어오는 경우, 위치를 위로 올립니다.
commands = input().strip()

# 3. 그 다음 격자 숫자 정보를 입력받습니다.
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# (이하 로직은 동일)
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
x, y = n // 2, n // 2
cur_dir = 0
total_score = grid[x][y]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

for cmd in commands:
    if cmd == 'L':
        cur_dir = (cur_dir - 1 + 4) % 4
    elif cmd == 'R':
        cur_dir = (cur_dir + 1) % 4
    elif cmd == 'F':
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if in_range(nx, ny):
            x, y = nx, ny
            total_score += grid[x][y]

print(total_score)