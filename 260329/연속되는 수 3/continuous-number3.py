n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 1
ans = 1

for i in range(1,len(arr)):
    if arr[i-1]*arr[i] > 0:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 1
print(ans)