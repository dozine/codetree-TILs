n = int(input())

# Write your code here!
visited=[False] * (n+1)
answer=[]

def print_permutation():
    for elem in answer:
        print(elem,end=" ")
    print()

def choose(curr_num):
    if curr_num==n+1:
        print_permutation()
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        
        visited[i]=True
        answer.append(i)

        choose(curr_num+1)

        answer.pop()
        visited[i]=False
    
choose(1)
    