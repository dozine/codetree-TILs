# 변수 선언 및 입력
n = int(input())

# 시작 위치를 기록합니다.
x, y = 0, 0

# 동, 서, 남, 북 순으로 dxs, dys를 정의합니다.
dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

# 답을 저장합니다. (원점에 도달하지 못하면 -1 출력)
ans = -1

# 지금까지 걸린 시간을 기록합니다.
elapsed_time = 0

# 원점 도달 여부를 체크할 플래그 변수
is_returned = False

# N개의 명령을 하나씩 처리합니다.
for _ in range(n):
    c_dir, dist = input().split()
    dist = int(dist)
    
    # 각 방향에 맞는 dxs, dys의 인덱스(번호)를 붙여줍니다.
    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    # 주어진 방향(move_dir)으로 dist만큼 1칸씩 실제로 이동해봅니다.
    for _ in range(dist):
        x = x + dxs[move_dir]
        y = y + dys[move_dir]
        
        # 이동할 때마다 시간을 1씩 더합니다.
        elapsed_time += 1

        # 이동한 후, 현재 위치가 시작점(0, 0)인지 확인합니다.
        if x == 0 and y == 0:
            ans = elapsed_time
            is_returned = True
            break  # 1칸씩 움직이는 이 내부 루프를 탈출합니다.

    # 만약 원점에 도달해서 내부 루프가 break 되었다면, 
    # 전체 명령을 처리하는 바깥쪽 루프도 종료합니다.
    if is_returned:
        break

print(ans)