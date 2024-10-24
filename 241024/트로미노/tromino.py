n, m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0

# 2x2 구역에서 최소값 제외한 합
for i in range(n-1):
    for j in range(m-1):
        arr_sum = (
            arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
        ) - min(arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1])
        max_sum = max(max_sum, arr_sum)

# 가로로 연속된 3개의 값 합산
for i in range(n):
    for j in range(m-2):
        arr_sum1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        max_sum = max(max_sum, arr_sum1)

# 세로로 연속된 3개의 값 합산
for i in range(n-2):
    for j in range(m):
        arr_sum2 = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        max_sum = max(max_sum, arr_sum2)

print(max_sum)