n = int(input())

# N x N 격자를 0으로 초기화
arr = [
    [0] * n
    for _ in range(n)
]

# 문제 조건 순서: 오른쪽(0) -> 위(1) -> 왼쪽(2) -> 아래(3)
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

# 시작 위치는 정중앙입니다.
x, y = n // 2, n // 2

# 시작점에 1을 채웁니다.
num = 1
arr[x][y] = num

cur_dir = 0       # 처음 방향: 오른쪽 (인덱스 0)
move_dist = 1     # 현재 방향으로 이동할 거리 (처음엔 1칸)

# 숫자 N*N을 다 채울 때까지 반복합니다.
while num < n * n:
    # 현재 방향으로 move_dist만큼 이동하며 숫자를 채웁니다.
    for _ in range(move_dist):
        # 만약 이미 N*N까지 다 채웠다면 더 이상 이동하지 않고 중단
        if num >= n * n:
            break
            
        x, y = x + dxs[cur_dir], y + dys[cur_dir]
        num += 1
        arr[x][y] = num

    # 한 방향으로 move_dist만큼 이동을 마쳤으므로 다음 방향으로 회전합니다.
    cur_dir = (cur_dir + 1) % 4
    
    # [방향 규칙] 위쪽(1)이나 아래쪽(3) 이동을 마친 직후에는 
    # 다음에 이동해야 할 거리가 1 늘어납니다.
    if cur_dir == 2 or cur_dir == 0:
        move_dist += 1

# 출력부
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()