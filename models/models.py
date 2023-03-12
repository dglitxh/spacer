from tortoise.models import Model
from tortoise import fields
from .schema import UserType


class User(Model):
    id = fields.IntField(pk=True, generated=True)
    firstname = fields.CharField(max_length=255, null=False)
    lastname = fields.CharField(max_length=255)
    age = fields.IntField()
    email = fields.CharField(max_length=255, unique=True, null=False)
    user_type = fields.CharEnumField(enum_type=UserType)
    gender = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        table = "users"

class Store(Model):
    id = fields.IntField(pk=True, generated=True)
    name = fields.CharField(max_length=255)
    description = fields.CharField(max_length=555)
    category = fields.CharField(max_length=255)
    cash_total = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    owner = fields.ForeignKeyField(model_name="models.User", related_name="owner")

    def __str__(self):
        return self.name
    class Meta:
        table = "stores"


class Product(Model):
    id = fields.IntField(pk=True, generated=True)
    name = fields.CharField(max_length=255)
    description = fields.CharField(max_length=555)
    category = fields.CharField(max_length=255)
    price = fields.FloatField()
    rating = fields.FloatField()
    store_id = fields.ForeignKeyField(model_name="models.Store", related_name="store")

    def __str__(self):
        return self.name
    class Meta:
        table = "products"


class CartItem(Model):
    id = fields.IntField(pk=True, generated=True)
    product = fields.ForeignKeyField(model_name="models.Product")
    quantity = fields.IntField()
    total_price = fields.FloatField()

    def __str__(self):
        return self.name
    class Meta:
        table = "cart_items"


class Order(Model):
    id = fields.IntField(pk=True, generated=True)
    owner = fields.ForeignKeyField(model_name="models.User", related_name="user")
    order_code = fields.UUIDField(generated=True)
    paid = fields.BooleanField(default=False)
    delivery = fields.BooleanField(default=False)
    items = fields.ForeignKeyField(model_name="models.CartItem", related_name="cart_items")

    def __str__(self):
        return self.name
    class Meta:
        table = "orders"
