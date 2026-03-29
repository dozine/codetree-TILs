N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cnt = 0
ans = 0
for i in range(len(arr)):
    if i>=1 and arr[i-1] < arr[i]:
        cnt +=1
        ans = max(ans,cnt )
    else : 
        cnt = 1
        
print(ans)