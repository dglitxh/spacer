from common.db import rdb

class Cart: 
    def __init__(self):
        self.cart = []

        self.total = 0

    async def cache_cart (self):
        await rdb.set("cart_key", self.get_cart())
        await rdb.set("total_amount", self.get_total())


    async def add_to_cart(self, item):
        self.total += item.price * item.quantity
        self.cart.append(item)
        await cache_cart()
        
    async def remove_from_cart(self, item): 
        self.total -= item.price * item.quantity
        self.cart = list(filter(lambda x: x.id != item.id))
        await cache_cart()

    async def empty_cart(self):
        self.cart = []
        await cache_cart()

    def get_total (self):
        return self.total

    def get_cart(self):
        return self.cart