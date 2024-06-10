from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view,home_view, logout_user, signup, logout_confirmation_view, search_stock, stock_data_list

urlpatterns = [
    path('', login_view.as_view(), name='login'),
    path('login/', login_view.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('logout_confirmation/', logout_confirmation_view, name='logout_confirmation'),
    path('signup/', signup, name='signup'),
    path('home/', home_view, name='home'),
    path('search_stock/', search_stock, name='search_stock'),
    path('stock_data/', stock_data_list, name='stock_data_list'),
]