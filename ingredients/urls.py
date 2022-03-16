
from django.urls import path
from ingredients import views

app_name = 'ingredients'

urlpatterns = [
    path('', views.IngredientsView.as_view(), name='lista_ingrediente'),
    path('adaugare/', views.CreateIngredientView.as_view(), name='adauga'),
    path('modificare/<int:pk>/', views.UpdateIngredientView.as_view(), name='modifica'),
    path('sterge/<int:pk>/', views.deactivate_ingredient, name='dezactiveaza'),
    path('mail/', views.send_mail_s, name='mail'),
]
