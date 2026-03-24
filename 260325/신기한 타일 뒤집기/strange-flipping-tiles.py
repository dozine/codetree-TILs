n = int(input())

# 1. 충분한 크기의 리스트와 시작점(OFFSET) 설정
# 명령 1000개 * 거리 100 = 최대 10만 이동 가능하므로 20만 칸 확보
grid = [0] * 200001  
cur = 100000        

for _ in range(n):
    line = input().split()
    if not line: break
    distance, direction = int(line[0]), line[1]
    
    if direction == 'R':
        # 오른쪽으로 뒤집기: 현재 위치(cur)부터 distance만큼 (검은색: 2)
        # 예: 현재 100에서 3R이면 100, 101, 102를 칠함
        for i in range(cur, cur + distance):
            grid[i] = 2
        # 마지막으로 뒤집은 타일(cur + distance - 1)에 서있기
        cur = cur + distance - 1
    else:
        # 왼쪽으로 뒤집기: 현재 위치(cur)부터 왼쪽으로 distance만큼 (흰색: 1)
        # 예: 현재 100에서 3L이면 100, 99, 98을 칠함
        for i in range(cur - distance + 1, cur + 1):
            grid[i] = 1
        # 마지막으로 뒤집은 타일(cur - distance + 1)에 서있기
        cur = cur - distance + 1

# 2. 결과 집계 (흰색: 1, 검은색: 2)
white_ans = 0
black_ans = 0
for g in grid:
    if g == 1:
        white_ans += 1
    elif g == 2:
        black_ans += 1

print(white_ans, black_ans)