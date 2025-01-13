n = int(input())  
arr = [1, 2, 5]   


dp = [0 for _ in range(n+1)]
dp[0]=1

# 동적 프로그래밍 진행
for i in range(1,n+1):
    for j in range(3):
        if i>=arr[j]:
            dp[i] = (dp[i]+dp[i-arr[j]]) % 10007
print(dp[n]) 