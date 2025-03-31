from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from .models import Scrap
from core.models import Proyecto
from .forms import ScrapForm
from django.utils import timezone
from django.contrib import messages  # Para lanzar mensajes de éxito y error

# Vista home de SCRAP
def scrap_home(request):
    scraps = Scrap.objects.all()  # Obtener todos los Scraps
    return render(request, 'scrap/scrap_home.html', {'scraps': scraps})  # Renderizar la página principal con los Scraps

# Vista de listeo de scraps
@login_required
@permission_required('scrap.puede_listar_scrap', raise_exception=True)
def scrap_list(request):
    query = request.GET.get('q')  # Filtro por texto
    date_query = request.GET.get('date')  # Filtro por fecha
    scraps = Scrap.objects.all()  # Obtener todos los registros inicialmente

    # Filtrar por nombre de proyecto o pieza
    if query:
        scraps = scraps.filter(
            models.Q(nombre_proyecto__nombre_proyecto__icontains=query) |  # Filtro por proyecto
            models.Q(nombre_pieza__icontains=query)  # Filtro por pieza
        )
    
    # Filtrar por fecha
    if date_query:
        scraps = scraps.filter(fecha_reporte=date_query)

    return render(request, 'scrap/scrap_list.html', {'scraps': scraps})  # Renderizar la lista de scraps

#Vista de formulario de detalle de scrap
@login_required
@permission_required('scrap.puede_detallar_scrap', raise_exception=True)
def scrap_detail_form(request):
    if request.method == "POST":
        id = request.POST.get('id')  # Obtener el ID del formulario
        return redirect('scrap:scrap_detail', id=id)  # Redirigir a la vista de detalles del Scrap
    return render(request, 'scrap/forms/scrap_detail_form.html')  # Renderizar el formulario de detalles

#VIsta para detallar un scrap
@login_required
@permission_required('scrap.puede_detallar_scrap', raise_exception=True)
def scrap_detail(request, id):
    scrap = get_object_or_404(Scrap, id=id)  # Obtener el Scrap por ID o devolver 404
    return render(request, 'scrap/scrap_detail.html', {'scrap': scrap})  # Renderizar los detalles del Scrap

#VIsta para crear un nuevo scrap
@login_required
@permission_required('scrap.puede_crear_scrap', raise_exception=True)
def scrap_new(request):
    if request.method == "POST":
        form = ScrapForm(request.POST)  # Crear un formulario con los datos POST
        if form.is_valid():
            scrap = form.save(commit=False)
            # Insertar automáticamente la fecha
            scrap.fecha_reporte = timezone.now()
            # Guardar los datos en la sesión para la confirmación
            request.session['scrap_data'] = {
                'nombre_proyecto_id': scrap.nombre_proyecto.id,  # Almacenar el ID del proyecto
                'nombre_pieza': scrap.nombre_pieza,
                'tipoDe_defecto': scrap.tipoDe_defecto,
                'cantidad': scrap.cantidad,
                'fecha_reporte': scrap.fecha_reporte.strftime('%Y-%m-%d'),
            }
            return redirect('scrap:scrap_new_confirm')
    else:
        form = ScrapForm()  # Crear un formulario vacío
    return render(request, 'scrap/forms/scrap_new_form.html', {'form': form})  # Renderizar el formulario de creación

#Vista pra confirmar nuevo scrap
@login_required
@permission_required('scrap.puede_crear_scrap', raise_exception=True)
def scrap_new_confirm(request):
    scrap_data = request.session.get('scrap_data')
    if not scrap_data:
        return redirect('scrap:scrap_new')  # Redirigir si no hay datos en la sesión

    if request.method == "POST":
        # Usar el ID almacenado en la sesión para recuperar el objeto Proyecto
        proyecto = get_object_or_404(Proyecto, id=scrap_data['nombre_proyecto_id'])
        scrap = Scrap(
            nombre_proyecto=proyecto,  # Usar el objeto Proyecto recuperado
            nombre_pieza=scrap_data['nombre_pieza'],
            tipoDe_defecto=scrap_data['tipoDe_defecto'],
            cantidad=scrap_data['cantidad'],
            fecha_reporte=scrap_data['fecha_reporte'],
        )
        scrap.save()
        messages.success(request, 'Scrap añadido correctamente')
        return redirect('scrap:scrap_detail', id=scrap.id)

    return render(request, 'scrap/scrap_new.html', {'scrap': scrap_data})


#vista de formulario para editar scrap
@login_required
@permission_required('scrap.puede_editar_scrap', raise_exception=True)
def scrap_edit_form(request):
    if request.method == "POST":
        id = request.POST.get('id')  # Obtener el ID del formulario
        return redirect('scrap:scrap_edit', id=id)  # Redirigir a la vista de edición del Scrap
    return render(request, 'scrap/forms/scrap_edit_form.html')  # Renderizar el formulario de edición

#Vista para editar scrap
@login_required
@permission_required('scrap.puede_editar_scrap', raise_exception=True)
def scrap_edit(request, id):
    try:
        scrap = Scrap.objects.get(id=id)  # Intentar obtener el Scrap
    except Scrap.DoesNotExist:
        # Si no existe, renderizar un mensaje de error
        messages.error(request, f'El Scrap con ID {id} no existe en la base de datos.')
        return redirect('scrap:scrap_list')  # Redirigir a la lista de scraps

    if request.method == "POST":
        form = ScrapForm(request.POST, instance=scrap)  # Crear un formulario con los datos POST y el Scrap existente
        if form.is_valid():
            scrap = form.save(commit=False)  # Guardar el formulario sin confirmar
            scrap.save()  # Guardar el Scrap
            messages.success(request, 'Scrap editado correctamente')  # Mensaje de éxito
            return redirect('scrap:scrap_detail', id=scrap.id)  # Redirigir a los detalles del Scrap
    else:
        form = ScrapForm(instance=scrap)  # Crear un formulario con el Scrap existente
    return render(request, 'scrap/scrap_edit.html', {'form': form})


