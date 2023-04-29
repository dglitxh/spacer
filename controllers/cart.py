from common.db import rdb
import json
from common.logger import logger

class Cart: 
    def __init__(self):
        self.cart = {}

    async def get_cache (self):
        cart = await rdb.get("cart_key")
        self.cart = dict(json.loads(cart)) if cart else {}

    async def cache_cart (self):
        await rdb.set("cart_key", json.dumps(self.cart))

    async def add_to_cart(self, item, quantity=1, repl=False):
        print(self.cart)
        id = str(item['id'])
        if id not in self.cart:
            self.cart[id] = item
            self.cart[id]["quantity"] = quantity
        elif(repl): self.cart[id]["quantity"] = quantity
        else: 
            self.cart[id]["quantity"] += quantity
        await self.cache_cart()
        return self.cart
        
    async def remove_from_cart(self, id) -> None: 
        id = str(id)
        if id in self.cart:
            del self.cart[id]
            await self.cache_cart()
        else: return
        return self.cart

    async def empty_cart(self):
        self.cart = {}
        await list(self.cart)
 
    def get_total (self) -> float:
        cart = self.get_cart()
        total = 0
        for i in cart: total += i["quantity"]*i["price"]
        return total

    def get_cart(self) -> list:
        return [self.cart[x] for x in list(self.cart)]

cart = Cart()