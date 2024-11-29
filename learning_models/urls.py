from django.urls import path
from learning_models.views import home, create_student, delete_student

urlpatterns = [
    path('', home, name='home'),
    path('create_student/', create_student, name='create_student'),
    path('delete/<int:roll>', delete_student, name='delete_student')
]
