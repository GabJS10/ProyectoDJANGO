from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carrito.carrito import Carro
from django.contrib import messages
from pedidos.models import Pedidos, lineaPedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from tienda.models import Producto
# Create your views here.

@login_required(login_url='/autenticacion/login')
def hacer_pedido(request):
	pedido = Pedidos.objects.create(user=request.user)

	carro = Carro(request)

	lista_linea_pedidos = list()
	total=0
	for key, value in carro.carrito.items():
		lista_linea_pedidos.append(lineaPedido(


			user = request.user,
			producto = Producto.objects.get(id=int(key)),
			pedido = pedido,
			cantidad = value['cantidad'],
			))

		total = total + float(value['precio'])

	  
	enviar_mail(
		pedido=pedido,
		lineas_pedido=lista_linea_pedidos,
		nombre=request.user.username,
		email=request.user.email,
		totalE=total
		)	

 
	messages.success(request,'Gracias por su compra')

	lineaPedido.objects.bulk_create(lista_linea_pedidos)
	carro.vaciarCarrito()
	return redirect('tienda')

def enviar_mail(**kwargs):
	asunto='Gracias por su pedido'
	mensaje=render_to_string('emails/pedidos.html',{

		'pedido':kwargs.get('pedido'),
		'lineas_pedido':kwargs.get('lineas_pedido'),
		'nombre':kwargs.get('nombre'),
		'email':kwargs.get('email'),
		'total':kwargs.get('totalE')
		})

	mensaje_procesado=strip_tags(mensaje)
	from_email='jgabis65@gmail.com'
	to=kwargs.get('email')

	send_mail(asunto,mensaje_procesado,from_email,[to],html_message=mensaje)
