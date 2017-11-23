from django import forms
from .functions import ListaMaterias
from .models import Materias
from .models import Profesores 
from .models import Solicitud 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class FormularioInscripcionProfesores(forms.ModelForm):
	nombrecompleto= forms.CharField(label='Nombre Completo',max_length= 80)
	correo= forms.EmailField(max_length= 100)
	contraseña= forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Contraseña', 'style':'width:20%'
		}))
	foto = forms.ImageField(label='Agregar Foto de Perfil')

	choices= ListaMaterias()
	choices1= choices.pop(0)
	materia= forms.MultipleChoiceField(label='Materias que desea enseñar',choices= choices, 
										widget=forms.CheckboxSelectMultiple(attrs=
											{'class':'checkbox-inline'}))
	cualidades= forms.CharField(label='Cualidades',max_length= 250)
	costohora=forms.IntegerField(label='Valor de la hora de clase')

	class Meta:
		model = Profesores
		fields = '__all__'

class FormularioInscripcionAlumnos(forms.Form):
	nombrecompletoal= forms.CharField(label='Nombre Completo',max_length= 80)
	correoal= forms.EmailField(max_length= 100)
	contraseñaal= forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Contraseña', 'style':'width:20%'
		}))
	
class ElegirMateria(forms.Form):
	choices=list(Materias.objects.values_list('materia',flat=True))
	for i in range(0,len(choices)):
		choices[i]=(choices[i],choices[i])
	category=forms.ChoiceField(label='Seleccione Categoria',choices=choices,widget=forms.Select(attrs={'class':'dropdown-header', 'style':'width:30%'}))
  
class FormularioSolicitud(forms.Form):
	responsable= forms.CharField(label='Nombre Completo del Responsable',max_length= 80)
	direccion = forms.CharField(label='Dirección de domicilio', max_length=30)
	fecha= forms.DateField(label= 'Fecha de tutoría', widget=forms.DateInput(format=('%m-%d-%Y'), 
                               attrs={'class':'myDateClass', 
                               'placeholder':'m-d-a'}))

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e-mail','style':'width:30%'}))
    password = forms.CharField(label='Contraseña', max_length=32,
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña','style':'width:30%'}))