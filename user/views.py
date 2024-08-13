from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout



from .forms import RegistrationForm, LoginForm
from .models import CustomUser



def home(request):
    print(request.user)
    
    return render(request, "project/main.html")


def custom_login(request):

    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        form = LoginForm(request,data=request.POST)
        model = CustomUser()
      
        if form.is_valid():
            print("username and password")
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,
                                password=password)
            print("auth in user")

            if user is not None:
                user_custom = CustomUser.objects.get(username=username)
                login(request,user)
                print(user)
                if user_custom.role == "doctors":
                    return redirect('doctors')
                else:
                    return redirect('dispatcher')
                # return redirect('home')
    
    context = {"loginform": form}

    
    return render(request,"project/login.html", context=context)


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

