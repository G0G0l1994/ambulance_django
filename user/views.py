from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.core.exceptions import PermissionDenied



from .forms import RegistrationForm, LoginForm
from .services.auth import login_user
from .services.role import get_role_redirect



def home(request):
    print(request.user)
    
    return render(request, "project/main.html")


def custom_login(request):

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            try:
                redirect_to = login_user(
                    request,
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'])

                return redirect(redirect_to)
            except PermissionDenied as e:
                form.add_error(None,str(e))
                


    
    return render(request,"project/login.html", {"loginform": form})


def logout_user(request):

    logout(request)

    return redirect('home')



def register(request):
    form = RegistrationForm()

    if request.method == "POST":

        form = RegistrationForm(request.POST or None)
        if form.is_valid():

            form.save_customuser(request)
            form.save(request)
            

            return redirect("login")
    
    context = {"registerform": form}


    return render(request,"project/register.html", context=context)

def doctor_page(request):

    return render(request, 'project/doctor-page.html')


def dispatcher_page(request):

    return render(request, 'project/dispatcher-page.html')

