from django.urls import path
from .views import ShopView, ProductDetailView

app_name = 'shops'

urlpatterns = [
    path('<int:pk>/details/', ProductDetailView.as_view(), name='product_detail'),
    path('', ShopView.as_view(), name='shop')
]