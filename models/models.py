from tortoise.models import Model
from tortoise import fields
from .schema import UserType


class User(Model):
    id = fields.IntField(pk=True, generated=True)
    firstname = fields.CharField(max_length=255, null=False)
    lastname = fields.CharField(max_length=255)
    age = fields.IntField()
    email = fields.CharField(max_length=255, unique=True, null=False)
    user_type = fields.CharEnumField(enum_type=UserType, max_length=12)
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
    name = fields.CharField(max_length=255, null=False)
    description = fields.CharField(max_length=555)
    category = fields.CharField(max_length=255, null=False)
    cash_total = fields.FloatField(null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    owner = fields.ForeignKeyField(model_name="models.User", related_name="owner")

    def __str__(self):
        return self.name
    class Meta:
        table = "stores"


class Product(Model):
    id = fields.IntField(pk=True, generated=True)
    name = fields.CharField(max_length=255, null=False)
    description = fields.CharField(max_length=555)
    category = fields.CharField(max_length=255, null=False)
    price = fields.FloatField(null=False)
    rating = fields.FloatField()
    store_id = fields.ForeignKeyField(model_name="models.Store", related_name="store")

    def __str__(self):
        return self.name
    class Meta:
        table = "products"


class OrderItem(Model):
    id = fields.IntField(pk=True, generated=True)
    order_id = fields.ForeignKeyField(model_name="models.Order", related_name="order")
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
    store_id = fields.ForeignKeyField(model_name="models.Store", related_name="order_store")
    order_code = fields.UUIDField(generated=True)
    paid = fields.BooleanField(default=False)
    delivery = fields.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        table = "orders"
