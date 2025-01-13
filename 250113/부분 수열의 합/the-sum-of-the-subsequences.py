import sys
MAX_ANS = sys.maxsize

n, m = map(int, input().split())
A = list(map(int, input().split()))

dp= [False for _ in range(m+1)]

def initialize():
    for i in range(m+1):
        dp[i] = MAX_ANS
    dp[0]=0

initialize()

for i in range(n):
    for j in range(m,-1,-1):
        if j >= A[i]:
            if dp[j-A[i]] == MAX_ANS:
                continue
            dp[j] = min(dp[j],dp[j-A[i]]+1)

ans=dp[m]
if ans == MAX_ANS:
    ans = "No"
else: 
    ans="Yes"
print(ans)