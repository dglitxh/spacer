from common.db import rdb

class Cart: 
    def __init__(self):
        cart = rdb.get("cart_key")
        total = rdb.get("total_amount")
        if cart and total:
            self.cart = cart
            self.total = total
        else:
            self.cart = {}
            self.total = 0

    async def cache_cart (self):
        await rdb.set("cart_key", self.get_cart())
        await rdb.set("total_amount", self.get_total())


    async def add_to_cart(self, item) -> None:
        id = item.id
        if not cart[id]:
            self.cart[id] = item
        else: 
            self.cart[id].quantity += item.quantity
        self.total += item.price * item.quantity
        await cache_cart()
        
    async def remove_from_cart(self, item) -> None: 
        id = item.id
        if self.cart[id]:
            self.cart[id].quantity -= item.quantity
        self.total -= item.price * item.quantity
        await cache_cart()

    async def empty_cart(self) -> None:
        self.cart = {}
        await cache_cart()

    def get_total (self) -> float:
        return self.total

    def get_cart(self) -> list:
        return self.cart.values()