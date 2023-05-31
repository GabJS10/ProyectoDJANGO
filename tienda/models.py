from django.db import models

# Create your models here.

class categoriaProducto(models.Model):
	nombre = models.CharField(max_length=40)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		verbose_name='categoriaProducto'
		verbose_name_plural='categoriasProductos'

	def __str__(self):
		return f"{self.nombre}"	

class Producto(models.Model):
	nombre = models.CharField(max_length=30)
	categoria = models.ForeignKey(categoriaProducto, on_delete=models.CASCADE)
	imagen= models.ImageField(upload_to='tienda',null=True,blank=False)
	precio= models.FloatField()
	disponibilidad = models.BooleanField(default=True) 
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		verbose_name='producto'
		verbose_name_plural='productos'

	def __str__(self):
		return f"{self.nombre}"	
