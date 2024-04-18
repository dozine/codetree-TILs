r,c=tuple(map(int,input().split()))
arr=[
    input().split()
    for _ in range(r)
]
cnt=0
for i in range(1,r):#왼쪽 상단에서 출발하기 때문에 0이 아닌 1에서 시작하게 된다. 여기가 첫번째 움직임
    for j in range(1,c):# 이또한 마찬가지 
        for k in range(i+1,r-1):# 이미 한번 움직인 상태에서 다음 움직임 
            for l in range(j+1,c-1):
                if arr[0][0]!=arr[i][j] and arr[i][j] !=arr[k][l] and arr[k][l] != arr[r-1][c-1]:
                    cnt+=1

print(cnt)