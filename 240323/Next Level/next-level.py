class Nextlevel:
    def __init__(self,user_id="",level=0):
        self.user_id = user_id
        self.level = level
    

nextlevel=Nextlevel()

nextlevel.user_id="codetree"
nextlevel.level=10

user_id2,level2=tuple(input().split())

nextlevel2=Nextlevel()
nextlevel2.user_id=user_id2
nextlevel2.level=int(level2)

print(f"user {nextlevel.user_id} lv {nextlevel.level}")
print(f"user {nextlevel2.user_id} lv {nextlevel2.level}")