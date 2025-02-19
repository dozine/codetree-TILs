import sys
INT_MIN=-sys.maxsize
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
dp=[
    [0 for _ in range(m)]
    for _ in range(n)
]

def initialize():
    for i in range(n):
        for j in range(m):
            dp[i][j]=INT_MIN
    dp[0][0]=1

initialize()

for i in range(n):
    for j in range(m):
        for k in range(i):
            for l in range(j):
                if dp[k][l]==INT_MIN:
                    continue
                if grid[k][l]<grid[i][j]:
                    dp[i][j]= max(dp[i][j],dp[k][l]+1)

ans = INT_MIN
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans)