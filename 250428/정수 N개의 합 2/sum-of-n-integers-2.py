n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 처음 구간 합 계산
window_sum = sum(arr[:k])
max_sum = window_sum

# 2. 슬라이딩 윈도우 돌리기
for i in range(k, n):
    window_sum = window_sum - arr[i - k] + arr[i]
    max_sum = max(max_sum, window_sum)

print(max_sum)
