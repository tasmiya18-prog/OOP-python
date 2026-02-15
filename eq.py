class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def __eq__(self,other):
        if not isinstance(other,Mobile):
            return False
        return self.brand == other.brand and self.model == other.model
    
mobile1=Mobile("Apple","14","12345")
mobile2=Mobile("Apple","14","12657")
mobile3=Mobile("Oppo","16","52345")

print(mobile1 == mobile2)
print(mobile2 == mobile3)
print(mobile1 == mobile3)
