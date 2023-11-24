from django.urls import path, include
from .views import *
urlpatterns = [
    path('', get_main_page, name='main_page'),
    path('register/',RegisterUser.as_view() , name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('feedback/', get_addfeedback_page, name='feedback'),
    path('products/', include('products.urls')),
    path('my_cart/', include('cartapp.urls')),
    path('order/', include('orderapp.urls'))
]
