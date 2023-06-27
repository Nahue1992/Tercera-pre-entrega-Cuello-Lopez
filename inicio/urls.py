from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('bonos/crear/', views.crear_bono, name= 'crear_bono'),
    path('acciones/crear/', views.crear_accion, name= 'crear_accion'),
    path('futuros/crear/', views.crear_futuro, name= 'crear_futuro'),
]

