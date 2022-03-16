
from django.urls import path
from distributors import views

app_name = 'distributors'

urlpatterns = [
    path('', views.DistributorsView.as_view(), name='lista_distribuitori'),
    path('adaugare/', views.CreateDistributorView.as_view(), name='adauga'),
    path('modificare/<int:pk>/', views.UpdateDistributorView.as_view(), name='modifica'),
    path('sterge/<int:pk>/', views.deactivate_distributor, name='dezactiveaza')
]
