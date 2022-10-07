from django.contrib import admin
from django.urls import path


from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('mypage/<str:id>', views.mypage, name='mypage'),
    path('user_update', views.user_update, name='user_update'),
]