from django.urls import path
from .views import CustomLoginView, CustomRegisterView, LogoutView, home_view, aviso_legal_view, explicacion_view

app_name = 'core'


# URLs para las vistas de login y registro
urlpatterns = [
    path('',home_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),  # URL para la vista de login
    path('register/', CustomRegisterView.as_view(), name='register'),  # URL para la vista de registro
    path('logout/', LogoutView.as_view(next_page='core:home'), name='logout'),  # URL para la vista de logout
    path('aviso_legal/',aviso_legal_view, name="aviso"), #URL para la vista de aviso legal
    path('explicacion/', explicacion_view, name='explicacion') #URL para la ista de explicacion
]
