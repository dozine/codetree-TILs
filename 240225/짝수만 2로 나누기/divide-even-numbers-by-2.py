N=int(input())
NN= list(map(int,input().split()))

def array(NN):
    for i in range(N):
        if NN[i]%2 ==0:
            NN[i]//=2

array(NN)

for j in NN:
    print(j,end=" ")