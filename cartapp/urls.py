from django.urls import path
from .views import *
urlpatterns = [
    path('', get_items_cart, name='itemscart'),
    path('update/', update_cart, name='update_cart'),
    # path('add/', add_item_cart, name ='add_item_cart'),
    # path('remove/', remove_item_cart, name='remove_item_cart')

]