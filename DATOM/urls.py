#Archivo de urls del proyecto(del proyecto no de una app del proyecto)
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


app_name= 'DATOM'

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("scrap/", include("scrap.urls", namespace="scrap")),
    path("down/", include("down.urls", namespace="down")),
    path("produccion/", include("produccion.urls", namespace="produccion")),
    path("admin/", admin.site.urls),
]
