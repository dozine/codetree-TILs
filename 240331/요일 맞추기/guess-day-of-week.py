m1, d1, m2, d2= tuple(map(int,input().split()))
weekday=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days=[0,31,28,31,30,31,30,31,30,31,30,31,30]

def function(m,d):
    days=[0,31,28,31,30,31,30,31,30,31,30,31,30]
    total_days=0
    for i in range(1,m):
        total_days +=days[i]
    
    total_days +=d
    return total_days 

diff = function(m2,d2)-function(m1,d1)
while diff<0:
    diff +=7

print(weekday[diff%7])