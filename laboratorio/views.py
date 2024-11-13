from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

def ListadoLaboratorio(request):
    busqueda = request.GET.get('busqueda', '')

    if busqueda:
        laboratorios = Laboratorio.objects.filter(nombre__icontains=busqueda)
    else:
        laboratorios = Laboratorio.objects.all()

    total_laboratorios = laboratorios.count()

    paginator = Paginator(laboratorios, 10)

    page_number = request.GET.get('page')  # page es el parámetro de la URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'listado_laboratorio.html',  {'page_obj': page_obj,'total_laboratorios': total_laboratorios})

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorios')  # Redirige a la lista de productos después de crear uno nuevo
            
    else:
        form = LaboratorioForm()

    errores = {field: form[field].errors for field in form.fields if form[field].errors}

    return render(request, 'crear_laboratorio.html', {'form': form, 'errores': errores})
