from django.contrib import admin
from .models import Pedidos, lineaPedido
# Register your models here.



admin.site.register([Pedidos,lineaPedido])