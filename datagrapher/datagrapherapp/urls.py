from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view,home_view, logout_user, signup, logout_confirmation_view

urlpatterns = [
    path('', login_view.as_view(), name='login'),
    path('login/', login_view.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('logout_confirmation/', logout_confirmation_view, name='logout_confirmation'),
    path('signup/', signup, name='signup'),
    path('home/', home_view, name='home'),
]