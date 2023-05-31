from django.urls import path
from . import views
urlpatterns = [
	path('',views.hacer_pedido,name='pedidos'),

]