n = int(input())
m = [0]+list(map(int, input().split()))

# Write your code here!

dp = [0 for _ in range(n+1)] 

for i in range(1,n+1):
    for j in range(i):
        if m[j] < m[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))


