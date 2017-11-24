from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profesores(models.Model):
	nombrecompleto= models.CharField(max_length= 80)
	correo= models.EmailField(max_length= 100, )
	contraseña= models.CharField(max_length=32)
	foto= models.ImageField(upload_to="viacadapp/images/")
	materia= models.CharField(max_length=250)
	cualidades= models.CharField(max_length= 250)
	costohora= models.IntegerField(default=0)

class Materias(models.Model):
  materia= models.CharField(max_length=34)
  class Meta:
    managed=False
    db_table = 'viacadapp_materias'

  def __str__(self):
    return self.materia

class Alumnos(models.Model):
	nombrecompletoal= models.CharField(max_length= 80)
	correoal= models.EmailField(max_length= 100)
	contraseñaal= models.CharField(max_length=32)
class Solicitud(models.Model):
	responsable= models.CharField(max_length=80)
	direccion=models.CharField(max_length=30)
	fecha=models.DateTimeField(auto_now_add=True)



