arr = list(map(int, input().split()))
cnt=0

for i in arr:
    if i==0:
        break 
    cnt+=1

for j in range(cnt-1,-1,-1):
    print(arr[j],end=" ")