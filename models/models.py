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
    created_at: fields.DateTimeField(auto_now_add=True)
    modified_at: fields.DateTimeField(auto_now=True)

    class Meta:
        table: "users"

class Ticket(Model):
    id: fields.IntField()
    event_id: fields.StringField()
    user_id: fields.ForeignKeyField("models.User", related_name="owner")
    ticket_type: fields.CharField(max_length=255)
    created_at: fields.DateTimeField(auto_now_add=True)
    modified_at: fields.DateTimeField(auto_now=True)

    class Meta:
        table: "tickets"

class Event(Model):
    id: fields.IntField()
    tickets: fields.ForeignKeyField("models.Ticket", related_name="tickets")
    user_id: fields.ForeignKeyField("models.User", related_name="owner")
    ticket_type: fields.CharField(max_length=255)
    created_at: fields.DateTimeField(auto_now_add=True)
    modified_at: fields.DateTimeField(auto_now=True)

    class Meta:
        table: "events"