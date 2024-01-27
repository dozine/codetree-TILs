arr=list(map(int,input().split()))
sum=0
cnt=0
for i in arr:
    if i>=250:
        break 
    sum += i
    cnt += 1
avg=sum/cnt
print(f'{sum} {avg:.1f}')