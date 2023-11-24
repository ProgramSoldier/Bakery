from django.urls import path, include
from .views import CategoriesView, ProducrtsCategoryView

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<str:title_category>/', ProducrtsCategoryView.as_view(), name='products_category')
]
