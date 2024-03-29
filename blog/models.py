from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	created= models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)

	class Meta():
		verbose_name='categoria'
		verbose_name_plural='categorias'

	def __str__(self):
		return f"{self.nombre}"
 

class Post(models.Model):
	titulo = models.CharField(max_length=50)
	contenido = models.CharField(max_length=50)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	categoria = models.ManyToManyField(Categoria)
	imagen= models.ImageField(upload_to='blog',null=True,blank=False)
	created= models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)

	class Meta():
		verbose_name='Post'
		verbose_name_plural='Posts'

	def __str__(self):
		return f"{self.titulo}"	
