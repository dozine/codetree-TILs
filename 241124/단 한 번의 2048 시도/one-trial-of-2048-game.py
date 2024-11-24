def move_and_merge(board, direction):
    N = 4
    result = [[0] * N for _ in range(N)]
    
    if direction == 'D':
        for j in range(N):
            # Get all numbers in the column from top to bottom
            numbers = []
            for i in range(N):
                if board[i][j] != 0:
                    numbers.append(board[i][j])
            
            # Merge same adjacent numbers
            merged = []
            i = len(numbers) - 1
            while i >= 0:
                if i > 0 and numbers[i] == numbers[i-1]:
                    merged.append(numbers[i] * 2)
                    i -= 2
                else:
                    merged.append(numbers[i])
                    i -= 1
            merged.reverse()  # Reverse to maintain correct order
            
            # Fill the result column from bottom to top
            idx = N - 1
            for num in merged:
                result[idx][j] = num
                idx -= 1
    
    elif direction == 'U':
        for j in range(N):
            numbers = []
            for i in range(N):
                if board[i][j] != 0:
                    numbers.append(board[i][j])
            
            merged = []
            i = 0
            while i < len(numbers):
                if i < len(numbers) - 1 and numbers[i] == numbers[i+1]:
                    merged.append(numbers[i] * 2)
                    i += 2
                else:
                    merged.append(numbers[i])
                    i += 1
            
            # Fill the result column from top to bottom
            for i, num in enumerate(merged):
                result[i][j] = num
    
    elif direction == 'L':
        for i in range(N):
            numbers = []
            for j in range(N):
                if board[i][j] != 0:
                    numbers.append(board[i][j])
            
            merged = []
            j = 0
            while j < len(numbers):
                if j < len(numbers) - 1 and numbers[j] == numbers[j+1]:
                    merged.append(numbers[j] * 2)
                    j += 2
                else:
                    merged.append(numbers[j])
                    j += 1
            
            # Fill the result row from left to right
            for j, num in enumerate(merged):
                result[i][j] = num
    
    elif direction == 'R':
        for i in range(N):
            numbers = []
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    numbers.append(board[i][j])
            
            merged = []
            j = 0
            while j < len(numbers):
                if j < len(numbers) - 1 and numbers[j] == numbers[j+1]:
                    merged.append(numbers[j] * 2)
                    j += 2
                else:
                    merged.append(numbers[j])
                    j += 1
            
            # Fill the result row from right to left
            idx = N - 1
            for num in merged:
                result[i][idx] = num
                idx -= 1
    
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