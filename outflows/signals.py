from django.db.models.signals import post_save
from django.dispatch import receiver
from services.notify import NotifyService
from .models import Outflow

@receiver(post_save, sender=Outflow)
def update_outflow_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()

def send_outflow_notification(sender, instance, **kwargs):
    notify_service = NotifyService()

    data = {
        'product': str(instance.product),
        'quantity': instance.quantity,
    }

    notify_service.send_notification(data)
