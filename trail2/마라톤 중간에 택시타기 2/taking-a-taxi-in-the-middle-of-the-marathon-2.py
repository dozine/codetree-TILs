# import sys 
# INT_MAX=sys.maxsize

# n=int(input())
# arr=[
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

# ans=INT_MAX
# for i in range(1,n-1):
#     dist=0
#     prev_idx=0
#     for j in range(1,n):
#         if j == i:
#             continue
#         dist+=abs(arr[prev_idx][0]-arr[j][0])+abs(arr[prev_idx][1]-arr[j][1])
#         prev_idx=j
#     ans=min(ans,dist)
# print(ans)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


min_dis = float('inf')

for j in range(1, n - 1):  # 건너뛸 위치

    distance = 0

    for i in range(n - 1):  # 현재 위치

        if i == j:
            continue

        if i + 1 == j:
            distance += manhattan_distance(
                arr[i][0], arr[i][1],
                arr[i + 2][0], arr[i + 2][1]
            )
        else:
            distance += manhattan_distance(
                arr[i][0], arr[i][1],
                arr[i + 1][0], arr[i + 1][1]
            )

    min_dis = min(min_dis, distance)

print(min_dis)