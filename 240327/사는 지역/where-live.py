class Area:
    def __init__(self,name,code,address):
        self.name=name
        self.code=code
        self.address=address
    

n=int(input())
arr=[tuple(input().split()) for _ in range(n)]
people=[Area(name,code,address) for name, code, address in arr]

target =0
for i, person in enumerate(people):
    if person.name>people[target].name:
        target=i

print(f'name {people[target].name}')
print(f'addr {people[target].code}')
print(f'city {people[target].address}')