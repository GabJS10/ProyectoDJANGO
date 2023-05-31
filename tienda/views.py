from django.shortcuts import render
from .models import categoriaProducto, Producto
# Create your views here.
def tienda(request):


	if request.user.is_authenticated:
		producto = Producto.objects.all()
		return render(request,"tienda/tienda.html",{'productos':producto})
	else:
		return render(request,"tienda/noautenticado.html")
