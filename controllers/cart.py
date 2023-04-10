from common.db import rdb
import json
import asyncio
from common.logger import logger

class Cart: 
    def __init__(self):
        self.cart = {}
        self.total = 0.0

    async def get_cache (self):
        cart = await rdb.get("cart_key")
        total = await rdb.get("cart_total")
        self.cart = dict(json.loads(cart))
        self.total = float(self.total)

    async def cache_cart (self):
        await rdb.set("cart_key", json.dumps(self.cart))
        await rdb.set("total_amount", json.dumps(self.total))


    async def add_to_cart(self, item, quantity=1) -> None:
        id = item['id']
        if id not in self.cart:
            self.cart[id] = item
            self.cart[id]["quantity"] = quantity
        else: 
            self.cart[id]["quantity"] += quantity
        self.total += item["price"] * quantity
        await self.cache_cart()
        return self.cart
        
    async def remove_from_cart(self, item) -> None: 
        id = item['id']
        if id in self.cart:
            del cart[id]
            self.total -= item["price"] * quantity
            await self.cache_cart()
        else: return
        return self.cart

    async def empty_cart(self):
        self.cart = {}
        self.total = 0.0
        await self.cache_cart()
        return self.cart

    def get_total (self) -> float:
        return self.total

    def get_cart(self) -> list:
        if self.cart:
            return [self.cart[x] for x in list(self.cart)]
        else: return None

cart = Cart()