dirs = input()
x,y = 0,0
curr_dir=3

dx,dy = [1,0,-1,0],[0,-1,0,1]
for i in dirs:
    if i == 'L':
        curr_dir=(curr_dir-1+4)%4
    elif i =='R':
        curr_dir=(curr_dir +1)%4
    else:
        x,y= x+dx[curr_dir], y+dy[curr_dir]
print(x,y)