from django.urls import path
from .views import update_wishlist

app_name = 'products'

urlpatterns = [
    path('<int:id>/wishlist/', update_wishlist, name='add_wishlist')
]