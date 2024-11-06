from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models import ManyToManyField, Model, CharField, ImageField, ForeignKey, CASCADE, PositiveIntegerField


class Product(Model):
    name = CharField(max_length=255)


class A(Model):
    name = CharField(max_length=255)
    images = GenericRelation('apps.Image')


class B(Model):
    name = CharField(max_length=255)
    images = GenericRelation('apps.Image')


class C(Model):
    name = CharField(max_length=255)
    images = GenericRelation('apps.Image')


class D(Model):
    name = CharField(max_length=255)
    images = GenericRelation('apps.Image')

    class Meta:
        abstract = True

class Image(Model):
    image = ImageField()
    content_type = ForeignKey('contenttypes.ContentType', CASCADE, limit_choices_to={'model__in': ['a', 'b', 'c', 'd']})
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


#
# class AImage(Model):
#     a_image = ImageField(null=True, blank=True)
#     b_image = ImageField(null=True, blank=True)
#     c_image = ImageField(null=True, blank=True)
#     d_image = ImageField(null=True, blank=True)


# class AImage(Model):
#     image = ImageField()
#
#
# class BImage(Model):
#     image = ImageField()
#
#
# class CImage(Model):
#     image = ImageField()
#
#
# class DImage(Model):
#     image = ImageField()


# GenericForeignKey

# class User(AbstractUser):
#     pass

#
# class A(Model):
#     name = CharField(max_length=100)
#
#
# class B(Model):
#     age = CharField(max_length=100)
#     a = ManyToManyField('apps.A', through='apps.AB', blank=True)
#
#
# class AB(Model):
#     # YEAR_IN_SCHOOL_CHOICES = [
#     #     ("junior", "Junior"),
#     #     ("middle", "Middle"),
#     #     ("senior", "Senior")
#     # ]
#     # status = CharField(max_length=100, choices=YEAR_IN_SCHOOL_CHOICES, default=YEAR_IN_SCHOOL_CHOICES[0][0])
#
#     class YearInSchoolChoices(TextChoices):
#         JUNIOR = 'junior', 'Junior'
#         MIDDLE = 'middle', 'Middle'
#         SENIOR = 'senior', 'Senior'
#         __empty__ = 'Aniqlanmagan'
#
#     status2 = CharField(max_length=100, choices=YearInSchoolChoices.choices, default=YearInSchoolChoices.JUNIOR)
#
#     MEDIA_CHOICES = {
#         "Audio": {
#             "vinyl": "Vinyl",
#             "cd": "CD",
#         },
#         "Video": {
#             "vhs": "VHS Tape",
#             "dvd": "DVD",
#         },
#         "unknown": "Unknown",
#     }
#     status = CharField(max_length=100, choices=MEDIA_CHOICES, null=True, blank=True)
#
#     a = ForeignKey('apps.A', CASCADE)
#     b = ForeignKey('apps.B', CASCADE)
#

# ForeignKey
# on_delete
# CASCADE  +
# SET_NULL +
# RESTRICT +
# SET_DEFAULT +
# DO_NOTHING +
# PROTECT +


# OneToOneField +
# OneToOneRel
# ManyToOneRel
# ManyToManyField +
# ManyToManyRel
# ForeignKey +
# ForeignObjectRel
# ForeignObject
# GenericForeignKey +


'''

Gruppa-1
Abdulazizxon Sulaymonov
Abdulloh Baxtiyorov
Biloliddin Husanboyev


Gruppa-2
Ixlosbek Matkarivov
Kamola Normurodova
Kamron Rustamov


Gruppa-3
Xurshid Najmitdinov
Hasan Sanoqulov
Laziz Hamidov -
Usoma Akmaljonov -


'''
