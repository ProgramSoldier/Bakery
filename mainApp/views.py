from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .utils import DataMixin, menu
from .forms import *



#Классы CBV
#----------------------------------------------
class RegisterUser(DataMixin, CreateView):
    """
    Класс формирует страницу регистрации пользователей
    """
    form_class = RegisterUserForm
    template_name = 'mainapp/register_page.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    """
        Класс формирует страницу авторизации пользователей
    """
    form_class = LoginUserForm
    template_name = 'mainapp/login_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main_page')


#Функции FBV
#------------------------------------------------------------------------
def get_main_page(request):
    """
        Функция возвращает стартовую страницу
    """
    context = {
        'menu': menu
    }
    return render(request, 'mainApp/main_page.html', context=context)


def get_addfeedback_page(request):
    """
       Функция возвращает страниуц с отзывами, а ещё обрабатывает форму добавления отзывав
    """
    models = FeedbackModel.objects.all()
    if request.method == 'POST':
        form = AddFeedbackForm(request.POST, user_id=request.user.pk)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = AddFeedbackForm()

    context = {
        'form': form,
        'menu': menu,
        'models': models
    }
    return render(request, 'mainapp/feedback_page.html', context)

def user_logout(request):
    """
        Функция завершения сессии авторизации
    """
    logout(request)
    return redirect('login')


def get_plag_page(request):
    """
           обычная заглушка
    """
    return HttpResponse('Заглушка')