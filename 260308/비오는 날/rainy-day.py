class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
cast = []

for _ in range(n):
    d, dy, w = input().split()
    cast.append(Forecast(d, dy, w))

# 1. 날짜(date) 기준으로 사전순 정렬
cast.sort(key=lambda x: x.date)

# 2. 정렬된 상태에서 처음으로 "Rain"이 나오는 날 찾기
ans = ""
for f in cast:
    if f.weather == "Rain":
        ans = f
        break # 찾았으면 즉시 중단

print(ans.date, ans.day, ans.weather)