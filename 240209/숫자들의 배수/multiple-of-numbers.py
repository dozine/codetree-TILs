arr=[]
cnt=0
n=int(input())
arr.append(n)
for i in range(1,10):
    a = arr[i-1]+arr[0]
    arr.append(a)

for elem in arr: 
    print(elem,end=" ")
    if elem %5 ==0 :
        cnt+=1
    if cnt>=2:
        break