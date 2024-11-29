from django.contrib import admin

from apps.models import Product, ProductImage


class ProductStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    min_num = 1
    max_num = 8


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = ProductStackedInline,
