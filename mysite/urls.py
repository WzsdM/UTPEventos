from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name='login' ),
    path('logout/', views.log_out, name='logout' ),
    path('home/', views.home, name='home' ),
    path('detalle/<int:id>', views.evento_detail, name='evento_detail' ),
    path('administrar/', views.administrar_evento, name='administrar_evento' ),
    path('crear/', views.crear_evento, name='crear_evento' ),
    path('registrar_asistencia/', views.registar_asistencia_evento, name='registrar_asistencia' ),
    path('evento_admin_detail/<int:id>', views.evento_admin_detail, name='evento_admin_detail' ),
    path('estadisticas/', views.estadisticas, name='estadisticas' ),
    path('editar_usuarios/', views.editar_usuarios, name='editar_usuarios' ),
    
    
]