 # 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
pieces = [1 for _ in range(k)]

ans = 0


# 점수를 계산합니다.
def calc():
    score = 0
    for piece in pieces:
        if piece>=m:
            score+=1
    
    return score


def find_max(cnt):
    global ans

    if cnt == n: 
        ans = max(ans, calc())
        return
	
    for i in range(k):
        if pieces[i] >= m:
            continue
        
        pieces[i] += nums[cnt]
        find_max(cnt + 1)
        pieces[i] -= nums[cnt]


find_max(0)
print(ans)



