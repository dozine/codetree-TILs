# import sys
# INT_MAX=sys.maxsize

# n=int(input())
# arr=[
#     int(input())
#     for _ in range(n)
# ]
# min_dist=INT_MAX
# for i in range(n):
#     sum_dist=0
#     for j in range(n):
#         dist=(j+n-i)%n
#         sum_dist+=dist*arr[j]
#     min_dist=min(min_dist,sum_dist)
# print(min_dist)

# for i in range(n):
#     sum_dist=0
#     for j in range(n):
#         dist=(j+n-i)%n
#         sum_dist+=dist*arr[j]
#     min_dist=min(min_dist,sum_dist)



n = int(input())

people = [
    int(input())
    for _ in range(n)
]

ans = float('inf')

for i in range(n):  # 시작점
    dis = 0
    for j in range(n):  # 각 방
        # i에서 j까지 시계 반대방향으로 이동하는 거리
        distance = (j - i) % n
        dis += people[j] * distance
    ans = min(ans, dis)
print(ans)


