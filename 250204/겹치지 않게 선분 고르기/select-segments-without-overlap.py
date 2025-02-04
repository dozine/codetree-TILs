import sys

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 끝점 기준으로 정렬 (Greedy 기법과 결합)
segments.sort(key=lambda x: x[1])

# 선택된 선분 목록
selected = []
max_count = 0

def can_select(x1, x2):
    """현재 선택된 선분들과 겹치지 않는지 확인"""
    return all(x2 <= s1 or x1 >= s2 for s1, s2 in selected)

def backtrack(idx, count):
    global max_count

    # 모든 선분을 확인한 경우
    if idx == n:
        max_count = max(max_count, count)
        return

    x1, x2 = segments[idx]

    # 1️⃣ 현재 선분을 선택하는 경우
    if can_select(x1, x2):
        selected.append((x1, x2))  # 선택
        backtrack(idx + 1, count + 1)
        selected.pop()  # 원상 복구

    # 2️⃣ 현재 선분을 선택하지 않는 경우
    backtrack(idx + 1, count)

# 백트래킹 시작
backtrack(0, 0)
print(max_count)
