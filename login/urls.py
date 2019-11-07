from django.urls import path

from . import views

app_name = 'login'


urlpatterns = [
    path(r'login/', views.index, name='index'),
    path(r'signup/', views.signup, name='signup'),
    path(r'register/', views.register, name='register'),
]
