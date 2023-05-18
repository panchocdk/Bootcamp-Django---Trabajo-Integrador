from django.contrib import admin
from .models import Producto, Proveedor

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    #list display: muestra los atributos del objeto en forma de lista
    list_display=['nombre','precio','stock_actual','proveedor']

    #list filter: muestra un filtro para todos los objetos
    list_filter=['nombre','precio']

    #search fields: abre un campo 'Search' para poder buscar por los campos indicados
    search_fields=['nombre']


class ProveedorAdmin(admin.ModelAdmin):
    #list display: muestra los atributos del objeto en forma de lista
    list_display=['nombre','apellido','dni']

    #list filter: muestra un filtro para todos los objetos
    list_filter=['nombre','apellido']

    #search fields: abre un campo 'Search' para poder buscar por los campos indicados
    search_fields=['nombre','apellido']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)