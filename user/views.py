from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.conf import settings



from .forms import RegistrationForm, LoginForm
from .services.auth import user_auth, create_jwt_token
from .services.role import get_role_redirect



def home(request):
    print(request.user)
    
    return render(request, "project/main.html")


def custom_login(request):
    if request.method == 'GET':
        return render(request, "project/login.html", {"loginform": LoginForm()})
    
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if  not form.is_valid():
            return render(request, "project/login.html", {"loginform": form})
    try:
        user = user_auth(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
        
        token = create_jwt_token(user)

        login(request,user)

        response = redirect(get_role_redirect(user.profile))
        response.set_cookie(
             'access_token',
             token,
             httponly=True,
             secure=not settings.DEBUG,
             samesite='Strict'
        )
        return response

    except PermissionDenied as e:
        form.add_error(None,str(e))
        return render(request, "project/login.html", {"loginform": form})
                



def logout_user(request):

    if request.user.is_authenticated:
        request.user.profile.invalidate_all_session()
    
    response = redirect('home')
    response.delete_cookie('access_token')
    logout(request)

    return response



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

