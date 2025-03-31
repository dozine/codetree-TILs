n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

dp=[
    [0 for _ in range(n)]
    for _ in range(n)
]

def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1,n):
        dp[i][0]=max(dp[i-1][0],grid[i][0])
    for j in range(1,n):
        dp[0][j]=max(dp[0][j-1],grid[0][j])

initialize()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=max(min(dp[i-1][j],dp[i][j-1]),grid[i][j])
print(dp[n-1][n-1])
# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # DP 배열 초기화
# dp = [[float('inf')] * n for _ in range(n)]

# # 초기값 설정 (시작점)
# dp[0][0] = grid[0][0]

# # 첫 번째 열 초기화
# for i in range(1, n):
#     dp[i][0] = max(dp[i-1][0], grid[i][0])

# # 첫 번째 행 초기화
# for j in range(1, n):
#     dp[0][j] = max(dp[0][j-1], grid[0][j])

# # DP 점화식
# for i in range(1, n):
#     for j in range(1, n):
#         dp[i][j] = min(
#             max(dp[i-1][j], grid[i][j]),  # 위쪽에서 오는 경로
#             max(dp[i][j-1], grid[i][j])   # 왼쪽에서 오는 경로
#         )

# # 결과 출력
# print(dp[n-1][n-1])
