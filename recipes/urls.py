from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    CategoryListCreate,
    CategoryDetail,
    RecipeListCreate,
    RecipeDetail,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    path('recipes/', RecipeListCreate.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]
