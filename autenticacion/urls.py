from django.urls import path
from .views import vista_registro, cerrar_sesion, log_in

urlpatterns = [
    path('',vista_registro.as_view(),name='autenticacion'),
    path('cerrar_sesion',cerrar_sesion,name='cerrar'),
    path('cerrar_sesion',cerrar_sesion,name='cerrar'), 
    path('login',log_in,name='login')  
]

