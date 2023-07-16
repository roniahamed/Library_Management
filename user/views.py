from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import auth, User
# Create your views here.


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username != "" and User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Successfully Login')
                return redirect('/')
            else:
                messages.warning(request, 'Invalid Password')
                return redirect('login')
        else:
            messages.warning(request, 'Invalid Username')
            return redirect('login')
    return render(request, 'login.html')


def log_out(request):
    if request.user.is_authenticated:
        messages.success(request, "Successfully Logout!")
        logout(request)
    return redirect('/')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username, first_name, last_name, email, password1, password2)
        if password1 != "" and password1 == password2:
            if username == "" or User.objects.filter(username=username).exists():
                messages.warning(request, 'This Username is already taken')
                return redirect('signup')
            elif first_name == "":
                messages.warning(request, "Enter a valid First Name")
                return redirect('signup')
            elif email == "" or User.objects.filter(email=email).exists():
                messages.warning(request, "This email is already taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                messages.success(request, 'Your Registration Successful')
                return redirect('login')
        else:
            messages.warning(
                request, "Your password and confirm password does't match")
            return redirect('signup')
    return render(request, 'signup.html')
