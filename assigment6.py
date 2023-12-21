'''
CREATE A PRODUCT OBJECTS WITH NAME, DESCRITPION, BRAND, MODEL, PRICE, DISCOUNT,
CALCULATE THE TOTALNUMBER OF ALL OBECTSPRICE AFTER REMOVING DISCOUNT
'''

class product:
    def __init__(self, name, description, brand, model, price):
        self.name = name
        self.description = description
        self.brand = brand
        self.model = model
        self.price = price
    
    def calc_discount(self, discount=10):
        discounted_price = self.price * (discount/100)
        return discounted_price
    
    def new_price(self):
        discount = self.calc_discount()
        return self.price - discount

product1 = product(
    name ="Samsung",
    description ="flat and touch screen",
    brand = 'ls22',
    model = 'Android',
    price = 44000
)

product2 = product(
    name="beans",
    description="drum",
    price=60000,
    
)

product3 = product(
    name="spaghetti",
    description="tiny",
    
    price=15000
    