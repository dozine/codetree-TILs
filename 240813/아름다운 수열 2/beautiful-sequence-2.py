n,m=tuple(map(int,input().split()))
a_sequence=list(map(int,input().split()))
b_sequence=list(map(int,input().split()))

cnt=0
for i in range(0,n-m+1):
    if sorted(a_sequence[i:i+m])==sorted(b_sequence):
        cnt+=1

print(cnt)