# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Write your code here!

# def in_range(x,y):

# def positive_count(s_row,s_col,e_row,e_col):
#     cnt=0
#     for row in range(s_row,e_row):
#         for col in range(s_col,e_col):
#             if grid[row][col]<=0:
#                 break
#             else:
#                 cnt+=1
#     return cnt


# for i in range(n):
#     for j in range(n):
#         positive_count(i,j)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 범위 확인 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 주어진 시작점 (s_row, s_col)에서 가능한 직사각형 크기를 계산하는 함수
def positive_count(s_row, s_col):
    max_area = 0
    for e_row in range(s_row, n):  # 아래로 확장
        for e_col in range(s_col, m):  # 오른쪽으로 확장
            # 사각형 내부가 모두 양수인지 확인
            valid = True
            for row in range(s_row, e_row + 1):
                for col in range(s_col, e_col + 1):
                    if grid[row][col] <= 0:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                # 현재 사각형의 크기 계산
                area = (e_row - s_row + 1) * (e_col - s_col + 1)
                max_area = max(max_area, area)
            else:
                break  # 현재 범위에서 더 확장해도 유효하지 않음
    return max_area

# 전체 그리드에서 가능한 최대 직사각형 크기 계산
max_rectangle = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:  # 양수인 경우만 시작점으로 고려
            max_rectangle = max(max_rectangle, positive_count(i, j))

print(max_rectangle)
