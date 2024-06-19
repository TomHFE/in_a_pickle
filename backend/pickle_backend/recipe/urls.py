from django.urls import path
from .views import recipe_list_and_create, recipe_detail

urlpatterns = [
    path('recipes/', recipe_list_and_create, name='recipe-list-and-create'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
]