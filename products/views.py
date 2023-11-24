from django.shortcuts import render
from .models import Category, Product
from django.views.generic import ListView
from mainApp.utils import DataMixin


#Классы CBV
#----------------------------------------------
class CategoriesView(DataMixin, ListView):
    """
        ClassView для отображения страницы категорий продуктов
    """
    model = Category
    template_name = 'products/categories_page.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ProducrtsCategoryView(DataMixin, ListView):
    """
        ClassView для отображения страницы с продуктами по категории
    """
    model = Product
    template_name = 'products/products_category.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(category__title=self.kwargs['title_category'], is_visible = True)
        #return Product.objects.filter(category=Category.objects.get(title=self.kwargs['title_category']).pk, is_visible=True)


#Функции FBV
#
#------------------------------------------------------------------------
"""
    Дaнные функции выполняю то, что и классы выше, оставил для примера, что есть 2 подхода создания view
"""

# def get_categories(request):
#     categories = Category.objects.all()
#     content = {
#         'categories': categories,
#         'menu':menu
#     }
#     return render(request, 'products/categories_page.html', content)
#
#
# def get_products_category(request, title_category: str):
#     category = Category.objects.get(title=title_category)
#     products = Product.objects.filter(Q(category=category.pk), Q(is_visible = True))
#     content = {
#         'products': products,
#         'menu': menu
#     }
#     return render(request, 'products/products_category.html' , content)
