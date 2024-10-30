from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass

    @admin.display(description='Image')
    def scheme_image_tag(self, obj: Product):
        from base64 import b64decode
        return mark_safe(rf"""<img src = "`data: image/png; base64, {b64decode(obj.image)}`" width="200" height="100">""")

    scheme_image_tag.allow_tags = True

    readonly_fields = ['scheme_image_tag']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass
