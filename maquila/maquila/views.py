from django.http import HttpResponse


"""
El funcionamiento esperado para el index es,
si el usuario tiene cookies que lo identifican 
entonce lo redirecciona al panel de el rol 

si no esta esto entonces lo mandara al login
"""
def index(request):
    return HttpResponse("Hello World");

