offset=100
max_r=200
n=int(input())
rects=[
    tuple(map(int,input().split()))
    for _ in range(n)
]
checked = [
    [0] * (max_r+1)
    for _ in range(max_r+1)
]
for x1,y1,x2,y2 in rects:
    x1,y1 =x1+offset,y1+offset
    x2,y2 =x2+offset,y2+offset
    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y]=1
area=0
for x in range(0,max_r+1):
    for y in range(0,max_r+1):
        if checked[x][y]:
            area+=1
print(area)