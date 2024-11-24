# NONE = -1

# # 변수 선언 및 입력
# n = 4
# grid = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
# next_grid = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]


# # grid를 시계방향으로 90' 회전시킵니다.
# def rotate():
#     # next_grid를 0으로 초기화합니다.
#     for i in range(n):
#         for j in range(n):
#             next_grid[i][j] = 0
    
#     # 90' 회전합니다.
#     for i in range(n):
#         for j in range(n):
#             next_grid[i][j] = grid[n - j - 1][i]
    
#     # next_grid를 grid에 옮겨줍니다.
#     for i in range(n):
#         for j in range(n):
#             grid[i][j] = next_grid[i][j]


# # 아래로 숫자들을 떨어뜨립니다.
# def drop():
#     # next_grid를 0으로 초기화합니다.
#     for i in range(n):
#         for j in range(n):
#             next_grid[i][j] = 0
    
#     # 아래 방향으로 떨어뜨립니다.
#     for j in range(n):
#         # 같은 숫자끼리 단 한번만
#         # 합치기 위해 떨어뜨리기 전에
#         # 숫자 하나를 keep해줍니다.
#         keep_num, next_row = NONE, n - 1
        
#         for i in range(n - 1, -1, -1):
#             if not grid[i][j]:
#                 continue
            
#             # 아직 떨어진 숫자가 없다면, 갱신해줍니다.
#             if keep_num == NONE:
#                 keep_num = grid[i][j];
            
#             # 가장 최근에 관찰한 숫자가 현재 숫자와 일치한다면
#             # 하나로 합쳐주고, keep 값을 비워줍니다.
#             elif keep_num == grid[i][j]:
#                 next_grid[next_row][j] = keep_num * 2
#                 keep_num = NONE
                
#                 next_row -= 1
            
#             # 가장 최근에 관찰한 숫자와 현재 숫자가 다르다면
#             # 최근에 관찰한 숫자를 실제 떨어뜨려주고, keep 값을 갱신해줍니다.
#             else:
#                 next_grid[next_row][j] = keep_num
#                 keep_num = grid[i][j]
                
#                 next_row -= 1
        
#         # 전부 다 진행했는데도 keep 값이 남아있다면
#         # 실제로 한번 떨어뜨려줍니다.
#         if keep_num != NONE:
#             next_grid[next_row][j] = keep_num
#             next_row -= 1
    
#     # next_grid를 grid에 옮겨줍니다.
#     for i in range(n):
#         for j in range(n):
#             grid[i][j] = next_grid[i][j]


# # move_dir 방향으로 기울이는 것을 진행합니다.
# # 회전을 규칙적으로 하기 위해
# # 아래, 오른쪽, 위, 왼쪽 순으로 dx, dy 순서를 가져갑니다.
# def tilt(move_dir):
#     # Step 1.
#     # move_dir 횟수만큼 시계방향으로 90'회전하는 것을 반복하여
#     # 항상 아래로만 숫자들을 떨어뜨리면 되게끔 합니다.
#     for _ in range(move_dir):
#         rotate()

#     # Step 2.
#     # 아래 방향으로 떨어뜨립니다.
#     drop()
    
#     # Step 3.
#     # 4 - move_dir 횟수만큼 시계방향으로 90'회전하는 것을 반복하여
#     # 처음 상태로 돌아오게 합니다. (총 360' 회전)
#     for _ in range(4 - move_dir):
#         rotate()


# dir_char = input()

# # 아래, 오른쪽, 위, 왼쪽 순으로 
# # mapper를 지정합니다.
# dir_mapper = {
#     'D': 0,
#     'R': 1,
#     'U': 2,
#     'L': 3
# }

# # 기울입니다.
# tilt(dir_mapper[dir_char])

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end=" ")
#     print()



# grid = [
#     list(map(int,input().split()))
#     for _ in range(4)
# ]

# def rotate_grid(grid, direction):
#     if direction =='L':
#         return grid 
#     if direction =='R':
#         return []
def merge_line(line):
    """한 줄을 병합하여 정렬한 결과를 반환"""
    filtered = [num for num in line if num != 0]  # 0을 제외한 숫자 리스트
    merged = []
    i = 0

    while i < len(filtered):
        # 병합 가능하다면
        if i < len(filtered) - 1 and filtered[i] == filtered[i + 1]:
            merged.append(filtered[i] * 2)  # 병합된 값 추가
            i += 2  # 병합된 숫자는 건너뜀
        else:
            merged.append(filtered[i])  # 그대로 추가
            i += 1

    # 0으로 채워 길이를 원래대로 맞춤
    while len(merged) < len(line):
        merged.append(0)

    return merged


def rotate_grid(grid, direction):
    """격자를 방향에 따라 회전"""
    if direction == 'L':  # 왼쪽: 그대로 처리
        return grid
    elif direction == 'R':  # 오른쪽: 모든 행을 뒤집음
        return [row[::-1] for row in grid]
    elif direction == 'U':  # 위쪽: 90도 반시계 회전
        return list(map(list, zip(*grid)))
    elif direction == 'D':  # 아래쪽: 90도 시계 회전
        return [list(reversed(row)) for row in zip(*grid)]


def undo_rotate_grid(grid, direction):
    """회전된 격자를 원래 방향으로 복원"""
    if direction == 'L':  # 왼쪽: 그대로 반환
        return grid
    elif direction == 'R':  # 오른쪽: 모든 행을 다시 뒤집음
        return [row[::-1] for row in grid]
    elif direction == 'U':  # 위쪽: 90도 시계 회전
        return [list(reversed(row)) for row in zip(*grid)]
    elif direction == 'D':  # 아래쪽: 90도 반시계 회전
        return list(map(list, zip(*grid)))


def solve_2048(grid, direction):
    # 입력 grid를 방향에 따라 회전
    rotated_grid = rotate_grid(grid, direction)

    # 각 행을 병합 처리
    merged_grid = [merge_line(row) for row in rotated_grid]

    # 회전된 결과를 원래 방향으로 복원
    final_grid = undo_rotate_grid(merged_grid, direction)
    return final_grid


# 입력 처리
grid = [list(map(int, input().split())) for _ in range(4)]
direction = input().strip()

# 문제 해결
result = solve_2048(grid, direction)

# 출력
for row in result:
    print(' '.join(map(str, row)))
