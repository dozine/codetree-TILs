n=int(input())
arr=list(map(int,input().split()))

new_arr=[i*i for i in arr]

for j in range(n):
    print(new_arr[j],end=" ")