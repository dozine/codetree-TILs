# 입력 처리
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부 기록
visited = [[False] * m for _ in range(n)]

# 방향 벡터: 아래쪽(1, 0), 오른쪽(0, 1)
dxs = [1, 0]
dys = [0, 1]

# 범위 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 이동 가능 여부 확인
def can_go(x, y):
    # 범위 밖이거나, 방문했거나, 뱀이 있는 칸(grid[x][y] == 0)인 경우 불가능
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

# DFS 탐색
def dfs(x, y):
    # 현재 위치 방문 처리
    visited[x][y] = True
    
    # 우측 하단 도달 시 경로 존재
    if x == n - 1 and y == m - 1:
        return True
    
    # 아래와 오른쪽 방향으로 이동
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            if dfs(nx, ny):  # 다음 이동에서 탈출 가능하면 True 반환
                return True

    return False  # 탈출 경로를 찾을 수 없으면 False 반환

# 좌측 상단에서 DFS 시작
if dfs(0, 0):
    print(1)  # 탈출 가능
else:
    print(0)  # 탈출 불가능
