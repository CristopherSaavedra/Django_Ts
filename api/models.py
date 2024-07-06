from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_client = models.BooleanField(default=False)

class Distrito(models.Model):
   nombre_distrito = models.CharField(max_length=50)
        
class Reporte(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='reportes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    direccion = models.CharField(max_length=255)

