n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def in_range(x,y):
    return 0<=x<n and 0<=y<n

ans=0
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(i,i+3):
            for l in range(j,j+3):
                if in_range(k,l) and grid[k][l]:
                    cnt+=1
                ans=max(ans,cnt)
print(ans)