K, N = map(int, input().split())

# Write your code here!
selected_nums=[]

def print_permutation():
    for num in selected_nums:
        print(num, end=" ")
    print()

def find_permutation(cnt):
    if cnt==N:
        print_permutation()
        return 
    for i in range(1,K+1):
        selected_nums.append(i)
        find_permutation(cnt+1)
        selected_nums.pop()

find_permutation(0)