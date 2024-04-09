Max_t=1000000
n,m=tuple(map(int,input().split()))
a,b=[0]*(Max_t+1),[0]*(Max_t+1)

time_a=1
for _ in range(n):
    d,t =tuple(input().split())
    for _ in range(int(t)):
        a[time_a]=a[time_a-1]+(1 if d =='R' else -1)
        time_a +=1


time_b=1
for _ in range(m):
    d,t =tuple(input().split())
    for _ in range(int(t)):
        b[time_b]=b[time_b-1]+(1 if d =='R' else -1)
        time_b +=1

ans=-1
for i in range(1,time_a):
    if a[i] ==b[i]:
        ans=i
        break 
print(ans)