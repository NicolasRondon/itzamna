from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.template import loader

from .models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def send_email_user_created(sender, instance, created, **kwargs):
    if created:
        html_message = loader.render_to_string(
            'email/newmember.html',
            {
                'user_name': instance.username,
                'first_name': instance.first_name,
                'last_name': instance.last_name,
                'gender': instance.gender
            }
        )
        send_mail('Bienvenido', 'prueba', 'nuevo@academlo.com', [instance.email], fail_silently=True, html_message=html_message)
        print('Se envio el mail de creado')
