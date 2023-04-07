from common.db import rdb
from common.logger import logger

class Cart: 
    def __init__(self):
        self.cart = {}
        self.total = 0

    async def cache_cart (self):
        await rdb.set("cart_key", self.cart)
        await rdb.set("total_amount", self.total)


    async def add_to_cart(self, item) -> None:
        id = item.product_id
        if not self.cart[id]:
            self.cart[id] = item
        else: 
            self.cart[id].quantity += item.quantity
        self.total += item.price * item.quantity
        await cache_cart()
        return self.cart
        
    async def remove_from_cart(self, item) -> None: 
        id = item.product_id
        if self.cart[id]:
            self.cart[id].quantity -= item.quantity
        self.total -= item.price * item.quantity
        await cache_cart()
        return self.cart

    async def empty_cart(self) -> None:
        self.cart = {}
        await cache_cart()

    def get_total (self) -> float:
        return self.total

    def get_cart(self) -> list:
        return self.cart.values()

cart = Cart()