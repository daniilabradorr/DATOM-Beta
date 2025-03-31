#Archivo para defnir los formularios que necesitaremos en la App 'core' (general)

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Formulario de autenticación personalizado
class CustomLoginForm(AuthenticationForm):
    # Campo de nombre de usuario con un widget de entrada de texto
    username = forms.CharField(
        label='Username',  # Etiqueta del campo
        widget=forms.TextInput(attrs={'autofocus': True})  # Widget de entrada de texto con autofocus
    )
    # Campo de contraseña con un widget de entrada de contraseña
    password = forms.CharField(
        label='Password',  # Etiqueta del campo
        widget=forms.PasswordInput  # Widget de entrada de contraseña que oculta los caracteres
    )

# Formulario de creación de usuario personalizado (DE REGISTRO)
class CustomUserCreationForm(forms.ModelForm):
    # Campo de contraseña con un widget de entrada de contraseña
    password1 = forms.CharField(
        label='Password',  # Etiqueta del campo
        widget=forms.PasswordInput  # Widget de entrada de contraseña que oculta los caracteres
    )
    # Campo de confirmación de contraseña con un widget de entrada de contraseña
    password2 = forms.CharField(
        label='Confirm Password',  # Etiqueta del campo
        widget=forms.PasswordInput  # Widget de entrada de contraseña que oculta los caracteres
    )

    class Meta:
        model = User  # Modelo de usuario predeterminado de Django
        fields = ['username', 'email']  # Campos del modelo que se incluirán en el formulario

    # Validación personalizada para asegurar que las contraseñas coincidan
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("las contraseñas no coinciden")
        return password2

    # Guardar el usuario con la contraseña encriptada
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

