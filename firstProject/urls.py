from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('navigation/', include("navigation.urls")),
    path('first_app/', include("first_app.urls")),
    path('learning_models/', include("learning_models.urls")),
    path('authentication/', include("authentication.urls")),
]
