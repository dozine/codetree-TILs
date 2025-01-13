import sys
MAX_ANS = sys.maxsize

n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp= [0 for _ in range(m+1)]

def initialize():
    for i in range(m+1):
        dp[i] = MAX_ANS
    dp[0]=0

initialize()

for i in range(n):
    for j in range(m,-1,-1):
        if j >= coins[i]:
            if dp[j-coins[i]] == MAX_ANS:
                continue
            dp[j] = min(dp[j],dp[j-coins[i]]+1)

ans=dp[m]
if ans == MAX_ANS:
    ans = -1
print(ans)