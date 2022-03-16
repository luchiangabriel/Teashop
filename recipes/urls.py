
from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipesView.as_view(), name='lista_retete'),
    path('adaugare/', views.CreateRecipeView.as_view(), name='adauga'),
    path('modificare/<int:pk>/', views.UpdateRecipeView.as_view(), name='modifica'),
    path('preparare/<int:pk>', views.updatequantityview, name='preparare'),
    path('sterge/<int:pk>/', views.deactivate_recipe, name='dezactiveaza'),
]
