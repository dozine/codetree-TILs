n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

ans=0
for i in range(1,n):
    if arr[i-1]==0:
        ans+=1
        arr[i-1]=1
        arr[i]^=1
        if i+1 < n:
            arr[i+1]^=1

if arr[n-1]==0:
    ans=-1

print(ans)