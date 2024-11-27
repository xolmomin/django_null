from django.urls import path

from apps.views import ProductCreateAPIView, CategoryListAPIView

urlpatterns = [
    path('products', ProductCreateAPIView.as_view(), name='product-list'),
    path('categories', CategoryListAPIView.as_view(), name='categories-list'),
]

