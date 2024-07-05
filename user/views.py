from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout



from .forms import RegistrationForm, LoginForm



def home(request):
    
    return render(request, "project/main.html")


def custom_login(request):

    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        form = LoginForm(request,data=request.POST)
      
        if form.is_valid():
            print("username and password")
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,
                                password=password)
            print("auth in user")

            if user is not None:
                login(request,user)
                print(user)
                return redirect('home')
    
    context = {"loginform": form}

    
    return render(request,"project/login.html", context=context)






def register(request):
    form = RegistrationForm()

    if request.method == "POST":

        form = RegistrationForm(request.POST or None)
        if form.is_valid():

            form.save(request)
            form.save_customuser(request)

            return redirect("login")
    
    context = {"registerform": form}


    return render(request,"project/register.html", context=context)



