n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
# 특정 행이 비어 있는지 확인
def is_empty(row, col_start, col_end):
    for col in range(col_start, col_end + 1):
        if grid[row][col] == 1:  # 이미 블록이 있다면 False
            return False
    return True  # 모두 비어 있으면 True

# 블록이 멈출 행 찾기
def find_target_row():
    for row in range(n - 1):  # 위에서부터 마지막-1 행까지 확인
        if not is_empty(row + 1, k, k + m - 1):  # 다음 행이 비어 있지 않으면 멈춤
            return row
    return n - 1  # 끝까지 비어 있다면 마지막 행에서 멈춤

# 블록을 놓기
k -= 1  # 1-based -> 0-based
target_row = find_target_row()
for col in range(k, k + m):
    grid[target_row][col] = 1

# 결과 출력
for row in grid:
    print(" ".join(map(str, row)))
