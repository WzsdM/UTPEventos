from django.db import models
from django.contrib.auth.hashers import make_password
#from django.contrib.auth.base_user import BaseUserManager
#from django.contrib.auth.models import AbstractUser,AbstractBaseUser
#from django.utils import timezone

# Create your models here.

class Rol(models.Model):
  rol_name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.rol_name
  
class Usuario(models.Model):
  nombre_usuario = models.CharField(max_length=50)
  telefono = models.CharField(max_length=9,blank=True)
  contrasena = models.CharField(max_length=100,null=False,blank=False,default='')
  email = models.EmailField(blank=False, null=False)
  codigo = models.CharField(max_length=9,null=False, default='')
  rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.nombre_usuario

  def save(self,*args, **kwargs ):
    self.contrasena = make_password(self.contrasena)
    return super().save(*args, **kwargs)
  
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
  telefono = models.CharField(max_length=9,blank=True)
  email = models.EmailField(blank=False, null=False)
  codigo = models.CharField(max_length=9, null=False, default='')
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
  
  
"""class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser):
    email = models.CharField(max_length=80, unique=True)
    nombre_usuario = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9,blank=True)
    #contrasena = models.CharField(max_length=100,null=False,blank=False,default='')
    #rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre_usuario"]

    def __str__(self):
        return self.nombre_usuario"""

  
  
  