n,t=tuple(map(int,input().split()))
arr= list(map(int,input().split()))

cnt,ans=0,0
for i in range(n):
    if t<arr[i] and t<arr[i-1]:
        cnt+=1
    else:
        cnt=1
    ans=max(ans,cnt)
print(ans)