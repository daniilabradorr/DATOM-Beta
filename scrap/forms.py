from django import forms
from .models import Scrap

class ScrapForm(forms.ModelForm):
    class Meta:
        model = Scrap
        fields = ['nombre_proyecto', 'nombre_pieza', 'tipoDe_defecto', 'cantidad']  
