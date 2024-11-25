from django.db.models import CharField, IntegerField, Model, TextField, ImageField


class Product(Model):
    name = CharField(max_length=100)
    price = IntegerField()
    description = TextField(null=True, blank=True)
