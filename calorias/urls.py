from django.urls import path
from .views import InicioCaloriasview, IndiceGeneral

urlpatterns = [
    path('inicio_calorias', InicioCaloriasview.as_view(), name='inicio_calorias'),
    path('', IndiceGeneral.as_view(), name='indice_general'),
]