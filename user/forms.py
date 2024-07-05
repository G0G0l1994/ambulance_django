from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput,PasswordInput

from user.models import CustomUser

    

class RegistrationForm(UserCreationForm):
    username=forms.CharField(label="Имя пользователя", max_length=100)
    first_name = forms.CharField(label = "Имя", max_length=30)
    surname = forms.CharField(label="Отчество", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=50)
    role = forms.ChoiceField(label ="Должность", choices=[("dispatcher","диспетчер"),("doctors","врач")])
    email = forms.EmailField(label="Электронная почта", max_length=100)
    password1=forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2=forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput())

    def save_customuser(self,request=None):
        custom_model = CustomUser()
        for key,item in request.POST.items():
            if hasattr(custom_model,key):
                setattr(custom_model,key,item)
        custom_model.save()
        print("save CustomUser")
        

    
    class Meta:
        model = User
        fields = ["username","first_name","last_name","surname","role","email","password1","password2"]
    

        
    


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Пользователь:", widget=TextInput())
    password = forms.CharField(label="Пароль", widget=PasswordInput())


