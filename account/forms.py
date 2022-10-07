from django.contrib.auth import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Profile()
        fields = ('name','nickname')
