n, m = map(int, input().split())

grid = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


def adjacent(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy 
        
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
            
    return cnt


for _ in range(m):
    r, c = map(int, input().split())
    
    grid[r][c] = 1
    
    if adjacent(r, c) == 3:
        print(1)
    else:
        print(0)