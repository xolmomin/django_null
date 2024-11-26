from django.db.models import CharField, BooleanField, IntegerField, Model, TextField, ForeignKey, CASCADE


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=100)
    price = IntegerField()
    description = TextField(null=True, blank=True)
    is_premium = BooleanField(db_default=False)
    category = ForeignKey('apps.Category', CASCADE, null=True, blank=True)

    @property
    def last_price(self):
        return self.price + 1000

#
# class Power:
#
#     def __init__(self, *args, **kwargs):
#         self._args = args
#
#     def __call__(self, *args, **kwargs):
#         if len(args) == 1:
#             def wrapper(a, b):
#                 return args[0](a, b) + self._args[0]
#             return wrapper
#         return self._args[0](*args, **kwargs)
#
#
# @Power
# def show(a, b):
#     return a + b
#
#
# print(show(2, 3))
