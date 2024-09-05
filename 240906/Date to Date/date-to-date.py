m1,d1,m2,d2=tuple(map(int,input().split()))

days=[0,30,28,31,30,31,30,31,30,31,30,31,30,31]

day=0
for i in range(m1+1,m2):
    day+=days[i]
print(day+d2+(days[m1]-d1))