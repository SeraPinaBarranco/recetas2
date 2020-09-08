from django import forms
from .models import NombreRecetas

class FormRecetas(forms.ModelForm):    
    #nombre_receta= forms.CharField(label='Título', max_length=80)
    def __init__(self, *args, **kwargs):
        super(FormRecetas, self).__init__(*args, **kwargs)    
   
    class Meta:
        model = NombreRecetas
        fields= ['titulo',]

        widgets = {
            'titulo': forms.TextInput(attrs=
                {'class':'form-control ml-3 mb-2 text-center'}),
        }