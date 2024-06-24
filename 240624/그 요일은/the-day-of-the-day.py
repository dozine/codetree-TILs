m1,d1,m2,d2=tuple(map(int,input().split()))
A=str(input())

def count(m,d):
    num_of_day=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    total_day=0
    for i in range(1,m+1):
        total_day+=num_of_day[i]
    total_day+=d
    return total_day

total_day=count(m2,d2)-count(m1,d1)+1
arr=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

cnt=total_day//7
for j in range(total_day%7):
    if arr[j]==A:
        cnt+=1
print(cnt)