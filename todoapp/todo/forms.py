from django import forms
from.models import login
from.models import register



class LoginForm(forms.ModelForm):

    class Meta:
        model = login
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'