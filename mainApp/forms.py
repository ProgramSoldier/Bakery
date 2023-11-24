from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.PasswordInput()


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['content']

    def __init__(self, *args, **kwargs):
        if 'user_id' in kwargs:
            self.user_id = kwargs.pop('user_id')
        super(AddFeedbackForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(AddFeedbackForm, self).save(commit=False)
        inst.user_id = self.user_id
        if commit:
            inst.save()
            self.save_m2m()
        return inst

