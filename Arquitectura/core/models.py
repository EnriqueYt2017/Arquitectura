from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField
from admin_confirm import AdminConfirmMixin
from django.utils import timezone
import datetime

# Create your models here.
class Marca(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descripcion

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=255)
    cant_puertas = models.IntegerField(default=0)
    cant_pasajeros = models.IntegerField(default=0)
    transmision = models.CharField(max_length=255)
    capacidad = models.IntegerField(default=0)
    velo_maxima = models.IntegerField(default=0)
    image = CloudinaryField('vehiculos')

    def __str__(self) -> str:
        return self.propietario

class Mantenimiento(models.Model):
    fecha_revision = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descripcion


# Create your models here.
class Clasificacion_taller(models.Model):
    clasificacion_taller_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.especialidad
    
class Dia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Taller(models.Model):
    nombre = models.CharField(max_length=255)
    clasificacion_taller_id = models.ForeignKey(Clasificacion_taller, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField(default=datetime.time(8, 0, 0), null=False)
    hora_fin = models.TimeField(default=datetime.time(23, 59, 59), null=False)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)
    cupo_maximo = models.IntegerField()
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    sala = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Taller', null=True, blank=True, default='predeterminada.jpeg')

    def __str__(self) -> str:
        return self.nombre

class Evento_especial(models.Model):
    evento_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_evento = models.DateField()
    taller_id = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class AgendarHora(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    capacidad = models.IntegerField(default=0)
    servicio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class Inscripcion_taller(models.Model):
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)  # Registra fecha y hora
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    taller_id = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inscripción de {self.usuario.username} al taller {self.taller_id}"



class Producto(AdminConfirmMixin, models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.IntegerField()
    image = CloudinaryField('productos')

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    total_usd = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha} -> {self.id}'

class Producto_Venta(models.Model):
    Venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=False, blank=False, related_name='productos')
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False, blank=False)
    cantidad = models.IntegerField(default=0)
    acumulado = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}'