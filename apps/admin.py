from django.contrib import admin

from apps.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        from django.db import connections
        with connections['second_db'].cursor() as cursor:
            cursor.execute("INSERT INTO apps_product(title, price) VALUES (%s, %s);", [obj.name, obj.price])
