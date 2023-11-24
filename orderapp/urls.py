from django.urls import path
from .views import *

urlpatterns = [
  #path('detail/', get_detail_order, name='detail_order')
  path('add/', add_order, name='add_order')
]
