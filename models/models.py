from tortoise.models import Model
from tortois import fields

class User(Model):
    id: fields.IntField()
    firstname: fields.CharField(max_length=255)
    lastname: fields.CharField(max_length=255)
    age: fields.IntField()
    email: fields.CharField(max_length=255)
    user_type: fields.CharField()
    gender: fields.CharField()
    password: fields.CharField()

