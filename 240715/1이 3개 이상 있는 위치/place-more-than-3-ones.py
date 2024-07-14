n=in(input())
arr=[
    tuple(map(int,input().split()))
    for _ in range(n)
]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def in_range(x,y):
    return 0 <=x and x<n and 0 <=y and y<nx

def adjacent_cnt(x,y):
    cnt=0
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx,y+dy
        if in_range(nx,ny) and arr[nx][ny] ==1:
            cnt+=1
    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i, j) >= 3:
            ans += 1
    
print(ans)