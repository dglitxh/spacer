from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True, generated=True)
    firstname = fields.CharField(max_length=255, null=False)
    lastname = fields.CharField(max_length=255)
    age = fields.IntField()
    email = fields.CharField(max_length=255, unique=True, null=False)
    user_type = fields.CharField(max_length=255)
    gender = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        table: "users"

class Store(Model):
    id: fields.IntField(pk=True, generated=True)
    name: fields.CharField(max_length=255)
    category: fields.CharField(max_length=255)
    cash_total: fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    products: fields.ForeignKeyField(model_name=Product, on_delete='CASCADE', related_name="products")

class Product(Model):
    id: fields.IntField(pk=True, generated=True)
    name: fields.CharField(max_length=255)
    description: fields.CharField()
    category: fields.CharField(max_length)
    price: fields.FloatField()
    rating: fields.FloatField()
    store_id: fields.ForeignKeyField(model_name=Store, related_name="store")

class CartItem(Model):
    id: fields.IntField(pk=True, generated=True)
    product: fields.ForeignKeyField(model_name=Product)
    quantity: fields.IntField()
    total_price: fields.FloatField()
    
class Order(Model): 
    id: fields.IntField(pk=True, generated=True)
    user: fields.ForeignKeyField(model_name=User, related_name="user")
    order_code: fields.UUIDField(generated=True)
    paid: fields.BooleanField(default=False)
    delivery: fields.BooleanField(default=False)
    items: fields.ForeignKeyField(model_name=CartItem, related_name="cart_items")