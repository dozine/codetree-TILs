max_num=100
n=int(input())
arr=[0]*(max_num+1)

for _ in range(n):
    d,a=tuple(input().split())
    d=int(d)
    arr[d] = 1 if a=='G' else 2

max_len=0
for i in range(max_num+1):
    for j in range(i+1,max_num+1):
        if arr[i] == 0 or arr[j]==0:
            continue
        cnt_g=0
        cnt_h=0

        for k in range(i,j+1):
            if arr[k]==1:
                cnt_g+=1
            if arr[k]==2:
                cnt_h+=1
        if cnt_g==0 or cnt_h==0 or cnt_g==cnt_h:
            leng=j-i
            max_len=max(max_len,leng)
print(max_len)