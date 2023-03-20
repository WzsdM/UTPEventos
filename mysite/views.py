from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.context_processors import auth
from .models import *
from .auth import VerifyPwd

# Create your views here.

#Entrar a la sesión del usuario
def userLogin(request):
    context = {
        'form': AuthenticationForm()
    }
    if request.method == 'POST':
        very_user = VerifyPwd(request)
        if very_user is not None:
            user_session = {
                'nombre': very_user[0].nombre_usuario,
                'codigo':very_user[0].codigo,
                'id': very_user[0].pk,
                'rol': very_user[0].rol.pk
            }
            request.session['usuario'] = user_session
            context['auth'] = True
            return redirect('home')
        else:
            context['error'] = 'Error en la contraseña o código'
            return render(request, 'login.html',context)
    else:
        return render(request, 'login.html',context)
    
    
#Salir de la sesión
def log_out(request):
    del request.session['usuario']
    return redirect('login')
    
#Segunda plantilla del proyecto, acá aparecen todos los evento y el nombre del usuario    
def home(request):
    usuaurio_login = request.session.get('usuario')
    if usuaurio_login is not None:
        context = {
            'usuario': usuaurio_login,
            'auth':True
        }
        return render(request, 'home.html',context)
    else:
        return redirect('login')
        

#Aqui se detalla el evento y aparecen los botones de registrarse
def evento_detail(request):
    return render(request,'evento_detail.html')

#Panel del organizador, aqui aparecen todos los eventos que ha creado y se podrá  eliminar, actualizar, etc
def administrar_evento(request):
    return render(request,'administrar_evento.html')

#Formulario para la creación del evento
def crear_evento(request):
    return render(request,'crear_evento.html')

#Escogemos cual de los eventos vamos a generar las asistencias
def registar_asistencia_evento(request):
    return render(request,'registar_asistencia_evento.html')

#Se detalla el evento desde el panel del organizador, aparecen los botones de generar reporte por pdf o excel
def evento_admin_detail(request):
    return render(request,'evento_admin_detail.html')

#Aparecen las estadisticas
def estadisticas(request):
    return render(request,'estadisticas.html')

#Reporte de los eventos desde el panel de administrador 
def editar_usuarios(request):
    return render(request,'editar_usuarios.html')
  