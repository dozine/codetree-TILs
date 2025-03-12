# from collections import deque

# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]

# visited = [
#    [False for _ in range(m)]
#    for _ in range(n)
# ]
# q=deque()

# def in_range(x,y):
#     return 0<=x and x<n and 0<=y and y<m

# def can_go(x,y):
#     return in_range(x,y) and a[x][y] and not visited[x][y]


# def bfs():
#     while q: 
#         x,y=q.popleft()
#         dxs,dys=[0,1,0,-1],[1,0,-1,0]
#         for dx,dy in zip(dxs,dys):
#             nx,ny=dx+x, dy+y
#             if can_go(nx,ny):
#                 q.append((nx,ny))
#                 visited[nx][ny]=True

# q.append((0,0))
# visited[0][0]=True
# bfs()
# answer = 1 if visited[n-1][m-1] else 0 
# print(answer)

n=int(input())
grid= [
    list(map(int,input().split()))
    for _ in range(n)
]

visited=[
    [False for _ in range(n)]
    for _ in range(n) 
]

max_block, bomb_cnt = 0, 0
curr_block_num=0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,color):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y]!=color:
    #이미 방문 했거나 해당 숫자가 아니면 False 
        return False
    return True

def dfs(x,y):
    global curr_block_num
    dxs,dys=[0,1,0,-1], [1,0,-1,0]
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx,y+dy
        if can_go(nx,ny,grid[x][y]):
            visited[nx][ny] = True
            curr_block_num += 1
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            visited[i][j]=True
            curr_block_num = 1
            dfs(i,j)
            if curr_block_num >= 4:
                bomb_cnt+=1
            max_block=max(max_block,curr_block_num)
print(bomb_cnt,max_block)