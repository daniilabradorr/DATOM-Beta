from django.shortcuts import render

# Create your views here.
def home_produccion_view(request):
    return render(request, 'scrap_home.html')