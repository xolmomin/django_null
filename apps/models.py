from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CharField, Model, IntegerField, Manager, ForeignKey, CASCADE, AutoField, BigAutoField, \
    BinaryField


class User(AbstractUser):

    def save(self, *args, **kwargs):
        if 'botir' in self.username.lower():
            raise ValidationError('Username atmen!')

        super().save(*args, **kwargs)


class Product(Model):
    # quantity = AutoField() # SERIAL
    number = BigAutoField(primary_key=True)  # SERIAL
    image = BinaryField()

    class Meta:
        db_tablespace = 'valijon_tablespace'

# class BaseMetaMixin:
#     class Meta:
#         verbose_name = 'Mahsulot'
#         db_tablespace = 'valijon_tablespace'
#
#
# class Product(Model):
#     name = CharField(max_length=100, db_tablespace="valijon_tablespace")
#     passport_series = CharField(max_length=2, null=True)
#     passport_number = CharField(max_length=7, null=True)
#
#     def __str__(self):
#         return f"{self.id} - {self.name}"
#
#     class Meta(BaseMetaMixin.Meta):
#         pass
#         # app_label = 'apps'
#         # abstract = True
#         # proxy = True
#         # db_table = 'apps_product'
#         # verbose_name_plural = 'Products'
#         # unique_together = [
#         #     ('passport_series', 'passport_number')
#         # ]
#         # indexes = [
#         #     Index(fields=['name'], name='name'),
#         # ]
#         # ordering = ['-name']
#
#
# class KamronManager(Manager):
#
#     def get_queryset(self):
#         return super().get_queryset().filter(name__icontains='kamron')
#
#
# class Category(Model):
#     name = CharField(max_length=255, db_comment='Bu ismi kiritadigan joy')
#     price = IntegerField(db_default=1000)
#     kamron = KamronManager()
#     ikkinchi = Manager()
#
#     def __str__(self):
#         return f"{self.id} - {self.price}"
#
#     class Meta(BaseMetaMixin):
#         verbose_name_plural = 'Categories'
#         default_manager_name = 'ikkinchi'
#
#
# class BookCategory(Model):
#     name = CharField(max_length=255)
#
#
# class Book(Model):
#     name = CharField(max_length=255)
#     category = ForeignKey('apps.BookCategory', CASCADE)
#
#     class Meta:
#         default_related_name = 'valijonni_boglanishi'
