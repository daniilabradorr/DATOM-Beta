from django.db import models
from core.models import Proyecto

class Scrap(models.Model): 
    nombre_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='scraps')  # Relación automática
    nombre_pieza = models.CharField(max_length=100)
    tipoDe_defecto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha_reporte = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'SCRAP_montaje'
        indexes = [
            models.Index(fields=['nombre_proyecto']),
            models.Index(fields=['nombre_pieza']),
        ]
        permissions = [
            ("puede_detallar_scrap", "Puede detallar Scrap"),
            ("puede_editar_scrap", "Puede editar Scrap"),
            ("puede_listar_scrap", "Puede listar Scrap"),
            ("puede_eiminar_scrap", "Puede eliminar Scrap"),
            ("puede_crear_scrap", "Puede crear Scrap"),
        ]
        constraints = [
            models.UniqueConstraint(fields=['nombre_proyecto', 'nombre_pieza'], name='unique_scrap')  # Garantiza combinaciones únicas
        ]

    def __str__(self):
        return f"{self.nombre_proyecto.nombre_proyecto} - {self.nombre_pieza}"
