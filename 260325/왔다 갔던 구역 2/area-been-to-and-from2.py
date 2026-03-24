n = int(input())
grid = [0] * 201  # OFFSET 100 기준, -100 ~ 100 범위를 커버
cur = 100         # 시작 위치 (OFFSET)

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    
    if direction == 'R':
        # 오른쪽으로 이동: 현재 위치부터 distance만큼 칸을 채움
        for i in range(cur, cur + distance):
            grid[i] += 1
        cur += distance # 이동 후 위치 갱신
    else:
        # 왼쪽으로 이동: (현재 위치 - distance)부터 현재 위치까지 칸을 채움
        for i in range(cur - distance, cur):
            grid[i] += 1
        cur -= distance # 이동 후 위치 갱신

# 2번 이상 겹친(값이 2 이상인) 구간의 개수 세기
ans = 0
for g in grid:
    if g >= 2:
        ans += 1

print(ans)