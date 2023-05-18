from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('lista_productos/',views.lista_productos),
    path('crear_producto/', views.crear_producto),
    path('lista_proveedores/',views.lista_proveedores),
    path('crear_proveedor/', views.crear_proveedor)
]