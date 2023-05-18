from django.db import models

# Create your models here.

class Proveedor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()

    def __str__(self):
        return str(self.nombre +' '+ self.apellido)

class Producto(models.Model):

    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)