from django.shortcuts import render

# Create your views here.


def createpedidos(request):
    return render(request, 'crearpedidos.html')

def pedidos_admin(request):
    return render(request, 'pedidosadmin.html')

def pedidos_client(request):
    return render(request, 'pedidosclient.html')

def actividades_worker(request):
    return render(request, 'actividadesworker.html')