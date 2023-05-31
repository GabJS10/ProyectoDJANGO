from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import miformularioRegistro
# Create your views here.
class vista_registro(View):
	def get(self,request):
		form=miformularioRegistro()

		return render(request,'autenticacion/autenticacion.html',{'formulario':form})

	

	def post(self,request):


		form = miformularioRegistro(request.POST)

		if form.is_valid():

			usuario=form.save()	

			login(request,usuario)

			return redirect('home')
		else:
			for error in form.error_messages:
				messages.error(request, form.error_messages[error])

			return render(request,'autenticacion/autenticacion.html',{'formulario':form})
	

def cerrar_sesion(request):
	logout(request)
	return redirect('home')

def log_in(request):

	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)

		if form.is_valid():
			username= form.cleaned_data.get('username')
			password= form.cleaned_data.get('password')
			u = authenticate(username= username, password=password)

			if u is not None:
				login(request, u)
				return redirect('home')
			else:
				messages.error(request,'El usuario no existe')
		else:
			messages.error(request,'Tiene errores en sus credenciales')			


	form = AuthenticationForm()
	return render(request,'login/login.html',{'formulario':form})
