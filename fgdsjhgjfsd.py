import os
import time

import django
from django.core.exceptions import FieldError
from django.db import transaction, connection
from django.db.models import Q, Min, F, Subquery, Sum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")

django.setup()

from django.contrib.auth.models import User
from apps.models import Product, Category

# Product.objects.filter(name__contains='anor')
# print(Product.objects.filter(name__contains='no'))

# User
# date_joined = 2020

Product.objects.filter(
    price__range=(2000, 3500),
    description__isnull=False,
    name__icontains='a'
)
Product.objects.filter(
    price__gte=2000,
    price__lte=3500
).filter(
    description__isnull=False,
    name__icontains='a'
)
Product.objects.filter(
    price__gte=2000,
    price__lte=3500
).filter(
    description__isnull=False
).filter(
    name__icontains='a'
)

Product.objects.filter(
    price__gte=2000,
    price__lte=3500
).exclude(
    description__isnull=True
).filter(
    name__icontains='a'
)

# task
''''
price 2000-3500
description bor bolganlarini
name ichida a harfi ishlatilgani


'''
