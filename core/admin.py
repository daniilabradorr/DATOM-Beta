from django.contrib import admin
from .models import LoginLog, Proyecto

# Configuración del modelo LoginLog en el administrador
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'ip_address')  # Muestra estos campos en la lista
    search_fields = ('user__username', 'ip_address')  # Permite buscar por usuario y dirección IP
    list_filter = ('timestamp', 'user')  # Añade filtros por usuario y fecha

admin.site.register(LoginLog, LoginLogAdmin)

# Configuración del modelo Proyecto en el administrador
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre_proyecto',)  # Muestra solo el nombre del proyecto en la lista
    search_fields = ('nombre_proyecto',)  # Permite buscar proyectos por nombre

admin.site.register(Proyecto, ProyectoAdmin)
