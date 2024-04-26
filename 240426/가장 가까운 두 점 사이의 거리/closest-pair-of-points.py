import sys
INT_MAX=sys.maxsize
n=int(input())
arr=[
    tuple(map(int,input().split()))
    for _ in range(n)
]

def dist(i,j):
    x1,y1 =arr[i]
    x2,y2 =arr[j]
    return (x1-x2) * (x1-x2) +(y1-y2) * (y1-y2) 

min_dist=INT_MAX
for i in range(n):
    for j in range(i+1,n):
        min_dist = min(min_dist, dist(i,j))
print(min_dist)