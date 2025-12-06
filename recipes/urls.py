from django.urls import path
from .views import (
    CategoryListCreate,
    CategoryDetail,
    RecipeListCreate,
    RecipeDetail,
)

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    path('recipes/', RecipeListCreate.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]
