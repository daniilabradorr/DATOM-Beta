from django.urls import path
from . import views
from .views import home_down_view

app_name = 'down'

urlpatterns = [
    path('', home_down_view, name='down_home'),
    # otras rutas
]
