from django.shortcuts import render, redirect
from .carrito import Carro
from tienda.models import Producto
# Create your views here. 
def agregarProducto(request,producto_id):
	carro = Carro(request)
	
	producto = Producto.objects.get(id=producto_id)

	carro.agregarProductos(producto)

	return redirect('tienda')

def eliminarProducto(request,producto_id):
	carro = Carro(request)

	producto = Producto.objects.get(id=producto_id)

	carro.eliminarProductos(producto)

	return redirect('tienda')

def restarProducto(request,producto_id):
	carro = Carro(request)

	producto = Producto.objects.get(id=producto_id)

	carro.restarUnidades(producto)

	return redirect('tienda')		

def vaciarCarro(request):
	carro = Carro(request)
	carro.vaciarCarrito()
	return redirect('tienda')