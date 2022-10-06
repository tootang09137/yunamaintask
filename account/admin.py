from django.contrib import admin
from account.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Profile)