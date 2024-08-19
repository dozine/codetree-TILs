import sys 
INT_MAX=sys.maxsize

n=int(input())
points=[
    tuple(map(int,input().split()))
    for _ in range(n)
]

def diff(i,j):
    x1,y1=points[i]
    x2,y2=points[j]
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)


ans=INT_MAX
for i in range(n):
    for j in range(i+1,n):
        ans=min(ans,diff(i,j))
print(ans)