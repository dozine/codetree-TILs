import sys
INT_MIN = -sys.maxsize
n,m = map(int, input().split())
coin = list(map(int, input().split()))

# Write your code here!
dp=[INT_MIN for _ in range(m+1)]
dp[0]=0

for i in range(1,m+1):
    for j in range(n):
        if i >= coin[j-1]:
            dp[i] = max(dp[i],dp[i-coin[j]]+1)

ans=dp[m]
if ans==INT_MIN:
    ans=-1
print(ans)
