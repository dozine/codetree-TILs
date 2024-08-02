r,c=tuple(map(int,input().split()))
arr=[
    input().split()
    for _ in range(r)
]
cnt=0
for i in range(1,c):
    for j in range(1,r):
        for k in range(i+1,c-1):
            for l in range(j+1,r-1):
                if arr[0][0] != arr[i][j] and \
                   arr[i][j] != arr[k][l] and \
                   arr[k][l] != arr[r-1][c-1]:
                    cnt+=1
print(cnt)