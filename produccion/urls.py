from django.urls import path
from . import views
from .views  import home_produccion_view
app_name = 'produccion'

urlpatterns = [
    path('', home_produccion_view, name='produccion_home'),
    # otras rutas
]
