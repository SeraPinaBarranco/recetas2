from django.contrib import admin
from .models import Productos, NombreRecetas, RecetasIngredientes
# Register your models here.

admin.site.register(Productos)
admin.site.register(NombreRecetas)
admin.site.register(RecetasIngredientes)