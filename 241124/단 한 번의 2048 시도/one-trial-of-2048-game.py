def merge_line(line):
    """한 줄의 숫자를 병합하는 함수"""
    # 숫자를 오른쪽으로 밀어내기 위해 0을 제거하고 정렬
    filtered = [num for num in line if num != 0]
    merged = []
    skip = False

    for i in range(len(filtered)):
        if skip:  # 이전에 병합되었으면 건너뜀
            skip = False
            continue
        if i < len(filtered) - 1 and filtered[i] == filtered[i + 1]:
            # 두 숫자가 같으면 병합
            merged.append(filtered[i] * 2)
            skip = True
        else:
            merged.append(filtered[i])

    # 결과 리스트를 오른쪽으로 정렬
    while len(merged) < len(line):
        merged.append(0)

    return merged


def rotate_grid(grid, direction):
    """방향에 따라 grid를 회전"""
    if direction == 'L':  # 왼쪽: 그대로 처리
        return grid
    elif direction == 'R':  # 오른쪽: 모든 행을 뒤집음
        return [row[::-1] for row in grid]
    elif direction == 'U':  # 위쪽: 90도 반시계 회전
        return list(map(list, zip(*grid)))
    elif direction == 'D':  # 아래쪽: 90도 시계 회전
        return [list(reversed(row)) for row in zip(*grid)]


def undo_rotate_grid(grid, direction):
    """회전된 grid를 원래 방향으로 복원"""
    if direction == 'L':  # 왼쪽: 그대로 복원
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
