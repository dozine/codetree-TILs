# import sys

# n = int(sys.stdin.readline().strip())
# segments = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# segments.sort()

# max_count = 0  
# selected = []  

# def backtrack(idx, count):
#     global max_count

#     if idx == n:
#         max_count = max(max_count, count)
#         return
    
#     x1, x2 = segments[idx]
#     if all(sel_x2 < x1 for sel_x1, sel_x2 in selected):
#         selected.append((x1, x2))
#         backtrack(idx + 1, count + 1)
#         selected.pop() 
    
#     backtrack(idx + 1, count)
# backtrack(0, 0)

# print(max_count)


# 변수 선언 및 입력:

# n = int(input())
# segments = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]

# ans = 0
# selected_segs = list()


# def overlapped(seg1, seg2):
#     (ax1, ax2), (bx1, bx2) = seg1, seg2

#     # 두 선분이 겹치는지 여부는
#     # 한 점이 다른 선분에 포함되는 경우로 판단 가능합니다. 
#     return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
#            (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)


# def possible():
#     # 단 한쌍이라도 선분끼리 겹치면 안됩니다
#     for i, seg1 in enumerate(selected_segs):
#         for j, seg2 in enumerate(selected_segs):
#             if i < j and overlapped(seg1, seg2):
#                 return False

#     return True


# def find_max_segments(cnt):
#     global ans
    
#     if cnt == n:
#         if possible():
#             ans = max(ans, len(selected_segs))
#         return
    
#     selected_segs.append(segments[cnt])
#     find_max_segments(cnt + 1)
#     selected_segs.pop()
    
#     find_max_segments(cnt + 1)


# find_max_segments(0)
# print(ans)


n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
selected = []

def is_valid(new_seg):
    """ 새로 추가할 선분이 기존 선택된 선분들과 겹치는지 확인 """
    x1, x2 = new_seg
    for sx1, sx2 in selected:
        if not (sx2 < x1 or x2 < sx1):  # 겹치면 False 반환
            return False
    return True

def backtrack(idx):
    global ans

    if idx == n:
        ans = max(ans, len(selected))
        return

    # 현재 선분을 선택하는 경우 (겹치지 않을 때만)
    if is_valid(segments[idx]):
        selected.append(segments[idx])
        backtrack(idx + 1)
        selected.pop()  # 백트래킹 (원상 복구)

    # 현재 선분을 선택하지 않는 경우
    backtrack(idx + 1)

backtrack(0)
print(ans)
