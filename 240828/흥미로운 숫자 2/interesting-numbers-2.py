x,y=map(int,input().split())
res=0
for elem in range(x,y+1):
    elem=str(elem)
    cnt=[0]*10
    for i in elem:
        i=int(i)
        cnt[i]+=1
    if cnt.count(1)==1 and cnt.count(0)==8:
        res+=1
print(res)