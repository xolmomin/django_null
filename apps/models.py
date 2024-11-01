from keyword import kwlist

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, SlugField
from django.utils.text import slugify


class User(AbstractUser):
    pass


class Product(Model):
    ITEMS_SCHEMA = {
        'type': 'dict',  # a list which will contain the items
        'keys': {  # or 'properties'
            'size': {
                'type': 'number'
            },
            'color': {
                'type': 'string'
            },
            'storage': {
                'type': 'string'
            }
        },
        'required': ['size', 'color']
    }

    name = CharField(max_length=255)
    slug = SlugField(editable=False, null=True, blank=True)

    def save(self, *args, init_id=None, **kwargs):
        self.slug = slugify(self.name)
        if not init_id:
            self.save(*args, init_id=True, **kwargs)
            self.slug += f"-{self.id}"
        super().save(*args, **kwargs)

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
