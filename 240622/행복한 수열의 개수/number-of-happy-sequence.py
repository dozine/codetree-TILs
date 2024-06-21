n,m=tuple(map(int,input().split()))
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
seq = [0 for _ in range(n)]

def happysequence():
    cnt,max_cnt=1,1
    for i in range(1,n):
        if seq[i-1]==seq[i]:
            cnt +=1
        else:
            cnt=1
        max_cnt=max(max_cnt,cnt)
    return max_cnt>=m

num_happy=0
for i in range(n):
    seq=grid[i][:]
    if happysequence():
        num_happy+=1

for j in range(n):
    for i in range(n):
        seq[i]=grid[i][j]
    if happysequence():
        num_happy+=1
print(num_happy)