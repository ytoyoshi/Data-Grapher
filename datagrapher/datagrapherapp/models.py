from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # e-mail
    email = models.EmailField(unique=True)

    def __str__(self) :
        return self.username
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="user_set_custom", 
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_set_custom",  
        related_query_name="user",
    )

class Page(models.Model):
    icon = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255, default="home")
    show_on_home = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StockData(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    class Meta:
        unique_together = ('stock', 'date')
    
    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"