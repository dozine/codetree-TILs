import sys

n = int(sys.stdin.readline().strip())
segments = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 정렬 (시작점 기준)
segments.sort()

max_count = 0  # 최대 선택 가능한 선분 개수
selected = []  # 현재 선택된 선분 리스트

def backtrack(idx, count):
    global max_count

    # 모든 선분을 검사한 경우, 최댓값 갱신
    if idx == n:
        max_count = max(max_count, count)
        return
    
    x1, x2 = segments[idx]
    
    # 현재 선분이 기존 선택된 선분과 겹치는지 확인
    if all(sel_x2 < x1 for sel_x1, sel_x2 in selected):
        # 겹치지 않으면 선택
        selected.append((x1, x2))
        backtrack(idx + 1, count + 1)
        selected.pop()  # 백트래킹 (원상 복구)

    # 현재 선분을 선택하지 않는 경우도 탐색
    backtrack(idx + 1, count)

# 백트래킹 시작
backtrack(0, 0)

print(max_count)
