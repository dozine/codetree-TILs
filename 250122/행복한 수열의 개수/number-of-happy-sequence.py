n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 행 체크
for i in range(n):
    row = 1  # 각 행을 시작할 때 초기화
    for j in range(1, n):
        if grid[i][j] == grid[i][j-1]:
            row += 1
        else:
            row = 1  # 연속되지 않으면 1로 초기화
        if row >= m:  # m개 이상이면
            cnt += 1
            break  # 이미 행복한 수열임이 확인되었으므로 다음 행으로

# 열 체크
for j in range(n):
    col = 1  # 각 열을 시작할 때 초기화
    for i in range(1, n):
        if grid[i][j] == grid[i-1][j]:
            col += 1
        else:
            col = 1  # 연속되지 않으면 1로 초기화
        if col >= m:  # m개 이상이면
            cnt += 1
            break  # 이미 행복한 수열임이 확인되었으므로 다음 열로

print(cnt)