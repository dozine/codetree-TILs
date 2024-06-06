a=input()
n=len(a)

cnt=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]=="(" and a[j]==")":
            cnt+=1
print(cnt)