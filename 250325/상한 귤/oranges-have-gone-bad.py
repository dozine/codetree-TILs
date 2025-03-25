from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited=[
    [False for _ in range(n)]
    for _ in range(n)
]

step=[
    [0 for _ in range(n)]
    for _ in range(n)
]

s_pos=[
    (i,j)
    for i in range(n)
    for j in range(n)
    if grid[i][j]==2
]

q=deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y]

def push(nx,ny,new_step):
    q.append((nx,ny))
    visited[nx][ny]=True
    step[nx][ny]=new_step

def bfs():
    while q:
        x,y=q.popleft()
        dxs,dys=[0,1,0,-1],[1,0,-1,0]
        for dx,dy in zip(dxs,dys):
            nx,ny=dx+x,dy+y
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
    
                
for x, y in s_pos:
    push(x, y, 0)

bfs()


for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            print(-1, end=" ")
        else:
            if not visited[i][j]:
                print(-2, end=" ")
            else:
                print(step[i][j], end=" ")
    print()