from django import forms

from users.models import User, TechSupport


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class AppCreationForm(forms.ModelForm):
    class Meta:
        model = TechSupport
        fields = ['title', 'description',  'file']