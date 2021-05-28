from django.db import models


"""
El modelo de una cuenta en el sistema
sirve para identificar los datos identidad y tipo de
cuenta que esta usando el sistema pues en identificar el usuario 
depende muchas veces el contenido que tenga que mostrarse al usuario
"""
class Account(models.Model):
    name = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

"""
El modelo de codigos de autorizacion
En Nuestro caso nuestro sistema no es publico por lo que
se requiere que un tipo de autorizacion para la creacion de una cuenta en un sistema
en este caso se dara por el codigo de 6 caracterez que tiene un vigencia de valides en el que puede ser
usado. 

En este caso el codigo de autorizacion puede ser creado por cualquier administrador

El codigo tiene que diferenciar el tipo de cuenta que puede crear.
"""
class AuthCode(models.Model):
    CATEGORY = (('Operator', 'Operator'),
                ('Administrator', 'Administrator'),
                ('Client', 'Client')) 

    code = models.CharField(max_length=6, null=False)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add = False)
    date_expired = models.DateTimeField(auto_now_add = False)

    def __str__(self):
        return self.code