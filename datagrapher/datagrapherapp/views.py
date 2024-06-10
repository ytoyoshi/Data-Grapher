from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import LoginForm, StockSearchForm, DateRangeForm
from .models import Page, Stock, StockData
import yfinance as yf

class login_view(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    form_class = LoginForm

@login_required
def home_view(request):
    pages = Page.objects.filter(show_on_home = True)
    return render(request, 'home.html', {'pages': pages})

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

def search_stock(request):
    if request.method == 'POST':
        search_form = StockSearchForm(request.POST)
        date_form = DateRangeForm(request.POST)
        if search_form.is_valid() and date_form.is_valid():
            symbol = search_form.cleaned_data['symbol']
            start_date = date_form.cleaned_data['start_date']
            end_date = date_form.cleaned_data['end_date']
            
            stock, created = Stock.objects.get_or_create(symbol=symbol, defaults={'name': symbol})
            
            data = yf.download(symbol, start=start_date, end=end_date)
            
            for date, row in data.iterrows():
                StockData.objects.update_or_create(
                    stock=stock,
                    date=date,
                    defaults={
                        'open': row['Open'],
                        'high': row['High'],
                        'low': row['Low'],
                        'close': row['Close'],
                        'volume': row['Volume'],
                    }
                )
            return redirect('stock_data_list')
    else:
        search_form = StockSearchForm()
        date_form = DateRangeForm()
    
    return render(request, 'search_stock.html', {'search_form': search_form, 'date_form': date_form})

def stock_data_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stock_data_list.html', {'stocks': stocks})