#Vista de fomulario para eliminar Scrap
@login_required
@permission_required('scrap.puede_eiminar_scrap', raise_exception=True)
def scrap_delete_form(request):
    if request.method == "POST":
        id = request.POST.get('id')  # Obtener el ID del formulario
        return redirect('scrap:scrap_delete_confirm', id=id)  # Redirigir a la vista de eliminación del Scrap
    return render(request, 'scrap/forms/scrap_delete_form.html')  # Renderizar el formulario de eliminación

#Vista de Eliminar Scrap
@login_required
@permission_required('scrap.puede_eiminar_scrap', raise_exception=True)
def scrap_delete(request, id):
    scrap = get_object_or_404(Scrap, id=id)  # Obtener el Scrap por ID o devolver 404
    try:
        scrap.delete()  # Eliminar el Scrap
        messages.success(request, 'Scrap Eliminado correctamente')  # Mensaje de éxito
    except Exception as e:
        messages.error(request, f'Hubo algún error a la hora de eliminar el Scrap: {e}')  # Mensaje de error
    return redirect('scrap:scrap_list')  # Redirigir a la lista de Scraps

#VIsta para confirmar la eliminacion de un Scrao
@login_required
@permission_required('scrap.puede_eiminar_scrap', raise_exception=True)
def scrap_delete_confirm(request, id):
    try:
        scrap = Scrap.objects.get(id=id)  # Intentar obtener el Scrap
    except Scrap.DoesNotExist:
        # Si no existe, renderizar un mensaje de error
        messages.error(request, f'El Scrap con ID {id} no existe en la base de datos.')
        return redirect('scrap:scrap_list')  # Redirigir a la lista de scraps

    if request.method == "POST":
        try:
            scrap.delete()
            messages.success(request, 'Scrap eliminado correctamente')
        except Exception as e:
            messages.error(request, f'Hubo un error al eliminar el Scrap: {e}')
        return redirect('scrap:scrap_list')

    return render(request, 'scrap/scrap_delete_confirm.html', {'scrap': scrap})



@login_required
def visualitation(request):
    # Obtener datos del modelo Scrap con relación a Proyecto
    data = Scrap.objects.select_related('nombre_proyecto').all()

    # Datos para el primer gráfico: Cantidad de Defectos por Proyecto
    defectos_por_proyecto = {}
    for record in data:
        proyecto = record.nombre_proyecto.nombre_proyecto  # Acceso al atributo relacionado
        cantidad = record.cantidad
        if proyecto in defectos_por_proyecto:
            defectos_por_proyecto[proyecto] += cantidad
        else:
            defectos_por_proyecto[proyecto] = cantidad

    # Datos para el segundo gráfico: Cantidad de Defectos por Tipo de Defecto
    defectos_por_tipo = {}
    for record in data:
        tipo = record.tipoDe_defecto
        cantidad = record.cantidad
        if tipo in defectos_por_tipo:
            defectos_por_tipo[tipo] += cantidad
        else:
            defectos_por_tipo[tipo] = cantidad

    # Datos para el tercer gráfico: Cantidad de Datos Introducidos por Técnico/Usuario
    datos_por_usuario = {}
    for record in data:
        usuario = record.nombre_pieza  # Suponiendo que 'nombre_pieza' representa al técnico/usuario
        cantidad = record.cantidad
        if usuario in datos_por_usuario:
            datos_por_usuario[usuario] += cantidad
        else:
            datos_por_usuario[usuario] = cantidad

    # Cálculo para el gráfico de pastel: Distribución por Tipo de Defecto (porcentual)
    total_defectos = sum(defectos_por_tipo.values())
    defectos_por_tipo_percent = {k: (v / total_defectos) * 100 for k, v in defectos_por_tipo.items()}

    # Convertir los diccionarios en listas de claves y valores para Highcharts
    defectos_por_proyecto_keys = list(defectos_por_proyecto.keys())
    defectos_por_proyecto_values = list(defectos_por_proyecto.values())

    defectos_por_tipo_keys = list(defectos_por_tipo.keys())
    defectos_por_tipo_values = list(defectos_por_tipo.values())

    defectos_por_tipo_percent_keys = list(defectos_por_tipo_percent.keys())
    defectos_por_tipo_percent_values = list(defectos_por_tipo_percent.values())

    datos_por_usuario_keys = list(datos_por_usuario.keys())
    datos_por_usuario_values = list(datos_por_usuario.values())

    # Pasamos todos estos datos a la plantilla
    return render(request, 'scrap/visualizacion.html', {
        'defectos_por_proyecto_keys': defectos_por_proyecto_keys,
        'defectos_por_proyecto_values': defectos_por_proyecto_values,
        'defectos_por_tipo_keys': defectos_por_tipo_keys,
        'defectos_por_tipo_values': defectos_por_tipo_values,
        'datos_por_usuario_keys': datos_por_usuario_keys,
        'datos_por_usuario_values': datos_por_usuario_values,
        'defectos_por_tipo_percent_keys': defectos_por_tipo_percent_keys,
        'defectos_por_tipo_percent_values': defectos_por_tipo_percent_values,
    })
