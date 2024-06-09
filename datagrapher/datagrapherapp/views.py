from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import LoginForm

class login_view(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    form_class = LoginForm

@login_required
def home_view(request):
    cards = [
        {'id': 1, 'icon': 'arrow-down-square.svg', 'title': 'Home', 'description': 'Home menu'},
        {'id': 2, 'icon': 'fa-user', 'title': 'Profile', 'description': 'Profile menu'},
        {'id': 3, 'icon': 'fa-cog', 'title': 'Settings', 'description': 'Settings menu'},
        {'id': 4, 'icon': 'fa-envelope', 'title': 'Messages', 'description': 'Messages menu'},
        # 他のカードもここに追加
    ]
    return render(request, 'home.html', {'cards': cards})

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logout_confirmation.html')

@login_required
def logout_confirmation_view(request):
    # print("logout ")
    return render(request, 'logout_confirmation.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # ホームページまたは適切なページにリダイレクト
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})