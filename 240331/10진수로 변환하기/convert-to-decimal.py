n=list(map(int,list(input())))
length=len(n)
num=0
for i in range(length):
    num=num*2+n[i]
print(num)