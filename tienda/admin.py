from django.contrib import admin
from .models import categoriaProducto,Producto
# Register your models here.

class categoriaProducto_admin(admin.ModelAdmin):
	readonly_fields = ('created','updated')


class producto_admin(admin.ModelAdmin):
	readonly_fields = ('created','updated')

admin.site.register(categoriaProducto,categoriaProducto_admin)
admin.site.register(Producto,producto_admin)	