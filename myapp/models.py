from django.db import models
from django.contrib.auth.models import AbstractUser

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


class Usuario(AbstractUser):
    is_staff = models.BooleanField(default=False)
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, unique=True, default='default_username')
    password = models.CharField(max_length=128, null=False)  # Agrega null=False
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_registro = models.DateField()
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', default='default_profile_pic.jpg')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Agrega related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Agrega related_name
    )

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

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
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

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
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.administrador_id

class Inscripcion_taller(models.Model):
    inscripcion_id = models.AutoField(primary_key=True)
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=50)
    adulto_mayor_id = models.ForeignKey(Adulto_Mayor, on_delete=models.CASCADE)
    taller_id = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return self.inscripcion_id

class Funcionario_municipal(models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionario_id