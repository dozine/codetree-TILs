def is_happy_sequence(arr, m):
    max_count = 1  # 현재까지의 최대 연속 길이
    count = 1      # 현재 연속 길이
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    
    return max_count >= m

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
happy_count = 0

# 행 체크
for row in grid:
    if is_happy_sequence(row, m):
        happy_count += 1

# 열 체크
for j in range(n):
    column = [grid[i][j] for i in range(n)]
    if is_happy_sequence(column, m):
        happy_count += 1

print(happy_count)