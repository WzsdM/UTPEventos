from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index' ),
    path('administrarEventos', views.adEventos, name='adEventos' ),
    path('login', views.Login, name='login' ),
]