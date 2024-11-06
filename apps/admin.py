from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.contenttypes.models import ContentType

from apps.models import Image, A, C, D, B


class ImageStackedInline(StackedInline):
    model = Image
    extra = 1
    min = 1


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    search_fields = ['app_label', 'model']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    autocomplete_fields = ['content_type']

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     # if db_field.name == 'content_type':
    #     #     kwargs["queryset"] = ContentType.objects.filter(model__in=['a', 'b', 'c', 'd'])
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(A)
class AAdmin(admin.ModelAdmin):
    # inlines = ImageStackedInline,
    pass


@admin.register(B)
class BAdmin(admin.ModelAdmin):
    #     inlines = ImageStackedInline,
    pass


@admin.register(C)
class CAdmin(admin.ModelAdmin):
    #     inlines = ImageStackedInline,
    pass


@admin.register(D)
class DAdmin(admin.ModelAdmin):
    #     inlines = ImageStackedInline,
    pass
