from common.db import rdb
import json
import asyncio
from common.logger import logger

class Cart: 
    def __init__(self):
        self.cart = {}

    async def get_cache (self):
        cart = await rdb.get("cart_key")
        total = await rdb.get("cart_total")
        self.cart = dict(json.loads(cart))

    async def cache_cart (self):
        await rdb.set("cart_key", self.cart)

    async def add_to_cart(self, item, quantity=1, repl=False) -> None:
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
        
    async def remove_from_cart(self, item) -> None: 
        id = str(item['id'])
        if id in self.cart:
            del cart[id]
            await self.cache_cart()
        else: return
        return self.cart

    async def empty_cart(self):
        self.cart = {}
        await rdb.delete("cart_key")
        return self.cart
 
    def get_total (self) -> float:
        cart = self.get_cart()
        for i in cart: total += i["quantity"]*i["price"]
        return total

    def get_cart(self) -> list:
        if self.cart:
            return [self.cart[x] for x in list(self.cart)]
        else: return None

cart = Cart()