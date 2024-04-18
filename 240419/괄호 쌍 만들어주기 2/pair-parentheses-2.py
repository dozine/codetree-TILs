a=input()
length=len(a)
cnt=0
for i in range(length-1):
    for j in range(i+1,length-1):
        if a[i]=='(' and a[i+1] =='(' and a[j]==')' and a[j+1]==')':
            cnt+=1
print(cnt)