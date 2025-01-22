n = int(input())
m = list(map(int, input().split()))

# Write your code here!
dp=[1 for _ in range(n+1)]

for i in range(n):
    for j in range(i):
        if m[i] < m[j]:
            dp[i] = max(dp[i],dp[j]+1)

# ans=0
# for i in range(n):
#     ans = max (ans, dp[i])
# print(ans)

print(max(dp))