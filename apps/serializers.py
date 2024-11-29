from random import choices

from rest_framework.exceptions import ValidationError
from rest_framework.fields import FileField, ListField, CurrentUserDefault, MultipleChoiceField, HiddenField, ChoiceField
from rest_framework.relations import PrimaryKeyRelatedField, HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from apps.models import Product, Category, ProductImage, Film, Genre


class GenreModelSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class FilmModelSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    # PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = Film
        fields = '__all__'
        # exclude
        # read_only_fields
        # extra_kwargs = {
        #     'password': {
        #         'write_only': True,
        #     }
        # }

    def to_representation(self, instance: Film):
        repr = super().to_representation(instance)
        repr['genres'] = GenreModelSerializer(instance.genres.all(), many=True).data
        if instance.owner:
            owner = instance.owner.username
        else:
            owner = None
        repr['owner'] = owner
        return repr


def validate_custom(value):
    if value < 2000:
        raise ValidationError('2000 dan kichik bolishi mn emas')
    return value


class DynamicFieldsModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CategoryModelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    # def to_representation(self, instance: Category):
    #     repr = super().to_representation(instance)
    #     repr['products'] = ProductModelSerializer(instance.product_set.all(), many=True, context=self.context).data
    #     return repr


class ProductImageModelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    # category = PrimaryKeyRelatedField(queryset=Category.objects.filter())
    # category = CategoryModelSerializer(read_only=True)
    # images = ProductImageModelSerializer(read_only=True, many=True, fields=('id', 'image'))
    selection = MultipleChoiceField(choices=(('name', 'Ism'), 'user', 'shop'), write_only=True)

    files = ListField(child=FileField(), write_only=True, required=False)
    category = HyperlinkedRelatedField(read_only=True, view_name='categories-detail')
    unmodel_field = ('selection', 'files')

    class Meta:
        model = Product
        fields = 'id', 'name', 'price', 'status', 'selection', 'last_price', 'description', 'category', 'files'

    def create(self, validated_data):
        exits_fields = set(self.unmodel_field).intersection(set(validated_data))
        print(exits_fields)
        for i in exits_fields:
            validated_data.pop(i)
        # files = validated_data.pop('files')
        instance = super().create(validated_data)
        # for _file in files:
        #     ProductImage.objects.create(product=instance, image=_file)

        return instance

    # def to_representation(self, instance: Product):
    #     repr = super().to_representation(instance)
    #
    #     repr['images'] = ProductImageModelSerializer(
    #         instance.images.all(), many=True, fields=('id', 'image'),
    #         context={'request': self.context['request']}
    #     ).data
    #     return repr
