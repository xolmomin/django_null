from django.urls import path

from apps.views import ProductListCreateAPIView, GenreListCreateAPIView, CategoryListAPIView, FilmListCreateAPIView, \
    CategoryRetrieveAPIView

urlpatterns = [
    path('genres', GenreListCreateAPIView.as_view(), name='genres'),
    path('films', FilmListCreateAPIView.as_view(), name='films'),
    path('products', ProductListCreateAPIView.as_view(), name='product-list'),
    path('categories', CategoryListAPIView.as_view(), name='categories-list'),
    path('categories/<int:pk>', CategoryRetrieveAPIView.as_view(), name='categories-detail'),
]
