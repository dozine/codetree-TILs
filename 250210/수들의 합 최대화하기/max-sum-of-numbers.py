n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

selected=[]

visited=[False]*n
ans=0
def choose(row):
    global ans
    
    if row == n:
        sum_val=0
        for i in range(n):
            sum_val += grid[i][selected[i]]
        ans = max(ans,sum_val)
        return 
    
    for i in range(n):
        if visited[i]:
            continue
        visited[i]=True
        selected.append(i)

        choose(row+1)

        visited[i] = False
        selected.pop()


choose(0)
print(ans)