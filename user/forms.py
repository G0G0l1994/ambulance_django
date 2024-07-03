from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, BaseUserCreationForm
from django.forms.widgets import TextInput,PasswordInput
from django.contrib.auth.models import User

from user.models import CustomUser


# class RegistrationForm(forms.Form):
#     username=forms.CharField(label="Имя пользователя", max_length=100)
#     first_name = forms.CharField(label = "Имя", max_length=30)
#     surname = forms.CharField(label="Отчество", max_length=30)
#     last_name = forms.CharField(label="Фамилия", max_length=50)
#     role = forms.ChoiceField(label ="Должность", choices=[("dispatcher","диспетчер"),("doctors","врач")])
#     email = forms.EmailField(label="Эелектронная почта", max_length=100)
#     password1=forms.CharField(label="Пароль", widget=forms.PasswordInput)
#     password2=forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput)

    
    # def save(self,request):
    #     dict_data = request.POST
    #     models = get_user_model()
    #     models_data = models(username=dict_data["username"],
    #                   first_name=dict_data["first_name"],
    #                   last_name=dict_data["last_name"],
    #                   surname=dict_data["surname"],
    #                   role=dict_data["role"],
    #                   password=dict_data["password1"])
        
    #     models_data.save()

        # return f"{dict_data.values()}"
    

class RegistrationForm(UserCreationForm):
    username=forms.CharField(label="Имя пользователя", max_length=100)
    first_name = forms.CharField(label = "Имя", max_length=30)
    surname = forms.CharField(label="Отчество", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=50)
    role = forms.ChoiceField(label ="Должность", choices=[("dispatcher","диспетчер"),("doctors","врач")])
    email = forms.EmailField(label="Электронная почта", max_length=100)
    password1=forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2=forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput())

    
    class Meta:
        model = User
        fields = ["username","first_name","last_name","surname","role","email","password1","password2"]
        
    


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Пользователь:", widget=TextInput())
    password = forms.CharField(label="Пароль", widget=PasswordInput())


