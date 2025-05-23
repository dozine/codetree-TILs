# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# # 1. 처음 구간 합 계산
# window_sum = sum(arr[:k])
# max_sum = window_sum

# # 2. 슬라이딩 윈도우 돌리기
# for i in range(k, n):
#     window_sum = window_sum - arr[i - k] + arr[i]
#     max_sum = max(max_sum, window_sum)

# print(max_sum)

import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
ans = INT_MIN


# [s, e] 구간 내의 원소의 합을 반환합니다.
def get_sum(s, e):
    return prefix_sum[e] - prefix_sum[s - 1]


# 누적합 배열을 만들어줍니다.
prefix_sum[0] = 0
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

# 모든 구간에 대해 합을 찾아
# 그 중 최댓값을 갱신합니다.
for i in range(1, n - k + 2):
    ans = max(ans, get_sum(i, i + k - 1))

print(ans)
