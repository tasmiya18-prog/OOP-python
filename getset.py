class ShoppingCart:
    def __init__(self):
        self.items=[]
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,value):
        if index < len(self.items):
            self.items[index]=value
        else:
            raise IndexError
    def add_item(self,item):
        self.items.append(item)

cart = ShoppingCart()
cart.add_item("milk")
cart.add_item("bread")
cart.add_item("eggs")
print(cart.items)
cart[1] = "new item"
print(cart.items)
