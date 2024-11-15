n, m, q = map(int, input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def shift(row, direction):
    if direction=="L":
        temp=grid[row][-1]
        for i in range(m-1,0,-1):
            grid[row][i]=grid[row][i-1]
        grid[row][0]=temp
    else: 
        temp=grid[row][0]
        for i in range(m-1):
            grid[row][i]=grid[row][i+1]
        grid[row][-1]=temp

def can_go(a,b):
    for i in range(m):
        if a[i]==b[i]:
            return True
    return False

for _ in range(q):
    r,d=map(str,input().split())
    r=int(r)
    shift(r-1,d)
    memory=d
    rows=r-1
    for i in range(rows,0,-1):
        if can_go(grid[i],grid[i-1]):
            if d=='R':
                shift(i-1,'L')
                d='L'
            else:
                shift(i-1,'R')
                d='R'
        else:
            break
    d=memory

    for i in range(rows,n-1):
        if can_go(grid[i],grid[i+1]):
            if d=='R':
                shift(i+1,'L')
                d='L'
            else:
                shift(i+1,'R')
                d='R'
        else:
            break

for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()