n = int(input())

# Write your code here!
MAX_N=1000
dp=[0]*MAX_N

dp[0]=1
dp[1]=2
dp[2]=7
dp[3]=22

for i in range(4,n+1):
    dp[i] = dp[i-2]+dp[i-3]

print(dp[n]%10007)