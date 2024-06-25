MAX_R=200
OFFSET=100
n=int(input())
segments=[
    tuple(map(int,input().split()))
    for _ in range(n)
]

blocks=[0]*(MAX_R+1)
for x1,x2 in segments:
    x1,x2=x1+OFFSET,x2+OFFSET
    for i in (x1,x2):
        blocks[i]+=1
max_num=max(blocks)
print(max_num)