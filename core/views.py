from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import CustomLoginForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy  # Asegúrate de importar reverse_lazy aquí
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


#Vista de la home de la aplicación
def home_view(request):
    return render(request, 'core/home.html')

# Vista de login personalizada
class CustomLoginView(LoginView):
    form_class = CustomLoginForm  # Formulario de autenticación personalizado
    template_name = 'core/login.html'  # Plantilla que se usará para el login
    success_message = 'Usuario logueado correctamente'

# Vista de logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Vista de registro personalizada
class CustomRegisterView(CreateView):
    form_class = UserCreationForm  # Formulario de creación de usuario predeterminado
    template_name = 'core/register.html'  # Plantilla que se usará para el registro
    success_url = reverse_lazy('core:home')  # URL a la que se redirige después del registro exitoso

    def form_valid(self, form):
        # Guardar el nuevo usuario
        user = form.save()
        # Iniciar sesión automáticamente después del registro
        login(self.request, user)
        # Agregar un mensaje de éxito
        messages.success(self.request, '¡Registro exitoso! Estás ahora logueado.')
        # Redirigir a la URL de éxito (home)
        return redirect(self.success_url)

    def form_invalid(self, form):
        # Si el formulario es inválido, mostrar un mensaje de error
        messages.error(self.request, 'Hubo un error en el registro. Por favor, revisa los campos.')
        return super().form_invalid(form)

#Vista del aviso legal de la empresa en la aplicación
def aviso_legal_view(request):
    return render(request, '_includes/_aviso_legal.html')


#Vista explicacion de la aplicación
def explicacion_view(request):
    return render(request, 'core/explicacion.html')