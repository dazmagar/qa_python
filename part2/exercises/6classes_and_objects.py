# 1. The __init__ method, which should take an argument, name. It should initialise self.name
#    to be the argument, and self.items to be an empty list.
# 2. The add_item method, which sholud append a dictionary representing an item to the store's
#    items property. The dictionary should have keys name and price.
# 3. stock_price method, which should add up each item price inside self.items to come up
#    with a total, and return that.

class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this  method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be ab empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys and price, and append that to self.items.
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item['price'] for item in self.items])

eBay = Store('eBay')
eBay.add_item('iphone', 300)
eBay.add_item('ipad', 400)
eBay.add_item('macbook', 2400)

print(eBay.items)
print(eBay.stock_price())
