MAX_NUM=3
n=int(input())
commands =[
    tuple(map(int,input().split()))
    for _ in range(n)
]

max_score=0

for i in range(1,4):
    yabawi=[0]*4
    yabawi[i]=1
    score=0
    for a,b,c in commands:
        yabawi[a],yabawi[b]=yabawi[b],yabawi[a]
        if yabawi[c]:
            score+=1
    max_score = max(max_score,score)

print(max_score)