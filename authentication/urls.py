from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('changePass_without_oldPass/', views.changePass_without_oldPass, name='changePass_without_oldPass'),
    path('change_profile/', views.change_profile, name='change_profile'),
]