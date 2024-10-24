n,m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
seq=[0 for _ in range(n)]


def happySequence():
    consecutive_count,max_ccnt=1,1
    for i in range(1,n):
        if seq[i-1]==seq[i]:
            consecutive_count+=1
        else:
            consecutive_count=1
        max_ccnt=max(max_ccnt,consecutive_count)
    return max_ccnt>=m

num_happy=0
for i in range(n):
    seq=arr[i][:]
    if happySequence():
        num_happy+=1
for j in range(n):
    for i in range(n):
        seq[i]=arr[i][j]
    if happySequence():
        num_happy+=1
print(num_happy)