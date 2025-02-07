n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Write your code here!


ans=0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,prev_num):
    return in_range(x,y) and num[x][y] > prev_num

def find_max(x,y,prev_num):
    global ans
    ans=max(ans,cnt)

    dxs=[-1,-1,0,1,1,1,0,-1]
    dys=[0,1,1,1,0,-1,-1,-1]
    d = move_dir[x][y]-1
    for i in range(n):
        nx,ny= x+dx[d]*i, y+dy[d]*i
        if can_go(nx,ny,num[x][y]):
            find_max(nx,ny,cnt+1)

find_max(r-1,c-1,0)
print(ans)