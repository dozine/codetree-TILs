a, b = map(int, input().split())

# Please write your code here.

def solution(a,b):
    small = min(a,b) + 10
    big = max(a,b) *2
    print(small, big)
    return 
     

solution(a,b)