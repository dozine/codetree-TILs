n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
r,c=map(int,input().split())
r,c=r-1,c-1

def bomb(grid,n,r,c):
    point=grid[r][c]
    grid[r][c] = 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for direction in range(4):
        for step in range(1,point):
            nx=r+dx[direction]*step
            ny=c+dy[direction]*step
            if 0<=nx<n and 0 <=ny<n:
                grid[nx][ny]=0
    
    for col in range(n):
        new_col = [grid[row][col] for row in range(n) if grid[row][col] !=0]
        new_col =[0]*(n-len(new_col))+new_col
        for row in range(n):
            grid[row][col]=new_col[row]
    return grid
    
result=bomb(grid,n,r,c)
for row in result:
    print(" ".join(map(str,row)))
