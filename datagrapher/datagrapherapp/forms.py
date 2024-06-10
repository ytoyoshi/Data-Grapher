from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'ID'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

class StockSearchForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)

class DateRangeForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.TextInput(attrs={'type': 'date'}))