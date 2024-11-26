from django.contrib import admin

from apps.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # obj.price += 1000
        obj.save()
