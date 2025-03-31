from django.urls import path
from . import views

app_name = 'scrap'

urlpatterns = [
    path('', views.scrap_home, name='scrap_home'),  # Ruta para la página principal de Scrap
    path('list/', views.scrap_list, name='scrap_list'),  # Ruta para listar todos los Scraps
    path('detail_form/', views.scrap_detail_form, name='scrap_detail_form'),  # Ruta para el formulario de detalles de Scrap
    path('detail/<int:id>/', views.scrap_detail, name='scrap_detail'),  # Ruta para ver los detalles de un Scrap específico
    path('new/', views.scrap_new, name='scrap_new'),  # Ruta para crear un nuevo Scrap
    path('new_confirm/', views.scrap_new_confirm, name='scrap_new_confirm'),  # Ruta para confirmar el nuevo Scrap
    path('edit_form/', views.scrap_edit_form, name='scrap_edit_form'),  # Ruta para el formulario de edición de Scrap
    path('edit/<int:id>/', views.scrap_edit, name='scrap_edit'),  # Ruta para editar un Scrap específico
    path('delete_form/', views.scrap_delete_form, name='scrap_delete_form'),# Ruta para el formulario de eliminación de Scrap
    path('delete/<int:id>/', views.scrap_delete, name='scrap_delete'),  # Ruta para eliminar un Scrap específico
    path('delete_confirm/<int:id>', views.scrap_delete_confirm, name='scrap_delete_confirm'),  # Ruta para confirmar eliminación de un Scrap
    path('visualizacion/', views.visualitation, name='visualizacion'),  # Ruta para la visualización de Dashboards y Gráficos
   
]
