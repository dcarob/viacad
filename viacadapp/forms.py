from django import forms
from .functions import ListaMaterias
from .models import Materias
from .models import Profesores 
from .models import Solicitud 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class FormularioInscripcionProfesores(forms.ModelForm):
	nombrecompleto= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	correo= forms.EmailField(label= 'Email', max_length= 100, widget=forms.TextInput(attrs=
                                {'class':'form-control',
                                'placeholder':'example@correo.com',
                                'style':'width:30%'}))
	contraseña= forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Contraseña', 'style':'width:20%'
		}))
	foto = forms.ImageField(label='Agregar Foto de Perfil')

	choices= ListaMaterias()
	materia= forms.MultipleChoiceField(label='Materias que desea enseñar',choices= choices, 
										widget=forms.CheckboxSelectMultiple(attrs=
											{'class':'checkbox-inline'}))
	cualidades= forms.CharField(label='Cualidades',max_length= 250, widget=forms.Textarea(attrs=
                                {'class':'form-control',
                                'placeholder':'Descripción corta', 'rows':'5',
                                'style':'width:30%'}))
	costohora=forms.IntegerField(label='Valor de la hora de clase', widget=forms.TextInput(attrs=
                                {'class':'form-control',
                                'placeholder':'$$$',
                                'style':'width:30%'}))

	class Meta:
		model = Profesores
		fields = '__all__'

class FormularioInscripcionAlumnos(forms.Form):
	nombrecompletoal= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	correoal= forms.EmailField(max_length= 100, widget=forms.TextInput(attrs=
                                {'class':'form-control',
                                'placeholder':'example@correo.com',
                                'style':'width:30%'}))
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
	responsable= forms.CharField(label='Nombre Completo del Responsable',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	direccion = forms.CharField(label='Dirección de domicilio', max_length=30, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	fecha= forms.DateField(label= 'Fecha de tutoría', widget=forms.DateInput(format=('%m-%d-%Y'), 
                               attrs={'class':'myDateClass','style':'width:30%', 
                               'placeholder':'m-d-a'}))

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e-mail','style':'width:30%'}))
    password = forms.CharField(label='Contraseña', max_length=32,
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña','style':'width:30%'}))

class FormularioEditarProfesores(forms.ModelForm):
	nombrecompleto= forms.CharField(label='Nombre Completo',max_length= 80)
	correo= forms.EmailField(max_length= 100)
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
		fields = ('nombrecompleto', 'correo', 'foto', 'materia', 'cualidades', 'costohora',)
class FormularioEditarProfesores(forms.Form):
	def __init__(self,*args,**kwargs):
		correo = kwargs.pop('correo')
		perfil = kwargs.pop('perfil')

		super(FormularioEditarProfesores,self).__init__(*args,**kwargs)
		self.fields['correo'].initial = correo
		self.fields['nombrecompleto'].initial = perfil.nombrecompleto
		self.fields['materia'].initial = perfil.materia
		self.fields['costohora'].initial = perfil.costohora
		self.fields['cualidades'].initial = perfil.cualidades
		

	nombrecompleto= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	correo= forms.EmailField(max_length= 100, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	contraseña= forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Contraseña', 'style':'width:20%'
		}))
	foto = forms.ImageField(label='Agregar Foto de Perfil')

	choices= ListaMaterias()
	materia= forms.MultipleChoiceField(label='Materias que desea enseñar',choices= choices, 
										widget=forms.CheckboxSelectMultiple(attrs=
											{'class':'checkbox-inline'}))
	cualidades= forms.CharField(label='Cualidades',max_length= 250, widget=forms.Textarea(attrs=
                                {'class':'form-control', 'rows':'5',
                                'style':'width:30%'}))
	costohora=forms.IntegerField(label='Valor de la hora de clase', widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))

class FormularioEditarAlumnos(forms.Form):
	def __init__(self,*args,**kwargs):
		correoal = kwargs.pop('correoal')
		perfil = kwargs.pop('perfil')

		super(FormularioEditarAlumnos,self).__init__(*args,**kwargs)
		self.fields['correoal'].initial = correoal
		self.fields['nombrecompletoal'].initial = perfil.nombrecompletoal
		
		

	nombrecompletoal= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	correoal= forms.EmailField(max_length= 100, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:30%'}))
	contraseñaal= forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Contraseña', 'style':'width:20%'
		}))
	

