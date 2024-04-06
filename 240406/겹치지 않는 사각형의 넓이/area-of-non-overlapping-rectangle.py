offset=1000
max_r=2000
n=3
rects=[
    tuple(map(int,input().split()))
    for _ in range(n)
]
checked =[
    [0]*(max_r+1)
    for _ in range(max_r +1)
]
for i, (x1,y1,x2,y2) in enumerate(rects, start =1):
    x1,y1=x1+offset,y1+offset
    x2,y2=x2+offset,y2+offset
    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y]=i

area = 0 
for x in range(0,max_r+1):
    for y in range(0,max_r+1):
        if checked[x][y] ==1 or checked[x][y]==2:
            area +=1
print(area)