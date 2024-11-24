def move_and_merge(board, direction):
    N = 4
    new_board = [[0] * N for _ in range(N)]
    
    # 방향에 따라 순회 방향 결정
    if direction == 'L':
        ranges = [(i, j) for i in range(N) for j in range(N)]
    elif direction == 'R':
        ranges = [(i, j) for i in range(N) for j in range(N-1, -1, -1)]
    elif direction == 'U':
        ranges = [(i, j) for j in range(N) for i in range(N)]
    elif direction == 'D':
        ranges = [(i, j) for j in range(N) for i in range(N-1, -1, -1)]
    
    # 보드를 회전하여 모든 방향의 처리를 왼쪽 이동으로 통일
    rotated = board
    if direction == 'R':
        rotated = [row[::-1] for row in board]
    elif direction == 'U':
        rotated = [[board[j][i] for j in range(N)] for i in range(N)]
    elif direction == 'D':
        rotated = [[board[j][i] for j in range(N-1, -1, -1)] for i in range(N)]
    
    # 각 행에 대해 처리
    result = []
    for row in rotated:
        # 0이 아닌 숫자들만 추출
        numbers = [x for x in row if x != 0]
        merged = []
        i = 0
        
        # 같은 숫자 합치기
        while i < len(numbers):
            if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
                merged.append(numbers[i] * 2)
                i += 2
            else:
                merged.append(numbers[i])
                i += 1
        
        # 결과 행의 길이를 4로 맞추기
        merged.extend([0] * (N - len(merged)))
        result.append(merged)
    
    # 방향에 따라 결과를 원래 방향으로 되돌리기
    if direction == 'R':
        result = [row[::-1] for row in result]
    elif direction == 'U':
        result = [[result[j][i] for j in range(N)] for i in range(N)]
    elif direction == 'D':
        result = [[result[j][i] for j in range(N-1, -1, -1)] for i in range(N)]
    
    return result

def main():
    # 입력 받기
    board = []
    for _ in range(4):
        row = list(map(int, input().split()))
        board.append(row)
    direction = input().strip()
    
    # 이동 및 병합 처리
    result = move_and_merge(board, direction)
    
    # 결과 출력
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()