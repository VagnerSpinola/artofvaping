from django.urls import path
from . import views

app_name = 'tutorial'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<pk>', views.tutorial_detail, name='tutorial_detail'),
    path('comment', views.comment, name='comment'),
]
