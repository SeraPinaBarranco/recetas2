from django.urls import path
from .views import IndiceGeneral, InicioCaloriasview, CrearReceta

urlpatterns = [

    path('', IndiceGeneral.as_view(), name='indice_general'),
    path('indice_calorias/', InicioCaloriasview.as_view(), name='indice_calorias'),
    path('crear_receta/', CrearReceta.as_view(), name='crear_receta'),
    
]