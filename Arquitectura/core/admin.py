from admin_confirm import AdminConfirmMixin
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


class VehiculoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['modelo', 'marca', 'propietario', 'cant_puertas', 'cant_pasajeros', 'transmision', 'capacidad', 'velo_maxima', 'image']

class MarcaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['descripcion']

class MantenimientoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['fecha_revision', 'descripcion']

class AgendarHoraModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre', 'email', 'capacidad', 'servicio']

class ProductoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre', 'categoria', 'precio', 'image']

class VentaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['fecha', 'total', 'total_usd', 'usuario']

class ProductoVentaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['Venta', 'Producto', 'cantidad', 'total']

class ClasificacionTallerModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre']

class InstructorModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre', 'especialidad']

class DiaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre']

class TallerModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre', 'clasificacion_taller_id']

# Register your models here.
admin.site.register(Vehiculo, VehiculoModelAdmin)
admin.site.register(Marca, MarcaModelAdmin)
admin.site.register(Mantenimiento, MantenimientoModelAdmin)
admin.site.register(AgendarHora, AgendarHoraModelAdmin)
admin.site.register(Producto, ProductoModelAdmin)
admin.site.register(Venta, VentaModelAdmin)
admin.site.register(Producto_Venta, ProductoVentaModelAdmin)
admin.site.register(Clasificacion_taller)
admin.site.register(Instructor)
admin.site.register(Dia)
admin.site.register(Taller)
admin.site.register(Inscripcion_taller)