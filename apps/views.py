from django.db.models import Count, Q
from rest_framework.generics import ListCreateAPIView, ListAPIView

from apps.models import Product, Category
from apps.serializers import ProductModelSerializer, CategoryModelSerializer


class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(
            premium_product_count=Count('category__product__is_premium', filter=Q(category__product__is_premium=True)))


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
