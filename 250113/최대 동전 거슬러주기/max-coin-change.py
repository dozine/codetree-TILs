# import sys
# INT_MIN = -sys.maxsize
# n,m = map(int, input().split())
# coin = list(map(int, input().split()))

# # Write your code here!
# dp=[INT_MIN for _ in range(m+1)]
# dp[0]=0

# for i in range(1,m+1):
#     for j in range(n):
#         if i >= coin[j-1]:
#             dp[i] = max(dp[i],dp[i-coin[j]]+1)

# ans=dp[m]
# if ans==INT_MIN:
#     ans=-1
# print(ans)
import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())  # 동전의 개수와 목표 금액
coin = list(map(int, input().split()))  # 동전 배열

# dp 배열 초기화
dp = [INT_MIN for _ in range(m + 1)]
dp[0] = 0  # 금액 0을 만드는 경우는 0개 동전 사용

# 동전 종류 순회
for c in coin:
    for i in range(c, m + 1):  # 현재 동전으로 만들 수 있는 금액부터 계산
        if dp[i - c] != INT_MIN:  # 이전 금액이 만들 수 있는 경우라면
            dp[i] = max(dp[i], dp[i - c] + 1)

# 결과 출력
ans = dp[m]
if ans == INT_MIN:
    ans = -1
print(ans)
