from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# Create your views here.

#회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password1"]
            )
            nickname = request.POST["nickname"],
            profile = Profile(user=user, nickname=nickname)
            profile.save()
            auth.login(request, user)
            return redirect('main')
        else :
            return render(request, 'account/signup.html')
    else:
        form = UserCreationForm()
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid() :
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else :
            return render(request, 'account/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('main')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})

def mypage(request, id):
    user = request.user
    user_id = str(user.id)
    if (user.is_authenticated == True) and (user_id == id) :
        user = User.objects.get(id=id)
        context = {
            'user':user,
        }
        return render(request, 'mypage.html', context)
    else:
        msg = "내 정보 페이지는 로그인 후 접근 가능합니다."
        form = AuthenticationForm()
        context = {
            'msg':msg,
            'form':form
        }
        return render(request, 'login.html', context)