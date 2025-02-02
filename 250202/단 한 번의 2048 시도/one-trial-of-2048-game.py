# 격자 크기
N = 4

def print_grid(grid):
    for row in grid:
        print(*row)

def move_down(grid):
    # 새로운 격자 생성
    new_grid = [[0] * N for _ in range(N)]
    
    # 각 열별로 처리
    for col in range(N):
        # 1. 해당 열의 0이 아닌 숫자들을 모두 추출
        numbers = []
        for row in range(N-1, -1, -1):  # 아래에서부터 위로
            if grid[row][col] != 0:
                numbers.append(grid[row][col])
        
        # 2. 같은 숫자끼리 합치기
        merged = []
        i = 0
        while i < len(numbers):
            if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
                # 같은 숫자면 합쳐서 저장
                merged.append(numbers[i] * 2)
                i += 2
            else:
                # 다른 숫자면 그대로 저장
                merged.append(numbers[i])
                i += 1
        
        # 3. 합쳐진 숫자들을 아래에서부터 채우기
        for i, num in enumerate(merged):
            new_grid[N-1-i][col] = num
    
    return new_grid

def rotate_90(grid):
    # 시계 방향으로 90도 회전
    return [[grid[N-1-j][i] for j in range(N)] for i in range(N)]

def move(grid, direction):
    # 먼저 격자를 회전하여 모든 방향의 이동을 아래 방향 이동으로 변환
    if direction == 'L':  # 왼쪽으로 이동
        grid = rotate_90(rotate_90(rotate_90(grid)))
    elif direction == 'U':  # 위로 이동
        grid = rotate_90(rotate_90(grid))
    elif direction == 'R':  # 오른쪽으로 이동
        grid = rotate_90(grid)
    
    # 아래 방향으로 이동
    grid = move_down(grid)
    
    # 원래 방향으로 되돌리기
    if direction == 'L':
        grid = rotate_90(grid)
    elif direction == 'U':
        grid = rotate_90(rotate_90(grid))
    elif direction == 'R':
        grid = rotate_90(rotate_90(rotate_90(grid)))
    
    return grid

# 입력 처리
grid = [list(map(int, input().split())) for _ in range(N)]
direction = input().strip()

# 이동 실행
result = move(grid, direction)

# 결과 출력
print_grid(result)