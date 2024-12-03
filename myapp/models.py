from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

# Create your models here.
class Adulto_Mayor(models.Model):
    adulto_mayor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido




class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.especialidad

class Sala(models.Model):
    sala_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Reporte(models.Model):
    reporte_id = models.AutoField(primary_key=True)
    tipo_reporte = models.CharField(max_length=50)
    fecha_generacion = models.DateField()
    contenido = models.TextField()

    def __str__(self):
        return self.fecha_generacion

class Clasificacion_taller(models.Model):
    clasificacion_taller_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Taller(models.Model):
    taller_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField(default=datetime.time(8, 0, 0), null=False)
    hora_fin = models.TimeField(default=datetime.time(23, 59, 59), null=False)
    dias = models.CharField(max_length=50, null=False, default=timezone.now)

    cupo_maximo = models.IntegerField()
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    clasificacion_taller_id = models.ForeignKey(Clasificacion_taller, on_delete=models.CASCADE)
    sala_id = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Evento_especial(models.Model):
    evento_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_evento = models.DateField()
    taller_id = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Registro_material(models.Model):
    registro_material_id = models.AutoField(primary_key=True)
    cantidad_utilizada = models.IntegerField()
    taller_id = models.ForeignKey(Taller, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.cantidad

class Administrador(models.Model):
    administrador_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.administrador_id

class Inscripcion_taller(models.Model):
    inscripcion_id = models.AutoField(primary_key=True)
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=50)
    adulto_mayor_id = models.ForeignKey(Adulto_Mayor, on_delete=models.CASCADE)
    taller_id = models.ForeignKey(Taller, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Inscripción de {self.adulto_mayor_id} al taller {self.taller_id}"

class Funcionario_municipal(models.Model):
    funcionario_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.funcionario_id

class Comentario(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    contenido = models.TextField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.comentario_id
    