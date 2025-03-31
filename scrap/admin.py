from django.contrib import admin
from .models import Scrap

class ScrapAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_proyecto', 'nombre_pieza', 'tipoDe_defecto', 'cantidad', 'fecha_reporte')  # El id primero
    search_fields = ('nombre_proyecto', 'nombre_pieza')  # Campos que se pueden buscar

admin.site.register(Scrap, ScrapAdmin)
