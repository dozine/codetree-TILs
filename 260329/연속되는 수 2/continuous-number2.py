n = int(input())
if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    cnt = 1
    maxx = 1
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            cnt = 1
        
        if cnt > maxx:
            maxx = cnt

    print(maxx)