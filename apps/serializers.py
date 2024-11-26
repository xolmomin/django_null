from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, IntegerField, Field, CharField
from rest_framework.serializers import ModelSerializer

from apps.models import Product, Category


def validate_custom(value):
    if value < 2000:
        raise ValidationError('2000 dan kichik bolishi mn emas')
    return value


class CategoryModelSerializer(ModelSerializer):
    # premium_product_count = SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    # def get_premium_product_count(self, obj):
    #     return obj.product_set.filter(is_premium=True).count()

    # def to_representation(self, instance: Category):
    #     repr = super().to_representation(instance)
    #     repr['product_count'] = instance.product_set.count()
    #     return repr


class ProductModelSerializer(ModelSerializer):
    # addition_price = IntegerField(write_only=True,validators=[validate_custom], label='narx', default=1500, initial=2000, required=False, help_text="Qo'shimcha pul")
    # category_name = CharField(source='category.name', read_only=True)
    # vali = SerializerMethodField("get_category_name")
    category = CategoryModelSerializer(read_only=True)

    class Meta:
        model = Product
        fields = 'id', 'name', 'category', 'price', 'last_price', 'description'
        # exclude = ()
        # extra_kwargs = {
        #     'son': {
        #         'write_only': True
        #     },
        # }

    # def get_category_name(self, obj):
    #     if obj.category:
    #         return obj.category.name
    #     return
    # def validate(self, attrs):
    #     if 'addition_price' in attrs:
    #         attrs['price'] += attrs.pop('addition_price')
    #     return attrs
    # def to_internal_value(self, data):
    #     internal_data = super().to_internal_value(data)
    #     internal_data['price'] += 1000
    #     print(internal_data)
    #     return internal_data

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        if repr['category'] is not None:
            repr['category'].update({'premium_product_count': instance.premium_product_count})
        return repr

    #
    # def validate_name(self, value):
    #     print('name')
    #     if 'olma' in value.lower():
    #         raise ValidationError('olma kiritilmaydi!')
    #     return value
    #
    # def validate_price(self, value):
    #     print('price')
    #     if value < 2000:
    #         raise ValidationError('2000 dan kichik bolishi mn emas')
    #     return value
