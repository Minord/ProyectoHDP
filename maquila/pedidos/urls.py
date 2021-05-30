from django.urls import path
from . import views

urlpatterns = [
	path('crearpedido/', views.createpedidos, name="crearpedido"),
    path('pedidos_admin/', views.pedidos_admin, name="pedidos_admin"),
    path('pedidos_client/', views.pedidos_client, name="pedidos_client"),
    path('actividades_worker/', views.actividades_worker, name="actividades_worker"),
]