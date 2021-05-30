from django.db import models

#Esto importa el modelo de usuario de Django
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver



"""
El modelo de una cuenta en el sistema
sirve para identificar los datos identidad y tipo de
cuenta que esta usando el sistema pues en identificar el usuario 
depende muchas veces el contenido que tenga que mostrarse al usuario


--Modificacion de Proposito.

Este modelo estaba pensando cumplir con el usuario.
Pero puede resultar mas eficiente usar esto como un perfil mas que
como una cuenta es decir un usuario tiene asignado un perfil.
Esta es una mejor opcion para hacer el sistema facil de construir
de esa forma aprovechar la robustes del sistema de usuarios
que tiene construido django.

Acount_id
User_id  Unique on table foreing key
rol
email

link que explica como hacer este cambio.
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
"""
class Account(models.Model):
    #Esta linea crea una tabla que se enlaza con
    #relacion uno a uno con la tabla de Usuarios de Django
    #Esta configurado en cascada cuando se borra el usuario
    #esta se barra tambien
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    rol = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    register_code = models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()

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