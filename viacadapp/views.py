from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse  
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
from .functions import CrearMaterias 
from .forms import FormularioInscripcionProfesores 
from .forms import FormularioInscripcionAlumnos 
from .forms import LoginForm 

from .forms import ElegirMateria 
from .forms import FormularioSolicitud
from django.core.mail import send_mail
from django.core import mail
from django.core.mail import EmailMessage
import smtplib
import datetime
from smtplib import SMTPException

from .models import Profesores
from .models import Alumnos
from .models import Materias
from .models import Solicitud

# Create your views here.
def index(request):
	try:
		if (request.session['registrado']==1):
			temp=request.session['registrado']
			del request.session['registrado']
			return render(request,'viacadapp/index.html',{'message':temp})
	except:
		return render(request,'viacadapp/index.html')

def registroProfesores(request):
	#CrearMaterias()
	#generate form
	if request.method=='POST':
		form=FormularioInscripcionProfesores(request.POST, request.FILES)
		registrado=0
		if form.is_valid():
			#nc=form.cleaned_data['nombrecompleto']
			#correo= form.cleaned_data['correo']
			#contra= form.cleaned_data['contraseña']
			#foto= request.FILES['foto']
			#mat= form.cleaned_data['materia']
			#cuali=form.cleaned_data['cualidades']
			#hora=form.cleaned_data['costohora']
			#g=Profesores(nombrecompleto=nc, correo=correo, contraseña=contra, foto=foto,
			# 			materia=mat, cualidades=cuali, costohora=hora)
			#g.save()
			form.save()
			registrado=1
			request.session['registrado']=registrado
			return redirect("/")
	else:
		form=FormularioInscripcionProfesores()
		return render(request, 'viacadapp/registroProfesores.html',{'form':form})


def registroAlumnos(request):
	if request.method=='POST':
		form=FormularioInscripcionAlumnos(request.POST, request.FILES)
		registrado=0
		if form.is_valid():
			nc=form.cleaned_data['nombrecompletoal']
			correoal= form.cleaned_data['correoal']

			contra= form.cleaned_data['contraseñaal']
			g=Alumnos(nombrecompletoal=nc, correoal=correoal, contraseñaal=contra)
			g.save()
			request.session['correoal']=correoal
			print(correoal)
			registrado=1
			request.session['registrado']=registrado
			return redirect("buscarprof/")
	else:
		form=FormularioInscripcionAlumnos()
		return render(request, 'viacadapp/registroAlumnos.html',{'form':form})

def buscarprof(request):
	if request.method=='POST':
		form=ElegirMateria(request.POST)

		if form.is_valid():
			sheet=form.cleaned_data['category']	
			request.session['sheet']=sheet #Materia seleccionada
			print(sheet)
			listaprofes = Profesores.objects.filter(materia__contains=request.session['sheet'])
			correo=list(Profesores.objects.values_list('correo',flat=True).filter(materia__contains=request.session['sheet']))
			print(correo)
			return render(request, 'viacadapp/buscarprof.html',{'form':form, 'listaprofes': listaprofes})
	else:
		form=ElegirMateria()

	return render(request, 'viacadapp/buscarprof.html',{'form':form})

def registroSolicitud(request):
	if request.method=='POST':
		form=FormularioSolicitud(request.POST, request.FILES)
		if form.is_valid():
			resp=form.cleaned_data['responsable']
			casa= form.cleaned_data['direccion']
			fecha= form.cleaned_data['fecha']
			correoal = request.session.get('correoal')
			print(correoal)
			g=Solicitud(responsable=resp, direccion=casa, fecha=fecha)
			g.save()
			smtp=smtplib.SMTP('smtp.gmail.com')
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login('alexacaro14', 'cosafa2008')
			FROM= 'alexacaro14'
			TO= str(correoal)
			formato = "%m-%d-%Y"
			dia  = fecha.strftime(formato)
			asunto= 'Confirmacion de solicitud'
			mensaje= 'Ha solicitado una tutoria a nombre de ' + resp+ ' , la cual se llevara a cabo en la '+ casa + ' el dia ' + dia+ '. Gracias por elegirnos'
			texto = message = """From: %s\nTo: %s\nSubject: %s\n\n%s
			""" % (FROM, ", ".join(TO), asunto, mensaje) 
			smtp.sendmail(FROM, correoal, texto)
			return redirect("buscarprof/")
			
	else:
		form=FormularioSolicitud()
		return render(request, 'viacadapp/elegido.html',{'form':form})
  
def login(request):
    if request.method=='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            Email=form.cleaned_data['email']
            Password=form.cleaned_data['password']
            #print(Email)
            #print(Password)
            correo=list(Profesores.objects.values_list('correo',flat=True).filter(correo=Email))
            contra=list(Profesores.objects.values_list('contraseña',flat=True).filter(contraseña=Password))
            correo=str(correo).replace("['",'')
            contra=str(contra).replace("['",'')
            correo=str(correo).replace("']",'')
            contra=str(contra).replace("']",'')
            correoalum=list(Alumnos.objects.values_list('correoal',flat=True).filter(correoal=Email))
            contraalum=list(Alumnos.objects.values_list('contraseñaal',flat=True).filter(contraseñaal=Password))
            correoalum=str(correoalum).replace("['",'')
            contraalum=str(contraalum).replace("['",'')
            correoalum=str(correoalum).replace("']",'')
            contraalum=str(contraalum).replace("']",'')
            #print(contraalum)
            #print(correoalum)
            if (correo==Email and Password==contra) :
            	print('%s %s' % (Email, Password))
            	request.session['Logged']=True
            	request.session['correolog']=Email
            	return redirect("/perfilprof/")
            elif (correoalum==Email and Password==contraalum):
            	print('%s %s' % (Email, Password))
            	request.session['Logged']=True
            	request.session['correolog']=Email
            	return redirect("/perfilalum/")

    else:
        form=LoginForm()
    return render(request,'viacadapp/login.html',{'form':form})


def perfilprof(request):
	perfilusuario = Profesores.objects.filter(correo=request.session['correolog'])
	return render(request,'viacadapp/perfilprof.html',{'perfilusuario':perfilusuario})

def perfilalum(request):
	perfilusuario = Alumnos.objects.filter(correoal=request.session['correolog'])
	return render(request,'viacadapp/perfilalum.html',{'perfilusuario':perfilusuario})
