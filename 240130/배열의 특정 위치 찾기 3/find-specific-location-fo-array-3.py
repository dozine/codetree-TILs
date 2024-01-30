arr=list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    if arr[i] == 0 and i>=3:
        break
print(arr[i-3]+arr[i-2]+arr[i-1])