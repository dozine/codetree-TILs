n,t=tuple(map(int,input().split()))
left=list(map(int,input().split()))
right=list(map(int,input().split()))
down=list(map(int,input().split()))

for i in range(t):
    temp=left[n-1]
    for i in range(n-1,0,-1):
        left[i]=left[i-1]
    left[0]=down[n-1]
    for i in range(n-1,0,-1):
        down[i]=down[i-1]
    down[0]=right[n-1]
    for i in range(n-1,0,-1):
        right[i]=right[i-1]
    right[0]=temp

for elem in left:
    print(elem, end=" ")
print()
for elem in right:
    print(elem, end=" ")
print()
for elem in down:
    print(elem, end=" ")
print()