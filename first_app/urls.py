from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('django_form/', views.djangoForm, name='django_form'),
    path('student_form/', views.studentForm, name='student_form'),
    path('password_validator/', views.passwordValidator, name='password_validator'),
]