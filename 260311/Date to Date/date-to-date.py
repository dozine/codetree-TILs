m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
ans = 0 
for i in days[m1:m2]:
    ans += i

ans = ans - d1 + d2 +1
print(ans)