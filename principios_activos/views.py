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

    paginator = Paginator(principios_activos, 10)

    page_number = request.GET.get('page')  # page es el parámetro de la URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'listado_principios_activos.html', {'page_obj': page_obj,'total_principios_activos': total_principios_activos})

def crear_principio_activo(request):
    if request.method == 'POST':
        # Recibir los datos del formulario
        form = PrincipioActivoForm(request.POST)
        
        # Validar los datos con el formulario
        if form.is_valid():
            # Si los datos son válidos, guardarlos en la base de datos
            principio_activo = PrincipioActivo.objects.create(
                nombre=form.cleaned_data['nombre'],
                concentracion=form.cleaned_data['concentracion']
            )
            return JsonResponse({'success': 'Principio activo creado correctamente.'})
        else:
            # Si el formulario no es válido, devolver los errores en formato JSON
            return JsonResponse({'error': form.errors}, status=422)
    
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

