from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from apps.models import Product, Category, Genre, Film
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, GenreModelSerializer, FilmModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').order_by('-id')
    serializer_class = ProductModelSerializer
    pagination_class = PageNumberPagination
    filter_backends = SearchFilter, OrderingFilter
    search_fields = '=id',


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


class FilmListCreateAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

