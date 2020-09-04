from django.forms import model_to_dict
from django.db import models

# Create your models here.
class Productos(models.Model):
    producto= models.CharField(verbose_name='Producto', max_length=70, null=True, blank=True)
    calorias = models.DecimalField(verbose_name='Calorias', max_digits=6, decimal_places=2)
    grasas= models.DecimalField(verbose_name='Grasas', max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.producto)

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'

class NombreRecetas(models.Model):
    titulo= models.CharField(verbose_name='Titulo', max_length=80)
    ingrediente= models.ManyToManyField(Productos, through='RecetasIngredientes')

    def __str__(self):
        return str(self.titulo)

    class Meta:
        verbose_name= 'NombreReceta'
        verbose_name_plural= 'NombreRecetas'        

class RecetasIngredientes(models.Model):
    nombre_producto= models.ForeignKey(Productos, on_delete=models.CASCADE, null= True, blank= True)
    nombre_receta= models.ForeignKey(NombreRecetas, on_delete=models.CASCADE, null= True, blank= True)
    cantidad= models.DecimalField(verbose_name='Cantidad', max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.nombre_receta)

    class Meta:
        verbose_name= 'RecetasIngrediente'
        verbose_name_plural= 'RecetasIngredientes'



