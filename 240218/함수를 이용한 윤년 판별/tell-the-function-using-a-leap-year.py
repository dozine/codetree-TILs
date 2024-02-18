y=int(input())
def is_yoon(y):
    if (y%4==0) or (y%4==0 and y%100==0 and y%400==0) :
        return "true" 
    else:
        return "false"

print(is_yoon(y))