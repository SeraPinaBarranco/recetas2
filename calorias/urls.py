from django.urls import path
from .views import InicioCaloriasview

urlpatterns = [
    path('', InicioCaloriasview.as_view(), name='inicio_calorias'),
]