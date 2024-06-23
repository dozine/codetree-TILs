m1,d1,m2,d2=tuple(map(int,input().split()))

def date(m,d):
    num_of_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    total_days=0
    for i in range(m):
        total_days+=num_of_days[i]
    total_days+=d
    return total_days

weekday=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
total_day=date(m2,d2)-date(m1,d1)
ans=weekday[total_day%7]
print(ans)