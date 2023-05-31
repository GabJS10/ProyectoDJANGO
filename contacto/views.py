from django.shortcuts import render, redirect
from .forms import formContacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):



	formulario = formContacto()

	if request.method == 'POST':
		formulario = formContacto(data=request.POST)

		if formulario.is_valid():
			nombre = request.POST.get('nombre')
			email = request.POST.get('email')
			contenido = request.POST.get('contenido')


			email = EmailMessage('Mensaje desde Django',
				f"Te escribe {nombre} con email {email} te dice lo siguiente: {contenido}",
				"",["jgabis65@gmail.com"],reply_to=[email])


			try:
				email.send()
				return redirect('/contacto/?valido')
			except:
				return redirect('/contacto/?invalido')			



	return render(request,"contacto/contacto.html",{'formulario':formulario})				

