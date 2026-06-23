n, m = map(int, input().split())

# N x M 크기의 격자를 0으로 초기화합니다.
arr = [
    [0] * m
    for _ in range(n)
]

# [중요] 문제 조건 순서: 아래(0) -> 오른쪽(1) -> 위쪽(2) -> 왼쪽(3)
# 행(x)과 열(y)의 변화량을 순서대로 적어줍니다.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x, y = 0, 0
cur_dir = 0  # 처음에는 '아래쪽'으로 시작하므로 인덱스 0

# 시작 위치(0, 0)에 첫 번째 숫자 1을 채웁니다.
arr[x][y] = 1

# 격자 안의 인덱스 범위를 체크하는 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 2부터 N*M까지의 숫자를 순서대로 채웁니다.
for i in range(2, n * m + 1):
    # 현재 방향으로 한 칸 나아갔을 때의 위치를 미리 계산해봅니다.
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    
    # 만약 격자를 벗어나거나, 이미 숫자가 채워져 있는 칸(0이 아닌 칸)을 만난다면?
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        # 시계 방향으로 90도 회전합니다 (0 -> 1 -> 2 -> 3 -> 0)
        cur_dir = (cur_dir + 1) % 4
    
    # 확정된 방향으로 실제로 한 칸 이동합니다.
    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    
    # 해당 칸에 숫자를 채웁니다.
    arr[x][y] = i

# 출력부
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()