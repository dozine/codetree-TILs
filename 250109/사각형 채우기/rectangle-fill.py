n = int(input())

# Write your code here!
def square(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # 점화식 계산
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

print(square(n))