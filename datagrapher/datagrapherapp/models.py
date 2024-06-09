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