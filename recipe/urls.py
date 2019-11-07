from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('recipe/', views.Index.as_view(), name='index'),
    path('recipe/detail/<pk>', views.RecipeDetailView, name='recipe-detail'),
    path('comment', views.comment, name='comment'),
]
