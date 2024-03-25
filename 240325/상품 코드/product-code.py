class Item:
    def __init__(self,name='codetree',code=50):
        self.name=name
        self.code=code
    
item=Item()
name,code=tuple(input().split())
item2=Item(name, int(code))



print(f'product {item.code} is {item.name}')
print(f'product {item2.code} is {item2.name}')