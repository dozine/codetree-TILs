def solution():
    # 입력 받기
    n, m, x, y = map(int, input().split())
    x, y = x-1, y-1  # 0-based 인덱스로 변환
    
    # 격자 초기화
    grid = [[0] * n for _ in range(n)]
    
    # 명령어 입력
    commands = input().split()
    
    # 주사위 초기 상태 [위, 아래, 앞, 뒤, 왼쪽, 오른쪽]
    dice = [1, 6, 2, 5, 4, 3]
    
    # 이동 방향 정의 (동서북남)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # 현재 위치에 주사위 바닥면 값 표시
    grid[x][y] = dice[1]  # 아래면
    
    for cmd in commands:
        # 이동 방향 결정
        if cmd == 'R': dir = 0
        elif cmd == 'L': dir = 1
        elif cmd == 'U': dir = 2
        else: dir = 3
        
        # 다음 위치 계산
        nx, ny = x + dx[dir], y + dy[dir]
        
        # 격자를 벗어나면 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        # 주사위 굴리기
        temp = dice[:]
        if cmd == 'R':  # 동쪽
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
        elif cmd == 'L':  # 서쪽
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
        elif cmd == 'U':  # 북쪽
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
        else:  # 남쪽
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
        
        # 위치 업데이트
        x, y = nx, ny
        # 현재 위치에 주사위 바닥면 값 표시
        grid[x][y] = dice[1]
    
    return sum(sum(row) for row in grid)

print(solution())