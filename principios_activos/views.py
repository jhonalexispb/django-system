from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from .models import PrincipioActivo
from .forms import PrincipioActivoForm

def ListadoPrincipiosActivos(request):
    busqueda = request.GET.get('busqueda', '')

    if busqueda:
        principios_activos = PrincipioActivo.objects.filter(nombre__icontains=busqueda) | PrincipioActivo.objects.filter(valor_minimo__icontains=busqueda)
    else:
        principios_activos = PrincipioActivo.objects.all()

    

    total_principios_activos = principios_activos.count()

    paginator = Paginator(principios_activos, 2)

    page_number = request.GET.get('page')  # page es el parámetro de la URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'listado_principios_activos.html', {'page_obj': page_obj,'total_principios_activos': total_principios_activos})

def ObtenerPrincipiosActivosUnicos(request):
    if request.method == 'GET':
        # Usamos values_list() con distinct() para obtener los valores únicos de 'nombre'
        principios_activos_unicos = PrincipioActivo.objects.values_list('nombre', flat=True).distinct()
        
        # Convertir el queryset a una lista para poder devolverlo como respuesta JSON
        principios_activos_lista = list(principios_activos_unicos)
        
        # Devolver los resultados como respuesta JSON
        return JsonResponse({'principios_activos': principios_activos_lista})
    
    return JsonResponse({'errors': 'Método no permitido.'}, status=405)

def crear_principio_activo(request):
    if request.method == 'POST':
        # Recibir los datos del formulario
        form = PrincipioActivoForm(request.POST)
        
        # Validar los datos con el formulario
        if form.is_valid():
            nombre = form.cleaned_data['nombrePrincipioActivo'].strip().lower()  # Normaliza el nombre (minúsculas y elimina espacios)
            concentracion = form.cleaned_data['concentracion'].strip().lower()  # Normaliza la concentración (minúsculas y elimina espacios)
            
            # Verificar si ya existe un principio activo con el mismo nombre y concentración normalizados
            if PrincipioActivo.objects.filter(nombre=nombre, concentracion=concentracion).exists():
                # Si ya existe, devolver un error en formato JSON
                return JsonResponse({'error': f"El principio activo '{nombre} {concentracion}' ya existe."}, status=422)
            
            # Si no existe, crear y guardar el nuevo principio activo
            principio_activo = PrincipioActivo.objects.create(
                nombre=form.cleaned_data['nombrePrincipioActivo'],
                concentracion=form.cleaned_data['concentracion']
            )
            return JsonResponse({'success': 'Principio activo creado correctamente.'})
        else:
            # Si el formulario no es válido, devolver los errores en formato JSON
            return JsonResponse({'errors': form.errors}, status=422)
    
    return JsonResponse({'errors': 'Método no permitido.'}, status=405)

