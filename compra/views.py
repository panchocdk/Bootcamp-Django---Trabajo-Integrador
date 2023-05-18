from django.shortcuts import render, redirect
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm


# Create your views here.

def home(request):
    return render(request, 'index.jinja')


def lista_productos(request):
    try:
        productos=Producto.objects.all()
        context={
            'productos':productos
        }
        return render(request,'lista_productos.jinja', context)
    except Exception:
        return render(request, 'error.jinja')
    
def crear_producto(request):
    #Instancia de ProductoForm
    form=ProductoForm()
    if request.POST:
        form=ProductoForm(request.POST)
        if form.is_valid():
            producto=Producto(
                nombre=form.cleaned_data['nombre'],
                precio=form.cleaned_data['precio'],
                stock_actual=form.cleaned_data['stock_actual'],
                proveedor=form.cleaned_data['proveedor']
            )
            producto.save()
            return redirect('/lista_productos/')
        else:
            return redirect('/lista_productos/')
    context={'form':form}
    return render(request, 'crear_producto.jinja', context)


def lista_proveedores(request):
    try:
        proveedores=Proveedor.objects.all()
        context={
            'proveedores':proveedores
        }
        return render(request,'lista_proveedores.jinja', context)
    except Exception:
        return render(request, 'error.jinja')
    
def crear_proveedor(request):
    #Instancia de ProveedorForm
    form=ProveedorForm()
    if request.POST:
        form=ProveedorForm(request.POST)
        if form.is_valid():
            proveedor=Proveedor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                dni=form.cleaned_data['dni']
            )
            proveedor.save()
            return redirect('/lista_proveedores/')
        else:
            return redirect('/lista_proveedores/')
    context={'form':form}
    return render(request, 'crear_proveedor.jinja', context)