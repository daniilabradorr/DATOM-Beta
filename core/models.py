from django.db import models
from django.contrib.auth.models import User

# Modelo para registrar los logs de inicios de sesión.
class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100, unique=True)  # Garantiza que no haya nombres duplicados

    def __str__(self):
        return self.nombre_proyecto
