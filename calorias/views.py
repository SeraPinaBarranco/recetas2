from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import NombreRecetas
from .form import FormRecetas
# Create your views here.


class IndiceGeneral(TemplateView):
    template_name= 'calorias/indice_general.html'


class InicioCaloriasview(TemplateView):
    template_name= 'calorias/indice_calorias.html'
    #template_name= 'calorias/indice_calorias.html'

    
class CrearReceta(CreateView):
    form_class = FormRecetas
    template_name = "calorias/crear_recetas.html"
    success_url = reverse_lazy('indice_calorias')