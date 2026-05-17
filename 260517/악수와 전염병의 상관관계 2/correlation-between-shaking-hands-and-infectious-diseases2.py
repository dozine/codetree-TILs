import sys

# 1. 입력 받기
n, k, p, t = map(int, sys.stdin.readline().split())

# 악수 정보 저장 (t, x, y)
handshakes = []
for _ in range(t):
    time, x, y = map(int, sys.stdin.readline().split())
    handshakes.append((time, x, y))

# 2. 시간(time) 순으로 정렬 (가장 중요!)
handshakes.sort(key=lambda x: x[0])

# 3. 개발자들의 상태 배열 초기화 (1번부터 N번까지 쓰기 위해 N+1 크기)
infected = [False] * (n + 1)
shake_num = [0] * (n + 1)

# 최초 감염자 P 설정
infected[p] = True
shake_num[p] = k

# 4. 시간 순으로 악수 진행
for time, x, y in handshakes:
    # 악수하는 순간의 두 사람의 감염 상태를 미리 복사 (동시 처리를 위해)
    x_infected = infected[x]
    y_infected = infected[y]
    
    # X가 Y에게 전염시키는 경우
    if x_infected and shake_num[x] > 0:
        if not infected[y]:
            infected[y] = True
            shake_num[y] = k
        # 이미 걸려있든 새로 걸리든 X의 전염 횟수는 깎임
        shake_num[x] -= 1
        
    # Y가 X에게 전염시키는 경우 (위의 스냅샷 x_infected, y_infected 기준)
    if y_infected and shake_num[y] > 0:
        if not infected[x]:
            infected[x] = True
            shake_num[x] = k
        # 이미 걸려있든 새로 걸리든 Y의 전염 횟수는 깎임
        shake_num[y] -= 1

# 5. 출력 양식에 맞게 0과 1로 출력
for i in range(1, n + 1):
    if infected[i]:
        print(1, end="")
    else:
        print(0, end="")
print()