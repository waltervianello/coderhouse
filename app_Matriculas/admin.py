from django.contrib import admin
from.models import Alumno
from.models import Matricula
class AlumnoAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","telefono","correo","direccion","foto_alumno")
class MatriculaAdmin(admin.ModelAdmin):
    list_display=("codigo","tipo","fecha","curso","carrera","fk_alumno")
# Register your models here.

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Matricula,MatriculaAdmin)
