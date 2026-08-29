from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_denuncias, name='lista_denuncias'),
    path('nova/', views.criar_denuncia, name='criar_denuncia'),
]