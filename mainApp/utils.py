menu = [{'title': 'Главная', 'url_name': 'main_page'},
        {'title': 'Продукция', 'url_name': 'categories'},
        {'title': 'Отзывы', 'url_name': 'feedback'},
        {'title': 'Корзина', 'url_name': 'itemscart'},
]

class DataMixin:
    """
        Класс, предназаначенный для добвления в ClassView атрибут menu
    """
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context