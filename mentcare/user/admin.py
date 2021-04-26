from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import SimpleListFilter


admin.site.register(CustomUser)