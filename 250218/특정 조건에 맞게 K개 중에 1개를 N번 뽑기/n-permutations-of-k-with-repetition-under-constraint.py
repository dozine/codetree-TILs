#k개중에서 1개를 n번 뽑는다라.. (조건)

k,n=tuple(map(int,input().split()))
selected=[]
def print_per():
    for i in selected:
        print(i,end=" ")
    print()

def find_permutation(cnt):
    if cnt==n:
        print_per()
        return
    
    for i in range(1,k+1):
        if cnt>=2 and i==selected[-1] and i==selected[-2]:
            continue
        else:
            selected.append(i)
            find_permutation(cnt+1)
            selected.pop()
find_permutation(0)