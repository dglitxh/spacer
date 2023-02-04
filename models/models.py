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

