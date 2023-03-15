from common.db import rdb

class Cart: 
    def __init__(self):
        self.cart = {}
        self.total = 0

    async def cache_cart (self):
        await rdb.set("cart_key", self.get_cart())
        await rdb.set("total_amount", self.get_total())


    async def add_to_cart(self, item):
        id = item.id
        if not cart[id]:
            cart[id] = item
        else: 
            cart[id].quantity += item.quantity
        self.total += item.price * item.quantity
        await cache_cart()
        
    async def remove_from_cart(self, item): 
        id = item.id
        if cart[id]:
            cart[id].quantity -= item.quantity
        
        self.total -= item.price * item.quantity
        await cache_cart()

    async def empty_cart(self):
        self.cart = {}
        await cache_cart()

    def get_total (self):
        return self.total

    def get_cart(self):
        return self.cart.values()