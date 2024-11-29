from django.core.validators import FileExtensionValidator
from django.db.models import CharField, BooleanField, IntegerField, Model, TextField, ForeignKey, CASCADE, ImageField, \
    DateField, ManyToManyField, TextChoices


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    class Status(TextChoices):
        BEGIN = 'begin', 'Boshlandi'
        END = 'end', 'Tugadi'

    name = CharField(max_length=100)
    price = IntegerField()
    status = CharField(max_length=15, choices=Status.choices, default=Status.BEGIN)
    description = TextField(null=True, blank=True)
    is_premium = BooleanField(db_default=False)
    category = ForeignKey('apps.Category', CASCADE, null=True, blank=True)

    @property
    def last_price(self):
        return self.price + 1000


class ProductImage(Model):
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
    image = ImageField(upload_to='products/images', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])


class Genre(Model):
    name = CharField(max_length=255)


class Film(Model):
    title = CharField(max_length=255)
    released_date = DateField()
    genres = ManyToManyField('apps.Genre', related_name='films')
    owner = ForeignKey('auth.User', CASCADE, null=True, blank=True)
