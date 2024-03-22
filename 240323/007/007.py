class Spy:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time

a,b,c =tuple(input().split())
s = Spy(a,b,c)
print(f'secret code : {a}')
print(f'meeting point : {b}')
print(f'time : {c}')