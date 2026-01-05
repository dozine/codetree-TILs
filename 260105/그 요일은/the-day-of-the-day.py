m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
total_days = 0 
for i in range(m1,m2):
    total_days+=days[i]
total_days = total_days + d2 - d1

weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
idx = weekday.index(A)
ans = (total_days - idx) // 7+1
print(ans)