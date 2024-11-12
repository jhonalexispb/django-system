from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def ListadoProducto(request):
    busqueda = request.GET.get('busqueda', '')

    if busqueda:
        productos = Producto.objects.filter(nombre__icontains=busqueda) | Producto.objects.filter(descripcion__icontains=busqueda)
    else:
        productos = Producto.objects.all()

    total_productos = productos.count()

    paginator = Paginator(productos, 10)

    page_number = request.GET.get('page')  # page es el parámetro de la URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'listado_producto.html',  {'page_obj': page_obj,'total_productos': total_productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')  # Redirige a la lista de productos después de crear uno nuevo
        else:
            print(form)
    else:
        form = ProductoForm()

    errores = {field: form[field].errors for field in form.fields if form[field].errors}

    return render(request, 'crear_producto.html', {'form': form, 'errores': errores})