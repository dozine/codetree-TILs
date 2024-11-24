def find_next_position(grid, n, curr_r, curr_c):
    # 상하좌우 방향 정의 (우선순위 순서대로)
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]
    
    current_value = grid[curr_r][curr_c]
    candidates = []  # (값, row, col) 형태로 저장
    
    # 모든 방향을 확인하고 현재 값보다 큰 값을 가진 위치 저장
    for i in range(4):
        new_r = curr_r + dr[i]
        new_c = curr_c + dc[i]
        
        # 격자 범위 내에 있고 현재 값보다 큰 경우
        if 0 <= new_r < n and 0 <= new_c < n:
            if grid[new_r][new_c] > current_value:
                # (값, 방향 인덱스, row, col) 형태로 저장
                candidates.append((grid[new_r][new_c], i, new_r, new_c))
    
    # 이동할 수 있는 위치가 없는 경우
    if not candidates:
        return -1, -1
        
    # 가능한 위치들 중 우선순위가 가장 높은 위치 선택
    # 1. 값이 같은 경우 방향 우선순위(상하좌우)를 따름
    # 2. 값이 다른 경우 더 작은 값을 선택
    candidates.sort(key=lambda x: (x[0], x[1]))
    return candidates[0][2], candidates[0][3]

def solve(grid, n, start_r, start_c):
    path = []
    curr_r, curr_c = start_r - 1, start_c - 1  # 0-based 인덱스로 변환
    
    # 시작 위치 추가
    path.append(grid[curr_r][curr_c])
    
    while True:
        # 다음 위치 찾기
        next_r, next_c = find_next_position(grid, n, curr_r, curr_c)
        
        # 더 이상 이동할 수 없으면 종료
        if next_r == -1 and next_c == -1:
            break
        
        # 경로에 추가하고 현재 위치 업데이트
        path.append(grid[next_r][next_c])
        curr_r, curr_c = next_r, next_c
    
    return path

def main():
    # 입력 받기
    n, start_r, start_c = map(int, input().split())
    
    # 격자 정보 입력 받기
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # 경로 찾기
    path = solve(grid, n, start_r, start_c)
    
    # 결과 출력
    print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()