n = int(input())
arr = [
	int(input())
	for _ in range(n)
]
cnt=0
box=[]
for i in range(n):
    if i>=1 and arr[i]==arr[i-1]:
        cnt+=1
    else:
        box.append(cnt)
        cnt=1
print(max(box))