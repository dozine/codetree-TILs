r, c = tuple(map(int, input().split()))
arr = [input().split() for _ in range(r)]

cnt = 0
for i in range(1, r-1):  # row loop should be from 1 to r-2
    for j in range(1, c-1):  # column loop should be from 1 to c-2
        for k in range(i+1, r-1):  # k should start from i+1 to r-2
            for l in range(j+1, c-1):  # l should start from j+1 to c-2
                if arr[0][0] != arr[i][j] and \
                   arr[i][j] != arr[k][l] and \
                   arr[k][l] != arr[r-1][c-1]:
                    cnt += 1

print(cnt)