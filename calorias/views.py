from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class InicioCaloriasview(TemplateView):
    template_name= 'calorias/indice_calorias.html'


class IndiceGeneral(TemplateView):
    template_name= 'calorias/indice_general.html'