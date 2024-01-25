n=int(input())
cnt=n
for i in range(n):
    for j in range(i+1):
        print(n-j+1,end=" ")
    print()