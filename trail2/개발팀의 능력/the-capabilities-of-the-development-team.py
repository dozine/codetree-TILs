arr = list(map(int, input().split()))
min_val = 10000000
def back(start):
    global min_val
    if(len(num) == 2 and num[0]!=num[1]):
        min_val = min(min_val,max(num[0],num[1],(sum(arr) - sum(num))) - min(num[0],num[1],sum(arr)-sum(num)))
        # print(num,sum(arr)-sum(num),min_val)
        return
    for i in range(start,5):
        for j in range(i+1,5):
            if(i!=j):
                if(visited1[i] == False and visited1[j] == False):
                    visited1[i] = True 
                    visited1[j] = True 
                    num.append(arr[i]+arr[j])
                    back(i+1)
                    num.pop()
                    visited1[i] = False 
                    visited1[j] = False
                
visited1 = [False] * 5
num = []
back(0)
if min_val == 10000000:
    print(-1)
else:
    print(min_val)

