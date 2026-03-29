n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

cnt = 1
maxx = 0
for i in range(1, len(arr)):
    if arr[i-1]==arr[i]:
        cnt +=1 
        maxx = max(cnt,maxx )

print(cnt)
