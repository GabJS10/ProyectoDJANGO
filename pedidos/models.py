from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import Sum, F, FloatField

User = get_user_model()
# Create your models here.
class Pedidos(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	@property
	def total(self):
		return self.lineaPedido_set.aggregate(
			total=Sum(F('precio')*F('cantidad'), output_field=FloatField())
			)['total']

	class Meta:
		db_table='Pedidos'
		verbose_name='Pedido'
		verbose_name_plural='Pedidos'
		ordering=['id']

	def __str__(self):
		return self.id	


class lineaPedido(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
	pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.cantidad} unidades de {self.producto.nombre}"

	class Meta:
		db_table='linea_pedidos'
		verbose_name='linea pedido'
		verbose_name_plural='linea pedidos'
		ordering=['id']		