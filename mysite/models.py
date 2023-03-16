from django.db import models

# Create your models here.

class Rol(models.Model):
  rol_name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.rol_name
  
class Usuario(models.Model):
  nombre_usuario = models.CharField(max_length=50)
  telefono = models.IntegerField(blank=True)
  email = models.EmailField(blank=False, null=False)
  rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=False, blank=False)
  
  def __str__(self):
    return self.nombre_usuario
  
class Carrera(models.Model):
  nombre_carrera = models.CharField(max_length=50)
  
  def __str__(self):
    return self.nombre_carrera
  
  
class TipoAsistente(models.Model):
  nombre_tipo = models.CharField(max_length=50)
  
  def __str__(self):
    return self.nombre_tipo
  
class Asistente(models.Model):
  nombre_asistente = models.CharField(max_length=50)
  telefono = models.IntegerField(blank=True)
  email = models.EmailField(blank=False, null=False)
  carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=False)
  tipo_asistente = models.ForeignKey(TipoAsistente, on_delete=models.SET(value='Default'), null=False)
  
  def __str__(self):
    return self.nombre_asistente


class Ponente(models.Model):
  nombre_ponente = models.CharField(max_length=50)
  telefono = models.IntegerField(blank=True, null=True)
  email = models.EmailField(blank=False, null=False)
  
  def __str__(self):
    return self.nombre_ponente

class Evento(models.Model):
  nombre_evento = models.CharField(max_length=100)
  fecha = models.DateField(null=False, blank=False)
  hora = models.TimeField(null=False, blank=False)
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False)
  carrera = models.ManyToManyField(Carrera, blank=True)
  asistente = models.ManyToManyField(Asistente,blank=False)
  ponente = models.ManyToManyField(Ponente, blank=False)
  
  def __str__(self):
    return self.nombre_evento
  
  

  
  
  