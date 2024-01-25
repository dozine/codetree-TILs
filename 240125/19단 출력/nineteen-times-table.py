n=19

for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            print('/',f'{i} * {j} = {i*j}')
        else:
            print(f'{i} * {j} = {i*j}',end=" ")
        if j==19:
            print()