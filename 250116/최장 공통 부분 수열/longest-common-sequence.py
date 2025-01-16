A = input()
B = input()

# 문자열 길이
len_a = len(A)
len_b = len(B)

# DP 배열 초기화
dp = [[0 for _ in range(len_b + 1)] for _ in range(len_a + 1)]

# DP 테이블 채우기
for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if A[i - 1] == B[j - 1]:  # 현재 문자가 같다면
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 현재 문자가 다르다면
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 결과 출력
print(dp[len_a][len_b])
