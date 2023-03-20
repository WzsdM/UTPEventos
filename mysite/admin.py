from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario,Evento,Asistente,Carrera,Ponente,Rol,TipoAsistente

# Register your models here.

admin.site.register([Usuario,Rol,Evento,Asistente,Carrera,Ponente,TipoAsistente])
#admin.site.register(User)
