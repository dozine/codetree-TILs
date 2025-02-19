n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

def can_go(x,y):
    if in_range(x,y) and grid[x][y]==1:
        return True

def dfs(x,y):
    dxs,dys=[0,1],[1,0]
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if can_go(nx,ny):
            visited[nx][ny]=1
            dfs(nx,ny)

visited[0][0]=1
dfs(0,0)

print(visited[n-1][m-1])