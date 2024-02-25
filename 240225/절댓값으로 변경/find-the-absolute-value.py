N=int(input())
nn=list(map(int,input().split()))

def function(nn):
    for i in range(N):
        if nn[i]<0:
            nn[i]=-nn[i]
    return 

function(nn)
for i in nn:
    print(i,end=" ")