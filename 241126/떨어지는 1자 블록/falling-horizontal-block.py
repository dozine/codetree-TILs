# n,m,k=tuple(map(int,input().split()))
# grid =[
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

# def all_bank(row,col_s,col_e):
#     return all([
#         not grid[row][col]
#         for col in range(col_s,col_e+1)
#     ])

# def get_target_row():
#     for row in range(n-1):
#         if not all_bank(row+1,k,k+m-1):
#             return row
    
#     return n-1

# k-=1

# target_row =get_target_row()

# for col in range(k,k+m):
#     grid[target_row][col]=1

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j],end=" ")
#     print()

# 입력 처리
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

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
